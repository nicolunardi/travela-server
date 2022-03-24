from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.listings import Listing as ListingModel
from models.reviews import Review as ReviewModel
from models.images import Image as ImageModel
from models.bedroom import Bedroom as BedroomModel
from models.availability import Availability as AvailabilityModel

from schemas.listings import (
    CreateListing,
    AllListingsOut,
    ListingOut,
    CreateListingOut,
)
from schemas.users import User
from controllers import listingsControllers
from config.database import get_db
from dependencies.JWTtokens import get_current_user

router = APIRouter()


@router.get("/", tags=["Listings"], response_model=AllListingsOut)
async def get_all_listings(db: Session = Depends(get_db)):
    return listingsControllers.get_listings_list(db)


@router.post("/new", tags=["Listings"], response_model=CreateListingOut)
async def create_listing(
    data: CreateListing,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    listing_id = listingsControllers.create_new_listing(data, current_user, db)
    return CreateListingOut(listing_id=listing_id)


@router.get("/{listing_id}", tags=["Listings"], response_model=ListingOut)
async def get_listing(listing_id: int, db: Session = Depends(get_db)):
    return listingsControllers.get_listing(listing_id, db)


@router.put("/{listing_id}", tags=["Listings"])
async def update_listing(
    data: CreateListing,
    listing_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return listingsControllers.update_listing(listing_id, data, db, current_user)


@router.delete("/{listing_id}")
async def delete_listing(listing_id: str):
    return {"message": f"delete listing {listing_id}"}


@router.put("/publish/{listing_id}")
async def publish_listing(listing_id: str):
    return {"message": f"publish listing {listing_id}"}


@router.put("/unpublish/{listing_id}")
async def unpublish_listing(listing_id: str):
    return {"message": f"unpublish listing {listing_id}"}


@router.put("/publish/{listing_id}/review/{booking_id}")
async def review_listing(listing_id: str, booking_id: str):
    return {"message": f"review listing {listing_id} for booking {booking_id}"}
