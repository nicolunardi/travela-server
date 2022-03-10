from sqlalchemy import Column, ForeignKey, Integer, Text
from config.database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(Text)
    listing_id = Column(Integer, ForeignKey("listing.id"))
