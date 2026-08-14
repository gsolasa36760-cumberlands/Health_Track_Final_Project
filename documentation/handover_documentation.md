# HealthTrack Handover Documentation

## 1. Project Overview

HealthTrack is a healthcare monitoring system designed to manage patient information, vital signs, activities, alerts, and health-risk assessments.

The system consists of:

- MySQL database
- SQLAlchemy ORM
- FastAPI backend
- Pydantic validation
- Risk assessment service
- Alert management
- Dash dashboard
- Alembic database migrations
- Pytest automated testing

---

## 2. Main System Functions

The HealthTrack system provides the following functions:

1. Managing patient information.
2. Recording patient vital signs.
3. Recording patient activities.
4. Calculating health-risk assessments.
5. Managing patient alerts.
6. Retrieving patient health information.
7. Displaying health information through the Dash dashboard.
8. Validating application data.
9. Managing database schema changes through Alembic.

---

## 3. System Components

| Component | Location |
|---|---|
| FastAPI application | `app/main.py` |
| Database configuration | `app/database.py` |
| Database models | `app/models.py` |
| Validation schemas | `app/schemas.py` |
| Risk services | `app/services/` |
| Dashboard | `dashboard/dashboard.py` |
| Database migrations | `migrations/` |
| Automated tests | `tests/` |
| Documentation | `documentation/` |

---

## 4. Running the System

### Start the FastAPI Backend

Activate the virtual environment:

```text
venv\Scripts\activate