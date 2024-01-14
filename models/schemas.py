from pydantic import BaseModel, EmailStr
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    age: int | None
    name: str | None
    email: EmailStr
    class from_attributes:
        orm_mode = True