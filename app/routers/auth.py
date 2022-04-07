from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.controllers.authControllers import login_user, register_user
from app.schemas.users import UserCreate
from app.schemas.tokens import Token
from app.config.database import get_db


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
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    return login_user(form_data, db)
