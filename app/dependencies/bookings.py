from sqlalchemy.orm import Session
from errors.exceptions import BOOKING_NOT_FOUND_EXCEPTION
from models.bookings import Booking


def get_booking_by_id(booking_id: int, db: Session):
    db_booking: Booking = (
        db.query(Booking).filter(Booking.id == booking_id).first()
    )
    if not db_booking:
        raise BOOKING_NOT_FOUND_EXCEPTION

    return db_booking
