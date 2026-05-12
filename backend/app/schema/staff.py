from pydantic import BaseModel, EmailStr

class StaffSchema(BaseModel):
    name: str
    email:EmailStr
    department: str
    password: str

