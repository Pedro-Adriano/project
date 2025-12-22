from sqlalchemy import Column, ForeignKey, Integer

from app.entities.base import Base


class MovieProducer(Base):
    __tablename__ = "movie_producers"

    movie_id = Column(
        Integer,
        ForeignKey("movies.id", ondelete="CASCADE"),
        primary_key=True,
    )
    producer_id = Column(
        Integer,
        ForeignKey("producers.id", ondelete="CASCADE"),
        primary_key=True,
    )
