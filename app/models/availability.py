from datetime import date
from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from config.database import Base


class Availability(Base):
    __tablename__ = "availability"

    start = Column(Date, default=date.today, primary_key=True)
    end = Column(Date, default=date.today, primary_key=True)
    listing_id = Column(Integer, ForeignKey("listings.id"), primary_key=True)

    listing = relationship("Listing", back_populates="availability")
