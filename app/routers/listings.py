from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_all_listings():
    return {"message": "all listings"}


@router.post("/new")
async def create_listing():
    return {"message": "new listing"}


@router.get("/{listing_id}")
async def get_listing(listing_id: str):
    return {"message": f"listing {listing_id}"}


@router.put("/{listing_id}")
async def update_listing(listing_id: str):
    return {"message": f"update listing {listing_id}"}


@router.delete("/{listing_id}")
async def delete_listing(listing_id: str):
    return {"message": f"delete listing {listing_id}"}


@router.put("/publish/{listing_id}")
async def publish_listing(listing_id: str):
    return {"message": f"publish listing {listing_id}"}


@router.put("/unpublish/{listing_id}")
async def unpublish_listing(listing_id: str):
    return {"message": f"unpublish listing {listing_id}"}


@router.put("/publish/{listing_id}/review/{booking_id}")
async def review_listing(listing_id: str, booking_id: str):
    return {"message": f"review listing {listing_id} for booking {booking_id}"}
