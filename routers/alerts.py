# Importing FastAPI components
from fastapi import APIRouter, Depends, HTTPException, status

# Importing SQLAlchemy session
from sqlalchemy.orm import Session

# Importing database session factory
from app.database import SessionLocal

# Importing database models
from app.models import Alert, Patient

# Importing Pydantic schemas
from app.schemas import AlertCreate, AlertResponse


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
# ALERTS ROUTER
# =========================================================

# Creating the Alerts API router
router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)


# =========================================================
# CREATE ALERT
# =========================================================

# Creating a new alert
@router.post(
    "",
    response_model=AlertResponse,
    status_code=status.HTTP_201_CREATED
)
def create_alert(
    alert: AlertCreate,
    db: Session = Depends(get_db)
):
    # Checking whether the patient exists
    patient = db.query(Patient).filter(
        Patient.patient_id == alert.patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    # Creating an Alert database object
    new_alert = Alert(
        patient_id=alert.patient_id,
        alert_type=alert.alert_type,
        severity=alert.severity,
        message=alert.message,
        status=alert.status
    )

    # Adding the alert to the database
    db.add(new_alert)

    # Saving the database change
    db.commit()

    # Refreshing the object
    db.refresh(new_alert)

    return new_alert


# =========================================================
# GET ALL ALERTS
# =========================================================

# Retrieving all alerts
@router.get(
    "",
    response_model=list[AlertResponse]
)
def get_alerts(
    db: Session = Depends(get_db)
):
    # Retrieving all alerts from the database
    alerts = db.query(Alert).all()

    return alerts


# =========================================================
# GET ALERTS FOR ONE PATIENT
# =========================================================

# Retrieving alerts for a specific patient
@router.get(
    "/patient/{patient_id}",
    response_model=list[AlertResponse]
)
def get_patient_alerts(
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

    # Retrieving alerts for the patient
    alerts = db.query(Alert).filter(
        Alert.patient_id == patient_id
    ).all()

    return alerts


# =========================================================
# GET ONE ALERT
# =========================================================

# Retrieving a specific alert
@router.get(
    "/{alert_id}",
    response_model=AlertResponse
)
def get_alert(
    alert_id: int,
    db: Session = Depends(get_db)
):
    # Searching for the requested alert
    alert = db.query(Alert).filter(
        Alert.alert_id == alert_id
    ).first()

    if not alert:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found"
        )

    return alert


# =========================================================
# UPDATE ALERT STATUS
# =========================================================

# Updating the status of an alert
@router.put(
    "/{alert_id}",
    response_model=AlertResponse
)
def update_alert(
    alert_id: int,
    alert_update: AlertCreate,
    db: Session = Depends(get_db)
):
    # Searching for the alert
    alert = db.query(Alert).filter(
        Alert.alert_id == alert_id
    ).first()

    if not alert:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found"
        )

    # Updating alert information
    alert.alert_type = alert_update.alert_type
    alert.severity = alert_update.severity
    alert.message = alert_update.message
    alert.status = alert_update.status

    # Saving the changes
    db.commit()

    # Refreshing the alert
    db.refresh(alert)

    return alert


# =========================================================
# DELETE ALERT
# =========================================================

# Deleting an alert
@router.delete(
    "/{alert_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_alert(
    alert_id: int,
    db: Session = Depends(get_db)
):
    # Searching for the alert
    alert = db.query(Alert).filter(
        Alert.alert_id == alert_id
    ).first()

    if not alert:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found"
        )

    # Deleting the alert
    db.delete(alert)

    # Saving the database change
    db.commit()

    return None