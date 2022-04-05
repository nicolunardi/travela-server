from sqlalchemy.orm import Session
from schemas.availability import AvailabilityIn
from models.bedroom import Bedroom
from models.images import Image
from models.listings import Listing
from models.users import User
from models.availability import Availability
from models.bookings import Booking
from errors.exceptions import LISTING_NOT_FOUND_EXCEPTION


def create_beds(bedrooms: list[int], db: Session, listing_id: int):
    for bedroom in bedrooms:
        new_bed = Bedroom(listing_id=listing_id, beds=bedroom.beds)
        db.add(new_bed)

    db.commit()


def update_beds(bedrooms: list[int], db: Session, listing_id: int):
    # first delete all bedrooms associated with a listing
    db.query(Bedroom).filter_by(listing_id=listing_id).delete()
    # add new bedrooms
    create_beds(bedrooms, db, listing_id)


def create_images(images: list[str], db: Session, listing_id: int):
    for image in images:
        new_image = Image(listing_id=listing_id, image=image)
        db.add(new_image)

    db.commit()


def update_images(images: list[str], db: Session, listing_id: int):
    # first delete the images associated with the listing
    db.query(Image).filter_by(listing_id=listing_id).delete()
    # then add the new images to the db
    create_images(images, db, listing_id)


def get_address_dict(listing: Listing):
    address = {
        "street_number": listing.street_number,
        "street_name": listing.street_name,
        "suburb": listing.suburb,
        "post_code": listing.post_code,
        "state": listing.state,
        "country": listing.country,
    }
    return address


def get_amenities_dict(listing: Listing):
    amenities = {
        "wifi": listing.wifi,
        "aircon": listing.aircon,
        "kitchen": listing.kitchen,
        "tv": listing.tv,
        "heating": listing.heating,
        "fridge": listing.fridge,
        "microwave": listing.microwave,
        "pool": listing.pool,
    }
    return amenities


def get_metadata_dict(listing: Listing):
    metadata = {
        "total_bedrooms": listing.total_bedrooms,
        "total_beds": listing.total_beds,
        "type": listing.type,
        "description": listing.description,
        "bathrooms": listing.bathrooms,
        "parking": listing.parking,
        "images": listing.images,
        "amenities": get_amenities_dict(listing),
        "bedrooms": listing.bedrooms,
    }
    return metadata


def create_all_listing_dict(listing: Listing):
    listing_dict = {
        "thumbnail": listing.thumbnail,
        "price": listing.price,
        "title": listing.title,
        "address": get_address_dict(listing),
        "id": listing.id,
        "owner_id": listing.owner_id,
        "reviews": listing.reviews,
    }

    return listing_dict


def create_listing_dict(listing: Listing):
    listing_dict = {
        **create_all_listing_dict(listing),
        "availability": listing.availability,
        "published": listing.published,
        "posted_on": listing.posted_on,
        "metadata": get_metadata_dict(listing),
        "owner_name": listing.owner.name,
    }
    return listing_dict


def listing_belongs_to_user(listing: Listing, user: User):
    return user.id == listing.owner_id


def get_listing_by_id(listing_id: int, db: Session):
    db_listing: Listing = (
        db.query(Listing).filter(Listing.id == listing_id).first()
    )
    if not db_listing:
        raise LISTING_NOT_FOUND_EXCEPTION

    return db_listing


def create_availabilities(listing_id: int, data: AvailabilityIn, db: Session):
    for availability in data.availability:
        new_availability = Availability(
            start=availability.start,
            end=availability.end,
            listing_id=listing_id,
        )
        db.add(new_availability)

    db.commit()


def find_booking_by_listing_user(
    booking_id: int, listing_id: int, user: User, db: Session
):
    return db.query(Booking).filter_by(
        id=booking_id, listing_id=listing_id, owner_id=user.id
    )
