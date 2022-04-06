from sqlalchemy.orm import Session
from errors.exceptions import USER_NOT_OWNER_EXCEPTION
from dependencies.listings import get_listing_by_id, listing_belongs_to_user
from dependencies.bookings import get_booking_by_id
from schemas.bookings import (
    BookingOut,
    CreateBookingIn,
    CreateBookingOut,
    Booking,
)
from models.bookings import Booking as BookingModel
from schemas.users import User


def get_bookings(db: Session):
    db_bookings = db.query(BookingModel).all()
    all_bookings = []
    for booking in db_bookings:
        all_bookings.append(
            Booking(
                id=booking.id,
                start=booking.start,
                end=booking.end,
                total=booking.total,
                listing_id=booking.listing_id,
                owner_id=booking.owner_id,
                status=booking.status,
            )
        )
    return BookingOut(bookings=all_bookings)


def create_booking(
    listing_id: int, data: CreateBookingIn, db: Session, curr_user: User
):
    new_booking = BookingModel(
        status="pending",
        start=data.date_range.start,
        end=data.date_range.end,
        listing_id=listing_id,
        owner_id=curr_user.id,
        total=data.total,
    )
    print(new_booking.id)
    db.add(new_booking)
    db.commit()
    return CreateBookingOut(id=new_booking.id)


def accept_booking(booking_id: int, db: Session, curr_user: User):
    db_booking = get_booking_by_id(booking_id, db)
    # get the listing from the db to verify the curr_user is the owner
    # of the listing
    db_listing = get_listing_by_id(db_booking.listing_id, db)
    if not listing_belongs_to_user(db_listing, curr_user):
        raise USER_NOT_OWNER_EXCEPTION

    db_booking.status = "accepted"
    db.commit()
    return {}


def decline_booking(booking_id: int, db: Session, curr_user: User):
    db_booking = get_booking_by_id(booking_id, db)
    # get the listing from the db to verify the curr_user is the owner
    # of the listing
    db_listing = get_listing_by_id(db_booking.listing_id, db)
    if not listing_belongs_to_user(db_listing, curr_user):
        raise USER_NOT_OWNER_EXCEPTION

    db_booking.status = "declined"
    db.commit()
    return {}


def delete_booking(booking_id: int, db: Session, curr_user: User):
    db_booking = get_booking_by_id(booking_id, db)

    # get the listing from the db to verify the curr_user is the owner
    # of the listing
    db_listing = get_listing_by_id(db_booking.listing_id, db)
    if not listing_belongs_to_user(db_listing, curr_user):
        raise USER_NOT_OWNER_EXCEPTION

    db.delete(db_booking)
    db.commit()
    return {}
