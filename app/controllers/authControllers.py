from fastapi import HTTPException, status
from email_validator import EmailNotValidError
from sqlalchemy.orm import Session
from schemas.tokens import Token
from models.users import User as UserModel
from schemas.users import UserCreate, UserLogin
from dependencies.authentication import (
    get_password_hash,
    check_valid_email,
    get_user_by_email,
    verify_password,
)
from dependencies.JWTtokens import create_access_token


def create_user(db: Session, user: UserCreate):
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


def register_user(db: Session, user: UserCreate):
    new_user = create_user(db, user)
    # if the user was created without problems, generate the jwt token
    if new_user:
        print(new_user.email)
        token = create_access_token(
            data={"email": new_user.email, "name": new_user.name}
        )
        return Token(name=new_user.name, email=new_user.email, token=token)
    else:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong.",
        )


def login_user(db: Session, data: UserLogin):
    # check if the user exists in the db
    curr_user = get_user_by_email(db, data.email)
    if not curr_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user exists with that email address.",
        )

    # check if the passwords match
    if not verify_password(data.password, curr_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect password.",
        )
    token = create_access_token(
        data={"email": curr_user.email, "name": curr_user.name}
    )
    return Token(email=curr_user.email, name=curr_user.name, token=token)