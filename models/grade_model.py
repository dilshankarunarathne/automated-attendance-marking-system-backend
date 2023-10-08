from pydantic import BaseModel


class Grade(BaseModel):
    student_index_number: str
    semester: str
    subject: str
    marks
    grade: str 
