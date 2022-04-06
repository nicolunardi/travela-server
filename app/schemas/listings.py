from pydantic import BaseModel
from datetime import date

from .reviews import Review
from .availability import Availability


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


class CreateBedroom(Bedroom):
    pass


class ListingMetadata(BaseModel):
    total_bedrooms: int = 0
    total_beds: int = 0
    type: str
    description: str = ""
    bathrooms: int = 0
    parking: int = 0
    images: list = []
    amenities: Amenities
    bedrooms: list


class ListingBase(BaseModel):
    thumbnail: str = ""
    price: float
    title: str
    address: Address


class AllListings(ListingBase):
    id: int
    owner_id: int
    reviews: list

    class Config:
        orm_mode = True


class AllListingsOut(BaseModel):
    listings: list[AllListings]


class CreateListing(ListingBase):
    total_bedrooms: int = 0
    total_beds: int = 0
    type: str
    description: str = ""
    bathrooms: int = 0
    parking: int = 0
    images: list = []
    amenities: Amenities
    bedrooms: list[CreateBedroom] = []


class CreateListingOut(BaseModel):
    listing_id: int


class ListingOut(ListingBase):
    id: int
    owner_id: int
    reviews: list
    availability: list
    published: bool
    posted_on: date
    metadata: ListingMetadata
    owner_name: str
