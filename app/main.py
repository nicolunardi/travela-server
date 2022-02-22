from fastapi import FastAPI
from .routers import auth, listings, bookings

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(listings.router, prefix="/listings")
app.include_router(bookings.router, prefix="/bookings")
