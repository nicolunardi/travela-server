from datetime import date
from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from config.database import Base


class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    thumbnail = Column(Text)
    title = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    posted_on = Column(Date, default=date.today)
    published = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    street_number = Column(Integer, nullable=False)
    street_name = Column(String(50), nullable=False)
    suburb = Column(String(30), nullable=False)
    post_code = Column(Integer, nullable=False)
    state = Column(String(30))
    country = Column(String(30), nullable=False)
    description = Column(Text)
    type = Column(String(20))
    total_bedrooms = Column(Integer, default=0)
    total_beds = Column(Integer, default=0)
    bathrooms = Column(Integer, default=0)
    parking = Column(Integer, default=0)
    wifi = Column(Boolean, default=False)
    aircon = Column(Boolean, default=False)
    kitchen = Column(Boolean, default=False)
    tv = Column(Boolean, default=False)
    heating = Column(Boolean, default=False)
    fridge = Column(Boolean, default=False)
    microwave = Column(Boolean, default=False)
    pool = Column(Boolean, default=False)

    owner = relationship("User", back_populates="listings")
    reviews = relationship("Review", back_populates="listing")
    bookings = relationship("Booking", back_populates="listing")
    availability = relationship("Availability", back_populates="listing")
    bedrooms = relationship("Bedroom")
    images = relationship("Image")

    @property
    def listing_id(self):
        return self.id
