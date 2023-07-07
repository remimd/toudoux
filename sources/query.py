from os import getenv
from typing import Any

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
        await self.__connection.close()

    async def fetch(self, raw_sql: str) -> dict[str, Any]:
        async with self.__connection.cursor() as cursor:
            return await cursor.fetch(raw_sql)


query = Q()
