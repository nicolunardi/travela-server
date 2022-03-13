from sqlalchemy.orm import Session
from models.bedroom import Bedroom


def create_beds(beds: list[int], db: Session, listing_id: int):
    for bed in beds:
        new_bed = Bedroom(listin_id=listing_id, beds=beds)
        db.add(new_bed)
        db.commit()
        db.refresh(new_bed)
