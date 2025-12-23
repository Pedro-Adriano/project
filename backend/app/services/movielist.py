import csv
from collections import defaultdict
from io import StringIO
from itertools import groupby
from typing import Dict, List

from fastapi import HTTPException, UploadFile

from app.schemas.movielist_schema import MovieImportSchema, ProducerSchema


class AwardsService:
    def __init__(self, repository):
        self.repository = repository

    async def import_csv_movielist(self, file: UploadFile) -> List[MovieImportSchema]:

        content = await file.read()
        csv_file = StringIO(content.decode("utf-8"))
        reader = csv.DictReader(csv_file, delimiter=";")

        if self.validate_required_fields(reader.fieldnames):
            raise HTTPException(
                status_code=400,
                detail="Arquivo CSV inválido. Campos obrigatórios estão faltando.",
            )

        movies: List[MovieImportSchema] = []

        for row in reader:
            producers = [
                ProducerSchema(name=name.strip())
                for name in row["producers"].replace(" and ", ",").split(",")
            ]

            movies.append(
                MovieImportSchema(
                    year=int(row["year"]),
                    title=row["title"],
                    studios=row.get("studios"),
                    winner=row["winner"].lower() == "yes",
                    producers=producers,
                )
            )

        self.repository.insert_movies(movies)

        return {"movies_imported": len(movies)}

    def validate_required_fields(self, fieldnames: List[str]) -> bool:
        required_fields = ["year", "title", "studios", "producers", "winner"]

        return bool([field for field in required_fields if field not in fieldnames])

    def get_intervals(self):

        producer_wins = defaultdict(list)

        for movie in self.repository.get_winner_movies():
            for producer in movie.producers:
                producer_wins[producer.name].append(movie.year)

        intervals = []

        for producer, years in producer_wins.items():

            years.sort()
            for item in range(1, len(years)):
                intervals.append(
                    {
                        "producer": producer,
                        "interval": years[item] - years[item - 1],
                        "previousWin": years[item - 1],
                        "followingWin": years[item],
                    }
                )

        return self._split_min_max_intervals(intervals)

    def _split_min_max_intervals(
        self,
        intervals: List[Dict],
    ) -> Dict[str, List[Dict]]:

        if not intervals:
            return {"min": [], "max": []}

        intervals.sort(key=lambda x: x["interval"])

        grouped = {
            k: list(g) for k, g in groupby(intervals, key=lambda x: x["interval"])
        }

        min_interval = min(grouped)
        max_interval = max(grouped)

        return {
            "min": grouped[min_interval],
            "max": grouped[max_interval],
        }
