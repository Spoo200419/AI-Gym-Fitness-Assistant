# AI Gym & Fitness Assistant

An AI-powered fitness application that helps users manage workouts, track exercise performance, monitor fitness progress, and receive personalized fitness recommendations through a modern web interface.

## Overview

The AI Gym & Fitness Assistant combines a Python FastAPI backend with a React-based frontend to provide a centralized fitness experience.

The application supports user fitness profiling, BMI calculation, workout recommendations, exercise tracking, nutrition recommendations, habit and mood tracking, progress monitoring, weekly reports, and an AI fitness assistant.

## Key Features

- 👤 **User Fitness Profile**
  - Stores user information such as age, gender, height, weight, fitness goal, and experience level.
  - Generates a fitness profile based on user inputs.

- ⚖️ **BMI Analysis**
  - Calculates Body Mass Index (BMI).
  - Provides a basic BMI category such as Normal Weight.

- 🏋️ **Workout Recommendations**
  - Generates workout plans based on fitness goals and experience level.
  - Provides exercises with sets and repetitions.

- 🤖 **AI Exercise Trainer**
  - Provides exercise-tracking workflows for supported exercises.
  - Tracks completed repetitions and workout duration.
  - Generates basic workout form feedback.

- 📊 **Progress Tracking**
  - Records workout results.
  - Provides workout history and progress summaries.
  - Displays weekly activity and performance information.

- 🥗 **Nutrition Recommendations**
  - Provides fitness-oriented nutrition recommendations.
  - Displays recommended daily calorie information.

- 💬 **AI Fitness Assistant**
  - Provides an interactive assistant for fitness-related questions.
  - Supports questions related to workouts, nutrition, habits, and progress.

- 📅 **Habit & Mood Tracking**
  - Provides habit summaries.
  - Supports mood analysis workflows.

- 📄 **Weekly Reports**
  - Generates a summary of fitness activity and progress.

## Technology Stack

### Backend

- Python
- FastAPI
- REST APIs
- NumPy
- OpenCV
- TensorFlow / Keras
- SQLite
- Pydantic

### Frontend

- React
- JavaScript
- JSX
- CSS
- Vite

### Development Tools

- Visual Studio Code
- Git
- GitHub
- Postman

## System Architecture

```text
                    ┌──────────────────────────┐
                    │     React Frontend       │
                    │       Vite + JSX         │
                    └────────────┬─────────────┘
                                 │
                                 │ REST API
                                 ▼
                    ┌──────────────────────────┐
                    │     FastAPI Backend      │
                    │        Python            │
                    └────────────┬─────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
        Fitness Services   Workout Services   AI Services
              │                  │                  │
              └──────────────────┼──────────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │        SQLite DB         │
                    │     User & Workout Data  │
                    └──────────────────────────┘
                    ## Screenshots

### Dashboard

![AI Gym & Fitness Assistant Dashboard](screenshots/dashboard.png)

### Dashboard - Alternate View

![AI Gym & Fitness Assistant Dashboard](screenshots/dashboard1.png)