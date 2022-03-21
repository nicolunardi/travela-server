from fastapi import Depends
from sqlalchemy.orm import Session
from errors.exceptions import LISTING_NOT_FOUND
from config.database import get_db
from models.listings import Listing as ListingModel
from models.images import Image as ImageModel
from models.bedroom import Bedroom as BedroomModel
from schemas.users import User
from schemas.listings import AllListings, CreateListing
from dependencies.listings import (
    create_beds,
    create_images,
    create_all_listing_dict,
    create_listing_dict,
)


def get_listings_list(db: Session):
    db_listings = db.query(ListingModel).all()
    listings = []
    for listing in db_listings:
        listings.append(create_all_listing_dict(listing))
    return {"listings": listings}


def create_new_listing(data: CreateListing, current_user: User, db: Session):
    # for listing model
    new_listing_data = {
        "thumbnail": data.thumbnail,
        "title": data.title,
        "price": data.price,
        "description": data.description,
        "type": data.type,
        "owner_id": current_user.id,
        "street_number": data.address.street_number,
        "street_name": data.address.street_name,
        "suburb": data.address.suburb,
        "post_code": data.address.post_code,
        "state": data.address.state,
        "country": data.address.country,
        "bathrooms": data.bathrooms,
        "parking": data.parking,
        "total_bedrooms": data.total_bedrooms,
        "total_beds": data.total_beds,
        "wifi": data.amenities.wifi,
        "aircon": data.amenities.aircon,
        "kitchen": data.amenities.kitchen,
        "tv": data.amenities.tv,
        "heating": data.amenities.heating,
        "fridge": data.amenities.fridge,
        "microwave": data.amenities.microwave,
        "pool": data.amenities.pool,
    }
    new_listing = ListingModel(**new_listing_data)
    db.add(new_listing)
    db.commit()
    # for bedroom model
    bedrooms = data.bedrooms
    create_beds(bedrooms, db, new_listing.id)
    create_images(data.images, db, new_listing.id)
    return new_listing.id


def get_listing(listing_id: int, db: Session):
    db_listing = (
        db.query(ListingModel).filter(ListingModel.id == listing_id).first()
    )
    if not db_listing:
        raise LISTING_NOT_FOUND
    return create_listing_dict(db_listing)
