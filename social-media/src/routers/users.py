from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
import json
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, DataError, DBAPIError
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from common.Repository import repo
import models
from User import User
from start_session import get_session
from passwords import encrypt_password, check_encrypted_password

router = APIRouter()


@router.post("/registration", status_code=200, summary="Register a new user", tags=['user'])
async def user_registration(user: models.BaseUser, session: AsyncSession = Depends(get_session)):
    json_user = json.loads(user.model_dump_json())
    try:
        json_user['date_of_birth'] = datetime.strptime(user.date_of_birth, "%m.%d.%Y")
    except ValueError:
        raise HTTPException(status_code=400, detail="Неверные данные о дате")
    json_user['password'] = encrypt_password(user.password)
    try:
        new_user = await repo.post_item(User, json_user, session)
    except IntegrityError:
        raise HTTPException(status_code=409,
                            detail=f"Пользователять с логином {user.login} уже существует, придумайте другой")
    except DBAPIError or DataError:
        raise HTTPException(status_code=400, detail="Переданы неверные данные")
    return JSONResponse(status_code=200, content={
        "message": f"Пользователь {new_user.login} успешно зарегистрирован"})


@router.put("/profile", status_code=200, summary="Update profile data", tags=['user'])
async def update_profile(new_data: models.BaseUpdateData, session: AsyncSession = Depends(get_session)):
    json_new_data = json.loads(new_data.model_dump_json())
    try:
        json_new_data['date_of_birth'] = datetime.strptime(new_data.date_of_birth, "%m.%d.%Y")
    except ValueError:
        raise HTTPException(status_code=400, detail="Неверные данные о дате")
    await repo.update_by_criteria(User, 'login', new_data.login, json_new_data, session)
    return JSONResponse(status_code=200, content={
        "message": f"Данные успешно обновлены"})


@router.get("/authentication", status_code=200, summary="User authorization", tags=['user'])
async def user_authorization(authorization_data: models.BaseAuthorizationData,
                             session: AsyncSession = Depends(get_session)):
    user = await repo.select_by_criteria(User, ["login"], [authorization_data.login], session)
    if not user:
        return JSONResponse(status_code=404, content={
            "message": f"Пользователь с логином {authorization_data.login} не существует"})
    if check_encrypted_password(authorization_data.password, user[0].password):
        return JSONResponse(status_code=200, content={
            "message": f"Авторизация прошла успешно",
            "user_id": user[0].id})
    return JSONResponse(status_code=400, content={
        "message": f"Неверный пароль"})
