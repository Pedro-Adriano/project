from typing import Dict, List

from sqlalchemy.orm import Session

from app.entities.movie import Movie
from app.entities.producer import Producer
from app.schemas.movielist_schema import MovieImportSchema


class AwardsRepository:

    def __init__(self, session: Session):
        self.session = session

    def insert_movies(self, movies_dto: List[MovieImportSchema]) -> None:

        producers_cache: Dict[str, Producer] = {
            producer.name: producer for producer in self.session.query(Producer).all()
        }

        for movie_dto in movies_dto:
            movie = Movie(
                year=movie_dto.year,
                title=movie_dto.title,
                studios=movie_dto.studios,
                winner=movie_dto.winner,
            )

            for producer_dto in movie_dto.producers:
                name = producer_dto.name.strip()
                if not name:
                    continue

                producer = producers_cache.get(name)
                if not producer:
                    producer = Producer(name=name)
                    self.session.add(producer)
                    producers_cache[name] = producer

                movie.producers.append(producer)

            self.session.add(movie)

    def get_winner_movies(self):
        return self.session.query(Movie).filter(Movie.winner.is_(True)).all()
