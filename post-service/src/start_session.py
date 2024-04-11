from sqlalchemy.ext.asyncio import create_async_engine
import sqlalchemy.orm
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from config import settings

engine = create_async_engine(settings.database_url, echo=True)
Base = sqlalchemy.orm.declarative_base()
async_session = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session() -> AsyncSession:
    """Getting async session"""
    async with async_session() as session:
        yield session
