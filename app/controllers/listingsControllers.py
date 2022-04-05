from sqlalchemy.orm import Session
from errors.exceptions import (
    USER_NOT_OWNER_EXCEPTION,
    BOOKING_WITH_LISTING_AND_USER_EXCEPTION,
)
from models.listings import Listing as ListingModel
from models.reviews import Review as ReviewModel
from schemas.users import User
from schemas.listings import CreateListing
from schemas.availability import AvailabilityIn
from schemas.reviews import ReviewIn
from dependencies.listings import (
    create_beds,
    create_images,
    create_all_listing_dict,
    create_listing_dict,
    update_beds,
    update_images,
    listing_belongs_to_user,
    get_listing_by_id,
    create_availabilities,
    find_booking_by_listing_user,
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
        "thumbnail": data.thumbnail,  # done
        "title": data.title,  # done
        "price": data.price,  # done
        "description": data.description,
        "type": data.type,  # done
        "owner_id": current_user.id,  # done
        "street_number": data.address.street_number,  # done
        "street_name": data.address.street_name,  # done
        "suburb": data.address.suburb,  # done
        "post_code": data.address.post_code,
        "state": data.address.state,  # done
        "country": data.address.country,  # done
        "bathrooms": data.bathrooms,  # done
        "parking": data.parking,  # done
        "total_bedrooms": data.total_bedrooms,  # done
        "total_beds": data.total_beds,  # done
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
    create_beds(data.bedrooms, db, new_listing.id)
    create_images(data.images, db, new_listing.id)
    print(new_listing.listing_id)
    return new_listing.listing_id


def get_listing(listing_id: int, db: Session):
    db_listing: ListingModel = get_listing_by_id(listing_id, db)

    return create_listing_dict(db_listing)


def update_listing(
    listing_id: int, data: CreateListing, db: Session, current_user: User
):
    db_listing: ListingModel = get_listing_by_id(listing_id, db)

    # ensure the current user is the owner of the listing that is to be edited
    if not listing_belongs_to_user(db_listing, current_user):
        raise USER_NOT_OWNER_EXCEPTION

    # format the data for the listing model
    update_listing_data = {
        "thumbnail": data.thumbnail,  # done
        "title": data.title,  # done
        "price": data.price,  # done
        "description": data.description,
        "type": data.type,  # done
        "owner_id": current_user.id,  # done
        "street_number": data.address.street_number,  # done
        "street_name": data.address.street_name,  # done
        "suburb": data.address.suburb,  # done
        "post_code": data.address.post_code,
        "state": data.address.state,  # done
        "country": data.address.country,  # done
        "bathrooms": data.bathrooms,  # done
        "parking": data.parking,  # done
        "total_bedrooms": data.total_bedrooms,  # done
        "total_beds": data.total_beds,  # done
        "wifi": data.amenities.wifi,
        "aircon": data.amenities.aircon,
        "kitchen": data.amenities.kitchen,
        "tv": data.amenities.tv,
        "heating": data.amenities.heating,
        "fridge": data.amenities.fridge,
        "microwave": data.amenities.microwave,
        "pool": data.amenities.pool,
    }
    # update the values of the db listing
    for key, value in update_listing_data.items():
        setattr(db_listing, key, value)

    # update bedrooms
    update_beds(data.bedrooms, db, listing_id)

    # update images
    update_images(data.images, db, listing_id)

    db.commit()

    return {}


def delete_listing(listing_id: int, db: Session, current_user: User):
    db_listing: ListingModel = get_listing_by_id(listing_id, db)

    # ensure the current user is the owner of the listing that is to be edited
    if not listing_belongs_to_user(db_listing, current_user):
        raise USER_NOT_OWNER_EXCEPTION

    db.delete(db_listing)
    db.commit()
    return {}


def publish_listing(
    listing_id: int, data: AvailabilityIn, db: Session, current_user: User
):
    db_listing: ListingModel = get_listing_by_id(listing_id, db)

    if not listing_belongs_to_user(db_listing, current_user):
        raise USER_NOT_OWNER_EXCEPTION

    create_availabilities(listing_id, data, db)

    db_listing.published = True

    db.commit()

    return {}


def unpublish_listing(listing_id: int, db: Session, current_user: User):
    db_listing: ListingModel = get_listing_by_id(listing_id, db)

    if not listing_belongs_to_user(db_listing, current_user):
        raise USER_NOT_OWNER_EXCEPTION

    db_listing.published = False

    db.commit()

    return {}


# booking id is needed only to make sure that a valid booking exists, as users can
# only post reviews after they have a valid booking
def post_review(
    listing_id: int,
    booking_id: int,
    data: ReviewIn,
    db: Session,
    current_user: User,
):
    # check a booking exists with user id and listing id and booking id
    db_booking = find_booking_by_listing_user(
        booking_id, listing_id, current_user, db
    )
    if not db_booking:
        raise BOOKING_WITH_LISTING_AND_USER_EXCEPTION

    newReview = ReviewModel(**data)
    db.add(newReview)
    db.commit()
    return {}
