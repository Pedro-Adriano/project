from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.settings.settings import settings


def get_engine():
    return create_engine(
        settings.POSTGRES_URI,
        pool_pre_ping=True,
    )


class Database:
    _engine = None
    _SessionLocal = None

    @classmethod
    def get_engine(cls):
        if cls._engine is None:
            cls._engine = get_engine()
        return cls._engine

    @classmethod
    def get_sessionmaker(cls):
        if cls._SessionLocal is None:
            cls._SessionLocal = sessionmaker(
                bind=cls.get_engine(),
                autocommit=False,
                autoflush=False,
                expire_on_commit=False,
            )
        return cls._SessionLocal

    @classmethod
    @contextmanager
    def get_session(cls) -> Generator[Session, None, None]:
        session = cls.get_sessionmaker()()

        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def get_db() -> Generator[Session, None, None]:
        with Database.get_session() as session:
            yield session
