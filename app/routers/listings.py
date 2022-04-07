from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.listings import Listing as ListingModel
from app.models.reviews import Review as ReviewModel
from app.models.images import Image as ImageModel
from app.models.bedroom import Bedroom as BedroomModel
from app.models.availability import Availability as AvailabilityModel

from app.schemas.listings import (
    CreateListing,
    AllListingsOut,
    ListingOut,
    CreateListingOut,
)
from app.schemas.reviews import ReviewIn, ReviewOut
from app.schemas.availability import AvailabilityIn
from app.schemas.users import User
from app.controllers import listingsControllers
from app.config.database import get_db
from app.dependencies.JWTtokens import get_current_user

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
    return listingsControllers.update_listing(
        listing_id, data, db, current_user
    )


@router.delete("/{listing_id}", tags=["Listings"])
async def delete_listing(
    listing_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return listingsControllers.delete_listing(listing_id, db, current_user)


@router.put("/publish/{listing_id}", tags=["Listings"])
async def publish_listing(
    listing_id: int,
    data: AvailabilityIn,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return listingsControllers.publish_listing(
        listing_id, data, db, current_user
    )


@router.put("/unpublish/{listing_id}", tags=["Listings"])
async def unpublish_listing(
    listing_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return listingsControllers.unpublish_listing(listing_id, db, current_user)


@router.post(
    "/{listing_id}/review/{booking_id}",
    tags=["Listings"],
    response_model=ReviewOut,
)
async def review_listing(
    listing_id: str,
    booking_id: str,
    data: ReviewIn,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return listingsControllers.post_review(
        listing_id, booking_id, data, db, current_user
    )
