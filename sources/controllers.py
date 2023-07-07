from functools import cached_property
from uuid import UUID

from blacksheep import Response, pretty_json
from blacksheep.server.controllers import ApiController, get

from sources.services import ToDoService, todo_service


class ToDoController(ApiController):
    @cached_property
    def service(self) -> ToDoService:
        return todo_service

    @classmethod
    def class_name(cls) -> str:
        return "todo"

    @get(":todo_id")
    async def get_by_id(self, todo_id: UUID) -> Response:
        todo = await self.service.get_by_id(todo_id)
        return pretty_json(data=todo)
