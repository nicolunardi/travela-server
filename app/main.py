from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, listings, bookings
from config.settings import origins

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(listings.router, prefix="/listings")
app.include_router(bookings.router, prefix="/bookings")
