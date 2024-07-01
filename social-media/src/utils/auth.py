from fastapi import HTTPException, status, Depends, Header
from tables.user import User
from tables.session_dao import SessionDao
from utils.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from common.repository import repo
from uuid import UUID


async def check_session_key(session_key: UUID, db_session: AsyncSession):
    active_session = await repo.select_by_criteria(SessionDao, ["session_key"], [session_key], db_session)
    return [] != active_session


async def get_user_from_session_key(session_key: UUID, db_session: AsyncSession) -> User:
    active_session = await repo.select_by_criteria(SessionDao, ["session_key"], [session_key], db_session)

    user = await repo.select_by_criteria(User, ["id"], [active_session[0].user_id], db_session)
    return user[0]


async def get_user(session_key: UUID = Header(...), db_session: AsyncSession = Depends(get_session)) -> User:
    if await check_session_key(session_key, db_session):
        user = await get_user_from_session_key(session_key, db_session)
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Missing or invalid Session key"
    )
