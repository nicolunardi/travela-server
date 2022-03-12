from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from controllers.authControllers import login_user, register_user
from schemas.users import UserCreate, UserLogin, GetUser
from schemas.tokens import Token
from config.database import get_db


router = APIRouter()


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=Token,
    tags=["User"],
)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=Token,
    tags=["User"],
)
async def login(data: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, data)
