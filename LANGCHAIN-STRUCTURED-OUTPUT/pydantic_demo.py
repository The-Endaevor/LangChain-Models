from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'susheel'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10, default=5, description='A decimal value representing the cgpa of the student')


# new_student = {'name':'Susheel Reddy'}
new_student = {'age':27, 'email':'basa@xyz.com', 'cgpa':9}

student = Student(**new_student)

print(student) #student.name

new_student = dict(student) # To Dictionary

print(new_student['age'])

print(student.model_dump_json()) # To JSON

