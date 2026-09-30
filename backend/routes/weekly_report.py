from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from services.weekly_report_service import get_weekly_report

router = APIRouter()

@router.get("/weekly")
def weekly_report(db: Session = Depends(get_db)):
    report = get_weekly_report(db)

    return {
        "message": "Weekly fitness report generated successfully.",
        "weekly_report": report
    }
