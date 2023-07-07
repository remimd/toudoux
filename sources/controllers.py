from blacksheep import Response
from blacksheep.server.controllers import ApiController, get


class ToDoController(ApiController):
    @classmethod
    def class_name(cls) -> str:
        return "todo"

    @get(":todo_id")
    async def get_by_id(self, todo_id: str) -> Response:
        ...
