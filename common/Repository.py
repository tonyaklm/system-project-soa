from sqlalchemy import select, delete, update
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
import json
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Repository:
    """ Класс для шаблонных хождений в таблицу БД"""

    async def select_by_criteria(self, table: Base, columns: list, values: list, session: AsyncSession) -> json:
        """Makes select by given column names and expected values
        :rtype: object
        """

        items = select(table).where(getattr(table, columns[0]) == values[0])
        for i in range(1, len(columns)):
            items = items.where(getattr(table, columns[i]) == values[i])
        results = await session.execute(items)
        response_json = results.scalars().all()
        if not response_json:
            return []
        return response_json

    async def select_all(self, table, session: AsyncSession) -> json:
        """Makes select all available items"""

        stmt = select(table)
        results = await session.execute(stmt)
        response_json = results.scalars().all()
        return response_json

    async def post_item(self, table: Base, item: json, session: AsyncSession) -> Base:
        """Posts new item into given table"""

        new_item = table(**item)
        session.add(new_item)
        await session.commit()

        return new_item

    async def delete_item(self, table: Base, column: str, value, session: AsyncSession):
        """Deletes item by criteria from given table"""

        stmt = delete(table).where(getattr(table, column) == value)
        results = await session.execute(stmt)
        deleted_rows_count = results.rowcount
        await session.commit()
        return deleted_rows_count

    async def update_by_criteria(self, table: Base, column: str, expected_value: Any, new_values: json,
                                 session: AsyncSession):
        """Updates item by its unique key"""
        stmt = update(table).where(getattr(table, column) == expected_value).values(new_values)
        await session.execute(stmt)
        await session.commit()


repo = Repository()
