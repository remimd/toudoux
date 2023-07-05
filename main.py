from os import getenv

from asyncmy import Connection, connect
from blacksheep import Application
from dotenv import load_dotenv

load_dotenv(override=True)

app = Application()
connection: Connection | None = None


@app.on_start
async def setup(_):
    global connection
    connection = await connect(
        host=getenv("DB_HOST", "localhost"),
        port=getenv("DB_PORT", "3304"),
        user=getenv("DB_USER", "root"),
        password=getenv("DB_PASSWORD", "root"),
        database=getenv("DB_NAME", "db"),
    )


@app.on_stop
async def clean(_):
    await connection.close()


@app.router.get("/hello")
async def hello() -> str:
    return "Hello world!"
