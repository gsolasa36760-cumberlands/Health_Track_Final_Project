# Importing FastAPI components
from fastapi import APIRouter, Depends, HTTPException, status

# Importing SQLAlchemy session
from sqlalchemy.orm import Session

# Importing database session factory
from app.database import SessionLocal

# Importing database models
from app.models import RiskAssessment, Patient

# Importing Pydantic schemas
from app.schemas import RiskAssessmentCreate, RiskAssessmentResponse

# Importing database models
from app.models import RiskAssessment, Patient, VitalSign, Alert

# Importing the risk calculation service
from services.risk_service import calculate_risk

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
# RISK ASSESSMENT ROUTER
# =========================================================

# Creating the Risk Assessment API router
router = APIRouter(
    prefix="/risk",
    tags=["Risk Assessment"]
)


# =========================================================
# CREATE RISK ASSESSMENT
# =========================================================

# Creating a new risk assessment
@router.post(
    "",
    response_model=RiskAssessmentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_risk_assessment(
    assessment: RiskAssessmentCreate,
    db: Session = Depends(get_db)
):
    # Checking whether the patient exists
    patient = db.query(Patient).filter(
        Patient.patient_id == assessment.patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    # Creating a RiskAssessment database object
    new_assessment = RiskAssessment(
        patient_id=assessment.patient_id,
        risk_score=assessment.risk_score,
        risk_level=assessment.risk_level,
        assessment_method=assessment.assessment_method,
        explanation=assessment.explanation
    )

    # Adding the assessment to the database
    db.add(new_assessment)

    # Saving the database change
    db.commit()

    # Refreshing the object
    db.refresh(new_assessment)

    return new_assessment


# =========================================================
# GET ALL RISK ASSESSMENTS
# =========================================================

# Retrieving all risk assessments
@router.get(
    "",
    response_model=list[RiskAssessmentResponse]
)
def get_risk_assessments(
    db: Session = Depends(get_db)
):
    # Retrieving all risk assessments
    assessments = db.query(RiskAssessment).all()

    return assessments


# =========================================================
# GET RISK ASSESSMENTS FOR ONE PATIENT
# =========================================================

# Retrieving risk assessments for a specific patient
@router.get(
    "/patient/{patient_id}",
    response_model=list[RiskAssessmentResponse]
)
def get_patient_risk_assessments(
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

    # Retrieving assessments for the patient
    assessments = db.query(RiskAssessment).filter(
        RiskAssessment.patient_id == patient_id
    ).all()

    return assessments


# =========================================================
# GET ONE RISK ASSESSMENT
# =========================================================

# Retrieving a specific risk assessment
@router.get(
    "/{risk_id}",
    response_model=RiskAssessmentResponse
)
def get_risk_assessment(
    risk_id: int,
    db: Session = Depends(get_db)
):
    # Searching for the requested assessment
    assessment = db.query(RiskAssessment).filter(
        RiskAssessment.risk_id == risk_id
    ).first()

    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Risk assessment not found"
        )

    return assessment


# =========================================================
# DELETE RISK ASSESSMENT
# =========================================================

# Deleting a specific risk assessment
@router.delete(
    "/{risk_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_risk_assessment(
    risk_id: int,
    db: Session = Depends(get_db)
):
    # Searching for the assessment
    assessment = db.query(RiskAssessment).filter(
        RiskAssessment.risk_id == risk_id
    ).first()

    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Risk assessment not found"
        )

    # Deleting the assessment
    db.delete(assessment)

    # Saving the database change
    db.commit()

    return None

# =========================================================
# AUTOMATIC RISK CALCULATION
# =========================================================

# Calculating and storing risk from the patient's latest vital signs
@router.post(
    "/calculate/{patient_id}",
    response_model=RiskAssessmentResponse,
    status_code=status.HTTP_201_CREATED
)
def calculate_patient_risk(
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

    # Retrieving the patient's latest vital signs
    latest_vital = (
        db.query(VitalSign)
        .filter(VitalSign.patient_id == patient_id)
        .order_by(VitalSign.recorded_at.desc())
        .first()
    )

    # Checking whether vital signs are available
    if not latest_vital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No vital signs found for this patient"
        )

    # Calculating the patient's risk
    result = calculate_risk(
        heart_rate=latest_vital.heart_rate,
        oxygen_saturation=latest_vital.oxygen_saturation,
        temperature=latest_vital.temperature,
        systolic_bp=latest_vital.systolic_bp,
        diastolic_bp=latest_vital.diastolic_bp,
        respiratory_rate=latest_vital.respiratory_rate
    )

    # Creating a new risk assessment
    new_assessment = RiskAssessment(
        patient_id=patient_id,
        risk_score=result["risk_score"],
        risk_level=result["risk_level"],
        assessment_method="HealthTrack Risk Model",
        explanation=result["explanation"]
    )

    # Saving the risk assessment
    db.add(new_assessment)

    # Creating an automatic alert for high risk
    if result["risk_level"] == "High":

        # Creating a high-risk alert
        new_alert = Alert(
            patient_id=patient_id,
            alert_type="High Health Risk",
            severity="High",
            message=result["explanation"],
            status="Active"
        )

        # Adding the alert to the database
        db.add(new_alert)

    # Saving all database changes
    db.commit()

    # Refreshing the risk assessment
    db.refresh(new_assessment)

    return new_assessment