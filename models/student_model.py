from pydantic import BaseModel


class Student(BaseModel):
    index_number: str
    name
    adress
    gender
    date_of_birth
    parent_name
    contact_number
    grade
