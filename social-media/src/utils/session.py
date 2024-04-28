from database import async_session
from sqlalchemy.ext.asyncio import AsyncSession


async def get_session() -> AsyncSession:
    """Getting async session"""
    async with async_session() as session:
        yield session
