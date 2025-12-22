from typing import List

from pydantic import BaseModel


class ProducerSchema(BaseModel):
    name: str


class MovieImportSchema(BaseModel):
    year: int
    title: str
    studios: str | None
    winner: bool
    producers: List[ProducerSchema]


class AwardIntervalSchema(BaseModel):
    producer: str
    interval: int
    previousWin: int
    followingWin: int


class AwardIntervalResponseSchema(BaseModel):
    min: List[AwardIntervalSchema]
    max: List[AwardIntervalSchema]
