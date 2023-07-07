from uuid import UUID

from sources.models import ToDo
from sources.repositories import ToDoRepository, todo_repository


class ToDoService:
    def __init__(self, __todo_repository: ToDoRepository):
        self.todo_repository = __todo_repository

    async def get_by_id(self, todo_id: UUID) -> ToDo:
        return await self.todo_repository.get_by_id(todo_id)


todo_service = ToDoService(todo_repository)
