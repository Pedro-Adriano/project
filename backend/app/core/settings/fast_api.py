from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.api.routers import api_router
from app.core.settings.settings import settings
from app.db.init_db import init_db
from app.startup import import_csv_on_startup


def create_app() -> FastAPI:
    fast_api = FastAPI(
        title="Movielist API",
        description="Movielist API",
        version="1.0.0",
        docs_url=f"{settings.PREFIX}/docs",
        openapi_url=f"{settings.PREFIX}/openapi.json",
    )

    @fast_api.on_event("startup")
    async def startup():
        init_db()
        await import_csv_on_startup()

    fast_api.include_router(
        api_router,
        prefix=settings.PREFIX,
    )

    add_pagination(fast_api)

    return fast_api
