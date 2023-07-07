from os import getenv
from typing import Any, Iterable

from asyncmy import Connection, connect


class Q:
    __slots__ = ("__connection",)

    __connection: Connection | None

    def __init__(self):
        self.__connection = None

    async def setup(self):
        self.__connection = await connect(
            host=getenv("DB_HOST", "localhost"),
            port=int(getenv("DB_PORT", "3306")),
            user=getenv("DB_USER", "root"),
            password=getenv("DB_PASSWORD", "root"),
            database=getenv("DB_NAME", "toudoux"),
        )

    async def clean(self):
        self.__connection.close()

    async def execute(self, raw_sql: str):
        async with self.__connection.cursor() as cursor:
            await cursor.execute(raw_sql)

    async def fetch(self, raw_sql: str) -> Iterable[dict[str, Any]]:
        async with self.__connection.cursor() as cursor:
            await cursor.execute(raw_sql)
            response = await cursor.fetchall()

        return tuple(
            {column[0]: value for column, value in zip(cursor.description, data)}
            for data in response
        )


query = Q()
