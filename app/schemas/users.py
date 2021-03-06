from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    name: str


class UserLogin(UserBase):
    password: str


class User(UserBase):
    id: int
    name: str

    class Config:
        orm_mode = True
