from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.entities.base import Base
from app.entities.movie_producer import MovieProducer


class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    movies = relationship(
        "Movie",
        secondary=MovieProducer.__table__,
        back_populates="producers",
    )
