
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.fitness import router as fitness_router
from routes.profile import router as profile_router
from routes.workout import router as workout_router
from routes.exercise import router as exercise_router
from routes.workout_result import router as workout_result_router
from routes.progress import router as progress_router
from routes.nutrition import router as nutrition_router
from routes.chatbot import router as chatbot_router
from routes.habit import router as habit_router
from routes.mood import router as mood_router
from routes.smart_gym import router as smart_gym_router
from routes.weekly_report import router as weekly_report_router

from database.database import engine, Base
from models.workout_result_db import WorkoutResultDB

app = FastAPI(
    title="AI Gym & Fitness Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "AI Gym & Fitness Assistant Backend is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(
    fitness_router,
    prefix="/fitness",
    tags=["Fitness"]
)

app.include_router(
    profile_router,
    prefix="/user",
    tags=["User Profile"]
)

app.include_router(
    workout_router,
    prefix="/workout",
    tags=["Workout"]
)

app.include_router(
    exercise_router,
    prefix="/exercise",
    tags=["Exercise"]
)

app.include_router(
    workout_result_router,
    prefix="/workout",
    tags=["Workout Result"]
)

app.include_router(
    progress_router,
    prefix="/progress",
    tags=["Progress Tracking"]
)

app.include_router(
    nutrition_router,
    prefix="/nutrition",
    tags=["Nutrition"]
)

app.include_router(
    chatbot_router,
    prefix="/chatbot",
    tags=["Chatbot"]
)

app.include_router(
    habit_router,
    prefix="/habit",
    tags=["Fitness Habit Tracker"]
)

app.include_router(
    mood_router,
    prefix="/mood",
    tags=["AI Mood & Sentiment"]
)

app.include_router(
    smart_gym_router,
    prefix="/smart-gym",
    tags=["Smart Gym Assistant"]
)

app.include_router(
    weekly_report_router,
    prefix="/report",
    tags=["Weekly Performance Report"]
)