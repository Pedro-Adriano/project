from io import BytesIO

from fastapi import UploadFile

from app.core.database import Database
from app.repositories.movielist import AwardsRepository
from app.services.movielist import AwardsService


async def import_csv_on_startup() -> None:

    with Database.get_session() as session:
        service = AwardsService(repository=AwardsRepository(session))

        with open("data/Movielist.csv", "rb") as file:
            content = file.read()

        formatted_file = UploadFile(filename="Movielist.csv", file=BytesIO(content))

        await service.import_csv_movielist(formatted_file)
