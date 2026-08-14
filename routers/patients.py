"""
HealthTrack Patient API

This file is defining patient-related API endpoints for creating,
reading, updating, and deleting patient information.
"""

# Importing FastAPI components
from fastapi import APIRouter, Depends, HTTPException, status

# Importing SQLAlchemy session components
from sqlalchemy.orm import Session

# Importing HealthTrack database dependency
from app.database import SessionLocal

# Importing HealthTrack database models
from app.models import Patient

# Importing HealthTrack Pydantic schemas
from app.schemas import (
    PatientCreate,
    PatientResponse,
    PatientUpdate
)


# =========================================================
# DATABASE DEPENDENCY
# =========================================================

def get_db():
    """
    Providing a database session for each API request.
    """

    # Creating a database session
    db = SessionLocal()

    try:
        # Providing the database session to the endpoint
        yield db

    finally:
        # Closing the database session
        db.close()


# =========================================================
# PATIENT ROUTER
# =========================================================

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


# =========================================================
# CREATE PATIENT
# =========================================================

@router.post(
    "",
    response_model=PatientResponse,
    status_code=status.HTTP_201_CREATED
)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    """
    Creating a new patient record.
    """

    # Creating a SQLAlchemy patient object
    new_patient = Patient(
        first_name=patient.first_name,
        last_name=patient.last_name,
        date_of_birth=patient.date_of_birth,
        gender=patient.gender,
        phone=patient.phone,
        email=patient.email,
        emergency_contact=patient.emergency_contact
    )

    # Adding the patient to the database session
    db.add(new_patient)

    # Saving the patient to the database
    db.commit()

    # Refreshing the object to obtain the generated ID
    db.refresh(new_patient)

    # Returning the newly created patient
    return new_patient


# =========================================================
# GET ALL PATIENTS
# =========================================================

@router.get(
    "",
    response_model=list[PatientResponse]
)
def get_patients(
    db: Session = Depends(get_db)
):
    """
    Returning all patient records.
    """

    # Querying all patients
    patients = (
        db.query(Patient)
        .order_by(Patient.patient_id)
        .all()
    )

    # Returning the patient list
    return patients


# =========================================================
# GET PATIENT BY ID
# =========================================================

@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    """
    Returning one patient by patient ID.
    """

    # Searching for the requested patient
    patient = (
        db.query(Patient)
        .filter(Patient.patient_id == patient_id)
        .first()
    )

    # Checking whether the patient exists
    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    # Returning the requested patient
    return patient


# =========================================================
# UPDATE PATIENT
# =========================================================

@router.put(
    "/{patient_id}",
    response_model=PatientResponse
)
def update_patient(
    patient_id: int,
    patient_data: PatientUpdate,
    db: Session = Depends(get_db)
):
    """
    Updating an existing patient record.
    """

    # Searching for the requested patient
    patient = (
        db.query(Patient)
        .filter(Patient.patient_id == patient_id)
        .first()
    )

    # Checking whether the patient exists
    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    # Converting provided fields into a dictionary
    update_data = patient_data.model_dump(
        exclude_unset=True
    )

    # Updating each supplied patient field
    for field, value in update_data.items():
        setattr(patient, field, value)

    # Saving the updated patient
    db.commit()

    # Refreshing the patient object
    db.refresh(patient)

    # Returning the updated patient
    return patient


# =========================================================
# DELETE PATIENT
# =========================================================

@router.delete(
    "/{patient_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    """
    Deleting an existing patient record.
    """

    # Searching for the requested patient
    patient = (
        db.query(Patient)
        .filter(Patient.patient_id == patient_id)
        .first()
    )

    # Checking whether the patient exists
    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    # Deleting the patient
    db.delete(patient)

    # Saving the deletion
    db.commit()

    # Returning no response body
    return None