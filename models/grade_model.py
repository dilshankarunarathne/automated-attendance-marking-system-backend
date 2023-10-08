from pydantic import BaseModel


class Grade(BaseModel):
    student_index_number: str
    semester
    subject
    marks
    gade
