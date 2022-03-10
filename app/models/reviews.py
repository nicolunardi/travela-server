from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from config.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, primary_key=True, index=True)
    rating = Column(Float, default=3.5)
    listing_id = Column(Integer, ForeignKey("listings.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    listing = relationship("Listing", back_populates="reviews")
    owner = relationship("User")
