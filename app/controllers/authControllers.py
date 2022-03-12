from fastapi import HTTPException, status, Response
from email_validator import EmailNotValidError
from sqlalchemy.orm import Session
from models.users import User as UserModel
from schemas.users import UserCreate
from dependencies.authentication import (
    get_password_hash,
    check_valid_email,
    get_user_by_email,
)


def create_user(db: Session, user: UserCreate, response: Response):
    # check the email address isn't already in use
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered.",
        )

    # ensure the email address is valid
    try:
        email = check_valid_email(user.email)
    except EmailNotValidError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    hashed_password = get_password_hash(user.password)

    # create the user
    new_user = UserModel(
        email=user.email, name=user.name, hashed_password=hashed_password
    )
    # add the user to the db
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
