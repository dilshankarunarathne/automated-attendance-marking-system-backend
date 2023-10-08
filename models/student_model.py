from typing import Any

from pydantic import BaseModel


class Student(BaseModel):
    index_number: str
    name: str | None = None
    address: str | None = None
    gender: str | None = None
    date_of_birth: str | None = None  # Date
    parent_name: str | None = None
    contact_number: str | None = None
    grade: str | None = None

    def __init__(self, **data: Any):
        super().__init__(**data)
        self.index_number=
