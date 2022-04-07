from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.JWTtokens import get_current_user
from app.schemas.bookings import (
    BookingOut,
    CreateBookingOut,
    CreateBookingIn,
    AcceptDeclineBookingOut,
)
from app.models.bookings import Booking as BookingModel
from app.config.database import get_db
from app.controllers import bookingsControllers


router = APIRouter()


@router.get("/", tags=["Bookings"], response_model=BookingOut)
async def get_all_bookings(
    db: Session = Depends(get_db), user=Depends(get_current_user)
):
    return bookingsControllers.get_bookings(db)


@router.post(
    "/new/{listing_id}", tags=["Bookings"], response_model=CreateBookingOut
)
async def create_booking(
    listing_id: int,
    data: CreateBookingIn,
    db: Session = Depends(get_db),
    curr_user=Depends(get_current_user),
):
    return bookingsControllers.create_booking(listing_id, data, db, curr_user)


@router.put(
    "/accept/{booking_id}",
    tags=["Bookings"],
    response_model=AcceptDeclineBookingOut,
)
async def accept_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    curr_user=Depends(get_current_user),
):
    return bookingsControllers.accept_booking(booking_id, db, curr_user)


@router.put(
    "/decline/{booking_id}",
    tags=["Bookings"],
    response_model=AcceptDeclineBookingOut,
)
async def decline_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    curr_user=Depends(get_current_user),
):
    return bookingsControllers.decline_booking(booking_id, db, curr_user)


@router.delete(
    "/{booking_id}",
    tags=["Bookings"],
    response_model=AcceptDeclineBookingOut,
)
async def delete_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    curr_user=Depends(get_current_user),
):
    return bookingsControllers.delete_booking(booking_id, db, curr_user)
