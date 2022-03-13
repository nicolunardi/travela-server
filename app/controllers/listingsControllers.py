from fastapi import Depends
from sqlalchemy.orm import Session
from config.database import get_db
from models.listings import Listing as ListingModel
from models.images import Image as ImageModel
from models.bedroom import Bedroom as BedroomModel
from schemas.users import User
from schemas.listings import AllListings, CreateListing


def get_listings_list(db: Session = Depends(get_db)):
    pass


def create_new_listing(
    data: CreateListing, current_user: User, db: Session = Depends(get_db)
):
    # for listing model
    print(data)
    new_listing_data = {
        "thumbnail": data.thumbnail,
        "title": data.title,
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
    # for bedroom model
    bedrooms = data.bedrooms

    # for images
    return
