from fastapi import APIRouter


router = APIRouter()


@router.post("/register")
async def register():
    return {"message": "registered"}


@router.post("/login")
async def login():
    return {"message": "login"}


@router.post("/logout")
async def logout():
    return {"message": "logged out"}
