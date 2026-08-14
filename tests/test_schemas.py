# Testing the HealthTrack Pydantic schemas

from datetime import date

from app.schemas import (
    PatientCreate,
    VitalSignCreate,
    ActivityCreate,
    AlertCreate,
    RiskAssessmentCreate
)


# =========================================================
# TEST PATIENT SCHEMA
# =========================================================

def test_patient_schema():

    # Creating a sample patient
    patient = PatientCreate(
        first_name="Test",
        last_name="Patient",
        date_of_birth=date(1990, 1, 1),
        gender="Male",
        phone="555-0000",
        email="test@example.com",
        emergency_contact="Emergency Contact"
    )

    # Confirming the patient name
    assert patient.first_name == "Test"

    # Confirming the patient email
    assert patient.email == "test@example.com"


# =========================================================
# TEST VITAL SIGN SCHEMA
# =========================================================

def test_vital_schema():

    # Creating sample vital signs
    vital = VitalSignCreate(
        patient_id=1,
        heart_rate=72,
        oxygen_saturation=98,
        temperature=98.6,
        systolic_bp=120,
        diastolic_bp=80,
        respiratory_rate=16
    )

    # Confirming the patient ID
    assert vital.patient_id == 1

    # Confirming the heart rate
    assert vital.heart_rate == 72


# =========================================================
# TEST ACTIVITY SCHEMA
# =========================================================

def test_activity_schema():

    # Creating a sample activity
    activity = ActivityCreate(
        patient_id=1,
        activity_type="Walking",
        duration_minutes=30,
        calories_burned=150
    )

    # Confirming the activity type
    assert activity.activity_type == "Walking"


# =========================================================
# TEST ALERT SCHEMA
# =========================================================

def test_alert_schema():

    # Creating a sample alert
    alert = AlertCreate(
        patient_id=1,
        alert_type="High Heart Rate",
        severity="Medium",
        message="Heart rate exceeded the configured threshold.",
        status="Active"
    )

    # Confirming the alert severity
    assert alert.severity == "Medium"


# =========================================================
# TEST RISK ASSESSMENT SCHEMA
# =========================================================

def test_risk_schema():

    # Creating a sample risk assessment
    risk = RiskAssessmentCreate(
        patient_id=1,
        risk_score=35.5,
        risk_level="Moderate",
        assessment_method="HealthTrack Risk Model",
        explanation="Moderate risk based on recent health indicators."
    )

    # Confirming the risk score
    assert risk.risk_score == 35.5

    # Confirming the risk level
    assert risk.risk_level == "Moderate"