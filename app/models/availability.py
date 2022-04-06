from datetime import date
from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from config.database import Base


class Availability(Base):
    __tablename__ = "availability"

    id = Column(Integer, primary_key=True, index=True)
    start = Column(Date, default=date.today)
    end = Column(Date, default=date.today)
    listing_id = Column(Integer, ForeignKey("listings.id"))

    listing = relationship("Listing", back_populates="availability")
