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

USER_NOT_OWNER_EXCEPTION = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="You do not have permission to modify this listing.",
)
