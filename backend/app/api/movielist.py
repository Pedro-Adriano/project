from fastapi import APIRouter, Depends, File, UploadFile, status
from sqlalchemy.orm import Session

from app.core.database import Database
from app.repositories.movielist import AwardsRepository
from app.schemas.movielist_schema import AwardIntervalResponseSchema
from app.services.movielist import AwardsService

router = APIRouter()


@router.post("/import", status_code=status.HTTP_201_CREATED)
async def import_csv_movielist(
    file: UploadFile = File(...), db: Session = Depends(Database.get_db)
) -> dict:

    service = AwardsService(
        repository=AwardsRepository(session=db),
    )

    return await service.import_csv_movielist(file)


@router.get("/intervals", response_model=AwardIntervalResponseSchema)
def get_awards_intervals(db: Session = Depends(Database.get_db)):

    service = AwardsService(
        repository=AwardsRepository(session=db),
    )

    return service.get_intervals()
