from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from database.database import Base


class WorkoutResultDB(Base):

    __tablename__ = "workout_results"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    exercise = Column(
        String,
        nullable=False
    )

    target_reps = Column(
        Integer,
        nullable=False
    )

    completed_reps = Column(
        Integer,
        nullable=False
    )

    form_feedback = Column(
        String,
        nullable=False
    )

    duration_minutes = Column(
        Float,
        nullable=False
    )

    workout_date = Column(
        DateTime,
        default=datetime.utcnow
    )