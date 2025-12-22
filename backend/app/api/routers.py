from fastapi import APIRouter

from app.api.movielist import router as movielist_router

api_router = APIRouter()
api_router.include_router(movielist_router, tags=["movielist"])
