from datetime import date
from pydantic import BaseModel


class Availability(BaseModel):
    start: date
    end: date


class AvailabilityIn(BaseModel):
    availability: list[Availability]
