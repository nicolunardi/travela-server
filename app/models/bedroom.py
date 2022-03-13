from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from config.database import Base


class Bedroom(Base):
    __tablename__ = "bedrooms"

    id = Column(Integer, primary_key=True, index=True)
    listing_id = Column(Integer, ForeignKey("listings.id"))
    beds = Column(Integer, default=0)
