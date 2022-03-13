from pydantic import BaseModel


class Review(BaseModel):
    id: int
    text: str
    rating: float
    listing_id: int
    owner_id: int
