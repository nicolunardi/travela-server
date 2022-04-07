from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from app.config.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, index=True)
    rating = Column(Integer, default=3)
    listing_id = Column(Integer, ForeignKey("listings.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    listing = relationship("Listing", back_populates="reviews")
    owner = relationship("User")
