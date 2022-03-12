import bcrypt
from sqlalchemy.orm import Session
from email_validator import validate_email
from models.users import User as UserModel

# creates a hash of the password
def get_password_hash(password: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def check_valid_email(email: str) -> str:
    valid = validate_email(email)
    # Update with the normalized form.
    return valid.email
