from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(20), nullable=False)
    hashed_password = Column(LargeBinary, nullable=False)

    listings = relationship("Listing", back_populates="owner")
