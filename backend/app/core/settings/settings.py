from functools import lru_cache

from decouple import config


class Settings:
    PRODUCTION: bool = config("PRODUCTION", default=False, cast=bool)
    DEBUG: bool = config("DEBUG", default=False, cast=bool)
    SERVICE_NAME: str = config("SERVICE_NAME", default="movielist")
    PREFIX: str = config("PREFIX", default=f"/{SERVICE_NAME}/v1")
    POSTGRES_URI: str = config(
        "POSTGRES_URI",
        default="postgresql+psycopg2://project:project@db:5432/project",
    )
    POOL_SIZE: int = config("POOL_SIZE", default=5, cast=int)
    MAX_OVERFLOW: int = config("MAX_OVERFLOW", default=10, cast=int)
    POOL_RECYCLE: int = config("POOL_RECYCLE", default=30, cast=int)


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
