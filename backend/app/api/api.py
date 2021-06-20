from fastapi import APIRouter

from app.api.endpoints import demo

api_router = APIRouter()

api_router.include_router(demo.router, prefix="/demo", tags=["demo"])