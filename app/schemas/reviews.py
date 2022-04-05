from pydantic import BaseModel


class Review(BaseModel):
    id: int
    text: str
    rating: float
    listing_id: int
    owner_id: int


class CreateReview(BaseModel):
    rating: int
    text: str


class ReviewIn(BaseModel):
    review: CreateReview
