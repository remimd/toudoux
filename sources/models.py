from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(kw_only=True, slots=True)
class Do:
    title: str
    id: UUID = field(default_factory=uuid4)


@dataclass(kw_only=True, slots=True)
class ToDo:
    name: str
    list: list[Do] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)
