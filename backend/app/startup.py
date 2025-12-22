from app.core.database import Database
from app.repositories.movielist import AwardsRepository
from app.services.movielist import AwardsService


def import_csv_on_startup() -> None:
    with Database.get_session() as session:

        service = AwardsService(
            repository=AwardsRepository(session),
        )

        service.import_csv_movielist("data/movielist.csv")
