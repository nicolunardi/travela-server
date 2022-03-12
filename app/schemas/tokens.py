from pydantic import BaseModel


class Token(BaseModel):
    token: str


class TokenPayload(BaseModel):
    name: str
    email: str
