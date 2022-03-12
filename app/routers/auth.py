from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from dependencies.JWTtokens import create_access_token
from controllers.authControllers import create_user
from dependencies.authentication import get_password_hash
from schemas.users import UserCreate, User as UserSchema
from schemas.tokens import TokenPayload, Token
from config.database import get_db


router = APIRouter()


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=Token
)
async def register(
    user: UserCreate, response: Response, db: Session = Depends(get_db)
):
    new_user = create_user(db, user, response)
    # if the user was created without problems, generate the jwt token
    if new_user:
        print(new_user.email)
        token = create_access_token(
            data={"email": new_user.email, "name": new_user.name}
        )
        return {"token": token}
    else:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong.",
        )


@router.post("/login")
async def login():
    return {"message": "login"}


@router.post("/logout")
async def logout():
    return {"message": "logged out"}
