from blacksheep import Application
from dotenv import load_dotenv

from sources import controllers  # noqa: F401
from sources.query import query

load_dotenv(override=True)

app = Application()


@app.on_start
async def setup(_):
    await query.setup()


@app.on_stop
async def clean(_):
    await query.clean()


@app.router.get("/")
def hello() -> str:
    return "Hello toto"
