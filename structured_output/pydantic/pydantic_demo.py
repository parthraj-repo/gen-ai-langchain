from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class student(BaseModel):

    name: str = 'nitish'        #( = ) for setting default value
    age: Optional[int] = None
    email: EmailStr              # to check valid email in passed dictionary
    cgpa: float=Field(gt=0, lt=10, default=5)  # for something in range 

new_student={'name':'nitish'}

student= student(**new_student)