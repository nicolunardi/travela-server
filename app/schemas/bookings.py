from datetime import date
from pydantic import BaseModel


class DateRange(BaseModel):
    start: date
    end: date


class Booking(BaseModel):
    id: int
    start: date
    end: date
    total: int
    listing_id: int
    owner_id: int
    status: str


class CreateBookingIn(BaseModel):
    date_range: DateRange
    total: int


class CreateBookingOut(BaseModel):
    id: int


class BookingOut(BaseModel):
    bookings: list[Booking]


class AcceptDeclineBookingOut(BaseModel):
    pass
