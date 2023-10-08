from pydantic import BaseModel


class Grade(BaseModel):
    student_index_number
    semester
    subject 
