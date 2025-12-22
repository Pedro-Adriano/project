from app.core.database import Database
from app.entities.base import Base


def init_db():
    engine = Database.get_engine()
    Base.metadata.create_all(bind=engine)
