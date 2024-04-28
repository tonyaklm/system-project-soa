import json
from common.repository import repo
from database import async_session
from tables.statistics import Statistics


async def consume_statistics(msg: json) -> None:
    async with async_session() as session:
        await repo.post_item(Statistics, msg, session)
