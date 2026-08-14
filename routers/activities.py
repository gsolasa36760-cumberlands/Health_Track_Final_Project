# Importing FastAPI components
from fastapi import APIRouter, Depends, HTTPException, status

# Importing SQLAlchemy session
from sqlalchemy.orm import Session

# Importing database session factory
from app.database import SessionLocal

# Importing database models
from app.models import Activity, Patient

# Importing Pydantic schemas
from app.schemas import ActivityCreate, ActivityResponse


# =========================================================
# DATABASE DEPENDENCY
# =========================================================

# Creating a database session for each API request
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# =========================================================
# ACTIVITIES ROUTER
# =========================================================

# Creating the Activities API router
router = APIRouter(
    prefix="/activities",
    tags=["Activities"]
)


# =========================================================
# CREATE ACTIVITY
# =========================================================

# Creating a new activity record
@router.post(
    "",
    response_model=ActivityResponse,
    status_code=status.HTTP_201_CREATED
)
def create_activity(
    activity: ActivityCreate,
    db: Session = Depends(get_db)
):
    # Checking whether the patient exists
    patient = db.query(Patient).filter(
        Patient.patient_id == activity.patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    # Creating an Activity database object
    new_activity = Activity(
        patient_id=activity.patient_id,
        activity_type=activity.activity_type,
        duration_minutes=activity.duration_minutes,
        calories_burned=activity.calories_burned
    )

    # Adding the activity to the database
    db.add(new_activity)

    # Saving the database change
    db.commit()

    # Refreshing the object
    db.refresh(new_activity)

    return new_activity


# =========================================================
# GET ALL ACTIVITIES
# =========================================================

# Retrieving all activity records
@router.get(
    "",
    response_model=list[ActivityResponse]
)
def get_activities(
    db: Session = Depends(get_db)
):
    # Retrieving all activities
    activities = db.query(Activity).all()

    return activities


# =========================================================
# GET ACTIVITIES FOR ONE PATIENT
# =========================================================

# Retrieving activities for a specific patient
@router.get(
    "/patient/{patient_id}",
    response_model=list[ActivityResponse]
)
def get_patient_activities(
    patient_id: int,
    db: Session = Depends(get_db)
):
    # Checking whether the patient exists
    patient = db.query(Patient).filter(
        Patient.patient_id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    # Retrieving activities for the patient
    activities = db.query(Activity).filter(
        Activity.patient_id == patient_id
    ).all()

    return activities


# =========================================================
# GET ONE ACTIVITY
# =========================================================

# Retrieving a specific activity
@router.get(
    "/{activity_id}",
    response_model=ActivityResponse
)
def get_activity(
    activity_id: int,
    db: Session = Depends(get_db)
):
    # Searching for the requested activity
    activity = db.query(Activity).filter(
        Activity.activity_id == activity_id
    ).first()

    if not activity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Activity not found"
        )

    return activity


# =========================================================
# DELETE ACTIVITY
# =========================================================

# Deleting a specific activity
@router.delete(
    "/{activity_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_activity(
    activity_id: int,
    db: Session = Depends(get_db)
):
    # Searching for the activity
    activity = db.query(Activity).filter(
        Activity.activity_id == activity_id
    ).first()

    if not activity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Activity not found"
        )

    # Deleting the activity
    db.delete(activity)

    # Saving the database change
    db.commit()

    return None