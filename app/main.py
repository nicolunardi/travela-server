from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, listings, bookings
from app.config.settings import origins
from app.config.database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/user/auth")
app.include_router(listings.router, prefix="/listings")
app.include_router(bookings.router, prefix="/bookings")
