"""
HealthTrack Schema Test

This file is testing whether the Pydantic schemas are loading
correctly before connecting them to the API endpoints.
"""

# Importing HealthTrack schemas
from app.schemas import (
    PatientCreate,
    PatientResponse,
    HealthProfileCreate,
    VitalSignCreate,
    ActivityCreate,
    AlertCreate,
    RiskAssessmentCreate
)


# Displaying successful schema loading
print("HealthTrack schemas loaded successfully!")

# Creating a sample patient request
sample_patient = PatientCreate(
    first_name="John",
    last_name="Smith",
    date_of_birth="1985-05-15",
    gender="Male",
    phone="555-0100",
    email="john.smith@example.com",
    emergency_contact="Jane Smith"
)

# Displaying the validated patient data
print("\nSample patient:")
print(sample_patient.model_dump())

# Creating a sample vital-sign request
sample_vital = VitalSignCreate(
    patient_id=1,
    heart_rate=72,
    oxygen_saturation=98,
    temperature=98.6,
    systolic_bp=120,
    diastolic_bp=80,
    respiratory_rate=16
)

# Displaying the validated vital-sign data
print("\nSample vital signs:")
print(sample_vital.model_dump())

# Creating a sample activity request
sample_activity = ActivityCreate(
    patient_id=1,
    activity_type="Walking",
    duration_minutes=30,
    calories_burned=150
)

# Displaying the validated activity data
print("\nSample activity:")
print(sample_activity.model_dump())

# Creating a sample alert request
sample_alert = AlertCreate(
    patient_id=1,
    alert_type="High Heart Rate",
    severity="Medium",
    message="Heart rate exceeded the configured threshold.",
    status="Active"
)

# Displaying the validated alert data
print("\nSample alert:")
print(sample_alert.model_dump())

# Creating a sample risk-assessment request
sample_risk = RiskAssessmentCreate(
    patient_id=1,
    risk_score=35.5,
    risk_level="Moderate",
    assessment_method="HealthTrack Risk Model",
    explanation="Moderate risk based on recent health indicators."
)

# Displaying the validated risk-assessment data
print("\nSample risk assessment:")
print(sample_risk.model_dump())