from pydantic import BaseModel
from .reviews import Review


class Address(BaseModel):
    street_number: int
    street_name: str
    suburb: str
    post_code: int
    state: str
    country: str


class Amenities(BaseModel):
    wifi: bool = False
    aircon: bool = False
    kitchen: bool = False
    tv: bool = False
    heating: bool = False
    fridge: bool = False
    microwave: bool = False
    pool: bool = False


class Image(BaseModel):
    image: str = ""


class Bedroom(BaseModel):
    beds: int = 0


class ListingBase(BaseModel):
    thumbnail: str = ""
    price: float
    title: str
    address: Address


class AllListings(ListingBase):
    id: int
    owner: int
    reviews: list[Review] = []

    class Config:
        orm_mode = True


class CreateListing(ListingBase):
    total_bedrooms: int = 0
    total_beds: int = 0
    type: str
    description: str = ""
    bathrooms: int = 0
    parking: int = 0
    images: list[Image] = []
    amenities: Amenities
    bedrooms: list[Bedroom] = []
