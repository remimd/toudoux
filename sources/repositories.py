from uuid import UUID

from sources.models import Do, ToDo
from sources.query import query


class ToDoRepository:
    async def get_by_id(self, todo_id: UUID) -> ToDo:
        todo_data = await query.fetch_one(
            f"SELECT * FROM todo WHERE id = '{todo_id}' LIMIT 1"
        )
        do_list_data = await query.fetch(
            f"SELECT * FROM do WHERE todo_id = '{todo_id}'"
        )
        do_list = [Do(id=data["id"], title=data["title"]) for data in do_list_data]
        return ToDo(do_list=do_list, **todo_data)


todo_repository = ToDoRepository()
