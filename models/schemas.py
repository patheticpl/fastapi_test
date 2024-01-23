from pydantic import BaseModel, EmailStr
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str

class SelfUser(UserBase):
    id: int



class User(UserBase):
    id: int
    age: int | None
    name: str | None
    class from_attributes:
        orm_mode = True

class Token(BaseModel):
    access_token: str