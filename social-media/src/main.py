import uvicorn
from fastapi import Depends
from fastapi import FastAPI, HTTPException
import json
from fastapi.responses import JSONResponse
from sqlalchemy import true
from sqlalchemy.exc import IntegrityError, DataError, DBAPIError
from passlib.context import CryptContext
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from models import BaseUser, BaseUpdateData, BaseAuthorizationData
from Repository import Repository
from User import User
from start_session import get_session, cli

app = FastAPI()

repo = Repository()

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000
)


def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)


@app.post("/registration", status_code=200, summary="Register a new user")
async def user_registration(user: BaseUser, session: AsyncSession = Depends(get_session)):
    json_user = json.loads(user.model_dump_json())
    try:
        json_user['date_of_birth'] = datetime.strptime(user.date_of_birth, "%m.%d.%Y")
    except ValueError:
        raise HTTPException(status_code=400, detail="Неверные данные о дате")
    json_user['password'] = encrypt_password(user.password)
    try:
        new_user = await repo.post_item(User, json_user, session)
    except IntegrityError:
        raise HTTPException(status_code=409, detail=f"Логин {user.login} уже существует, придумайте другой")
    except DBAPIError or DataError:
        raise HTTPException(status_code=400, detail="Переданы неверные данные")
    return JSONResponse(status_code=200, content={
        "message": f"Пользователь {new_user.login} успешно зарегистрирован"})


@app.post("/update-data", status_code=200, summary="Update users data")
async def update_data(new_data: BaseUpdateData, session: AsyncSession = Depends(get_session)):
    json_new_data = json.loads(new_data.model_dump_json())
    try:
        json_new_data['date_of_birth'] = datetime.strptime(new_data.date_of_birth, "%m.%d.%Y")
    except ValueError:
        raise HTTPException(status_code=400, detail="Неверные данные о дате")
    await repo.update_by_criteria(User, 'login', new_data.login, json_new_data, session)
    return JSONResponse(status_code=200, content={
        "message": f"Данные успешно обновлены"})


@app.get("/authentication", status_code=200, summary="User authorization")
async def user_authorization(authorization_data: BaseAuthorizationData,
                             session: AsyncSession = Depends(get_session)):
    user = await repo.select_by_criteria(User, ["login"], [authorization_data.login], session)
    if not user:
        return JSONResponse(status_code=404, content={
            "message": f"Пользователь с логином {authorization_data.login} не существует"})
    if check_encrypted_password(authorization_data.password, user.password):
        return JSONResponse(status_code=200, content={
            "message": f"Авторизация прошла успешно"})
    return JSONResponse(status_code=400, content={
        "message": f"Неверный пароль"})


# Использовала для дебага
# @app.get("/get-all-users", status_code=200, summary="User authorization")
# async def get_users(session: AsyncSession = Depends(get_session)):
#     return await repo.select_all(User, session)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", reload=true)
    cli()
