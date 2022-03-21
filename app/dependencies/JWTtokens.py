import os
from dotenv import load_dotenv, find_dotenv
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from dependencies.authentication import get_user_by_email
from config.database import get_db
from schemas.users import User

from schemas.tokens import TokenPayload
from errors.exceptions import CREDENTIALS_EXCEPTION


load_dotenv(find_dotenv())

JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/auth/login")


def create_access_token(data: dict):
    to_encode = data.copy()
    token = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    try:
        # get the teh user data from the token
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        # if the email doesnt exist reject the request
        if payload.get("email") is None:
            raise CREDENTIALS_EXCEPTION
        # destructure the payload
        token_payload = TokenPayload(**payload)
    except JWTError:
        raise CREDENTIALS_EXCEPTION

    # get the user from the DB to ensure the one from the token is valid
    user = get_user_by_email(db, token_payload.email)
    if user is None:
        raise CREDENTIALS_EXCEPTION
    return User(email=user.email, id=user.id, name=user.name)


def fake_token(token: str):
    return TokenPayload(name="john", email="john@test.com", id=4)
