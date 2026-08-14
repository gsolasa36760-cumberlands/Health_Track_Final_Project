"""
HealthTrack FastAPI Application

This file is creating the main FastAPI application for the
HealthTrack health monitoring system. The application is providing
the initial API endpoints and database connectivity required for
the remaining HealthTrack backend services.
"""

# Importing FastAPI components
from fastapi import FastAPI

# Importing the database engine
from app.database import engine

# Importing SQLAlchemy metadata
from app.database import Base

# Importing the patient API router
from routers import patients

# Importing the vital-sign API router
from routers import vitals

# Importing the activity API router
from routers import activities

# Importing the alerts API router
from routers import alerts

# Importing the risk assessment API router
from routers import risk

from app.websocket import router as websocket_router

# =========================================================
# FASTAPI APPLICATION
# =========================================================

# Creating the FastAPI application
app = FastAPI(
    title="HealthTrack API",
    description=(
        "HealthTrack health monitoring and risk assessment "
        "backend API."
    ),
    version="1.0.0"
)

# Registering the patient API router
app.include_router(patients.router)

# Registering the vital-sign API router
app.include_router(vitals.router)

# Registering the activity API router
app.include_router(activities.router)

# Registering the alerts API router
app.include_router(alerts.router)

# Registering the risk assessment API router
app.include_router(risk.router)

app.include_router(websocket_router)

# =========================================================
# ROOT ENDPOINT
# =========================================================

@app.get("/")
def root():
    """
    Providing the HealthTrack API welcome response.
    """

    # Returning the API status
    return {
        "application": "HealthTrack",
        "status": "running",
        "version": "1.0.0"
    }


# =========================================================
# HEALTH CHECK ENDPOINT
# =========================================================

@app.get("/health")
def health_check():
    """
    Providing a basic system health check.
    """

    # Returning the system health status
    return {
        "status": "healthy",
        "service": "HealthTrack API"
    }