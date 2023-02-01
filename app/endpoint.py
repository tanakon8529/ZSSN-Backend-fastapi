from fastapi import APIRouter
from app.routes import access, zssn

api_router = APIRouter()

api_router.include_router(
    access.router, 
    prefix="/access", 
    tags=["access"]
)

api_router.include_router(
    zssn.router, 
    prefix="/zssn", 
    tags=["zssn"]
)
