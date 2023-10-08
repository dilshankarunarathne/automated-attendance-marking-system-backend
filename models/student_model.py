from pydantic import BaseModel


class Student(BaseModel):
    index_number: str
    name: str | None = None
    adress: str | None = None
    gender
    date_of_birth
    parent_name
    contact_number
    grade
