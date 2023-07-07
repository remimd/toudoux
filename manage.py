import asyncio
from os import getcwd
from pathlib import Path

import click
from asyncmy.errors import OperationalError

from sources.query import query


@click.group
def cli():
    ...


@cli.command
def init_db():
    sql = Path(getcwd()) / "migrations" / "0001.sql"

    with open(sql, "r") as file:
        raw_sql = file.read()

    async def execute():
        await query.setup()
        await query.execute(raw_sql)
        await query.clean()

    coroutine = execute()
    try:
        asyncio.run(coroutine)
    except OperationalError:
        print("Database already initialized")
    else:
        print("Database initialized")


if __name__ == "__main__":
    cli()
