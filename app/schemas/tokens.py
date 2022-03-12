from pydantic import BaseModel


class Token(BaseModel):
    email: str
    name: str
    token: str


class TokenPayload(BaseModel):
    name: str
    email: str
