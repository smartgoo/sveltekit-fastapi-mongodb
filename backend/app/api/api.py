from fastapi import APIRouter

from app.api.endpoints import demo
from app.api.endpoints import user

api_router = APIRouter()

api_router.include_router(demo.router, prefix="/demo", tags=["demo"])
api_router.include_router(user.router, prefix="/users", tags=["user"])