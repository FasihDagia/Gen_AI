from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):

    name: str
    age: Optional[int] =None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=4,description="A decimal value representing student cgpa")

new_student = {"name":"Fasih","email":"abc@gmail.com","cgpa":2.7}

student = Student(**new_student)

student = student.model_dump_json()

print(student)