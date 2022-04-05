from fastapi import HTTPException, status


CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials.",
    headers={"WWW-Authenticate": "Bearer"},
)

# DATABASE ERRORS

LISTING_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No listing found with that id.",
)

BOOKING_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No booking found with that id.",
)

USER_NOT_OWNER_EXCEPTION = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="You do not have permission to modify this listing.",
)

BOOKING_WITH_LISTING_AND_USER_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No booking found for this listing with the given user id",
)
