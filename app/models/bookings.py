from datetime import date
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from app.config.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(15), nullable=False)
    start = Column(Date, default=date.today)
    end = Column(Date, default=date.today)
    total = Column(Integer, nullable=False)
    listing_id = Column(Integer, ForeignKey("listings.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    listing = relationship("Listing", back_populates="bookings")
    owner = relationship("User")
