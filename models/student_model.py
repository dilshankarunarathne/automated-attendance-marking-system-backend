from pydantic import BaseModel


class Student(BaseModel):
    index_number: str
    name: str | None = None
    adress: str | None = None
    gender: str | None = None
    date_of_birth: str | None = None
    parent_name
    contact_number
    grade
