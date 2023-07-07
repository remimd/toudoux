from uuid import UUID

from sources.models import ToDo


class ToDoRepository:
    async def get_by_id(self, todo_id: UUID) -> ToDo:
        ...
