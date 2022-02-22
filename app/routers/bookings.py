from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def get_all_bookings():
    return {"message": "all bookings"}


@router.post("/new/{listing_id}")
async def create_booking(listing_id):
    return {"message": f"Booking for listing {listing_id}"}


@router.put("/accept/{booking_id}")
async def accept_booking(booking_id):
    return {"message": f"accepting booking {booking_id}"}


@router.put("/decline/{booking_id}")
async def decline_booking(booking_id):
    return {"message": f"decline booking {booking_id}"}


@router.delete("/{booking_id}")
async def delete_booking(booking_id):
    return {"message": f"delete booking {booking_id}"}
