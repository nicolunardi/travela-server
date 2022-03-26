from sqlalchemy import Column, ForeignKey, Integer, Text
from config.database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(Text)
    listing_id = Column(Integer, ForeignKey("listings.id"))

    def __repr__(self) -> str:
        return f"Image: id = {self.id}, listing = {self.listing_id}"
