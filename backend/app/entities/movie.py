from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.entities.base import Base
from app.entities.movie_producer import MovieProducer


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    studios = Column(String, nullable=True)
    winner = Column(Boolean, nullable=False, default=False)

    producers = relationship(
        "Producer",
        secondary=MovieProducer.__table__,
        back_populates="movies",
    )
