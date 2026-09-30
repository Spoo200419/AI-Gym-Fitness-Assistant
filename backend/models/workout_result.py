from pydantic import BaseModel


class WorkoutResult(BaseModel):
    exercise: str
    target_reps: int
    completed_reps: int
    form_feedback: str
    duration_minutes: float