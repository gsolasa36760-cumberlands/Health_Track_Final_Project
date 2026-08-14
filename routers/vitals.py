# Importing FastAPI components
from fastapi import APIRouter, Depends, HTTPException, status

# Importing SQLAlchemy session
from sqlalchemy.orm import Session

# Importing database session factory
from app.database import SessionLocal

# Importing database models
from app.models import VitalSign, Patient

# Importing Pydantic schemas
from app.schemas import VitalSignCreate, VitalSignResponse


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
# VITAL SIGNS ROUTER
# =========================================================

# Creating the Vital Signs API router
router = APIRouter(
    prefix="/vitals",
    tags=["Vital Signs"]
)


# =========================================================
# CREATE VITAL SIGN
# =========================================================

# Creating a new vital-sign record
@router.post(
    "",
    response_model=VitalSignResponse,
    status_code=status.HTTP_201_CREATED
)
def create_vital(
    vital: VitalSignCreate,
    db: Session = Depends(get_db)
):
    # Checking whether the patient exists
    patient = db.query(Patient).filter(
        Patient.patient_id == vital.patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    # Creating a VitalSign database object
    new_vital = VitalSign(
        patient_id=vital.patient_id,
        heart_rate=vital.heart_rate,
        oxygen_saturation=vital.oxygen_saturation,
        temperature=vital.temperature,
        systolic_bp=vital.systolic_bp,
        diastolic_bp=vital.diastolic_bp,
        respiratory_rate=vital.respiratory_rate
    )

    # Adding the vital-sign record to the database
    db.add(new_vital)

    # Saving the record
    db.commit()

    # Refreshing the object to obtain generated values
    db.refresh(new_vital)

    return new_vital


# =========================================================
# GET ALL VITAL SIGNS
# =========================================================

# Retrieving all vital-sign records
@router.get(
    "",
    response_model=list[VitalSignResponse]
)
def get_vitals(
    db: Session = Depends(get_db)
):
    # Retrieving vital-sign records from the database
    vitals = db.query(VitalSign).all()

    return vitals


# =========================================================
# GET VITAL SIGNS FOR ONE PATIENT
# =========================================================

# Retrieving vital-sign records for a specific patient
@router.get(
    "/patient/{patient_id}",
    response_model=list[VitalSignResponse]
)
def get_patient_vitals(
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

    # Retrieving vital-sign records for the patient
    vitals = db.query(VitalSign).filter(
        VitalSign.patient_id == patient_id
    ).all()

    return vitals


# =========================================================
# GET ONE VITAL-SIGN RECORD
# =========================================================

# Retrieving a specific vital-sign record
@router.get(
    "/{vital_id}",
    response_model=VitalSignResponse
)
def get_vital(
    vital_id: int,
    db: Session = Depends(get_db)
):
    # Searching for the requested vital-sign record
    vital = db.query(VitalSign).filter(
        VitalSign.vital_id == vital_id
    ).first()

    if not vital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vital-sign record not found"
        )

    return vital


# =========================================================
# DELETE VITAL-SIGN RECORD
# =========================================================

# Deleting a specific vital-sign record
@router.delete(
    "/{vital_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_vital(
    vital_id: int,
    db: Session = Depends(get_db)
):
    # Searching for the vital-sign record
    vital = db.query(VitalSign).filter(
        VitalSign.vital_id == vital_id
    ).first()

    if not vital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vital-sign record not found"
        )

    # Deleting the vital-sign record
    db.delete(vital)

    # Saving the database change
    db.commit()

    return None