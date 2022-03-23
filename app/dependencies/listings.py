from sqlalchemy.orm import Session
from models.bedroom import Bedroom
from models.images import Image
from models.listings import Listing


def create_beds(bedrooms: list[int], db: Session, listing_id: int):
    for bedroom in bedrooms:
        new_bed = Bedroom(listing_id=listing_id, beds=bedroom.beds)
        db.add(new_bed)

    db.commit()


def create_images(images: list[str], db: Session, listing_id: int):
    for image in images:
        new_image = Image(listing_id=listing_id, image=image)
        db.add(new_image)

    db.commit()


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
    }
    return listing_dict
