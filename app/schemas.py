"""
HealthTrack API Schemas

This file is defining Pydantic schemas for validating request
data and formatting response data used by the HealthTrack API.
"""

# Importing date and datetime types
from datetime import date, datetime

# Importing optional typing support
from typing import Optional

# Importing Pydantic components
from pydantic import BaseModel, ConfigDict, Field


# =========================================================
# PATIENT SCHEMAS
# =========================================================

class PatientBase(BaseModel):
    """
    Defining the common patient information.
    """

    # Storing the patient's first name
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    # Storing the patient's last name
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    # Storing the patient's date of birth
    date_of_birth: Optional[date] = None

    # Storing the patient's gender
    gender: Optional[str] = Field(
        default=None,
        max_length=20
    )

    # Storing the patient's phone number
    phone: Optional[str] = Field(
        default=None,
        max_length=20
    )

    # Storing the patient's email address
    email: Optional[str] = Field(
        default=None,
        max_length=150
    )

    # Storing the emergency contact
    emergency_contact: Optional[str] = Field(
        default=None,
        max_length=150
    )


class PatientCreate(PatientBase):
    """
    Defining data required for creating a patient.
    """

    pass


class PatientUpdate(BaseModel):
    """
    Defining optional data for updating a patient.
    """

    # Allowing the first name to be updated
    first_name: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    # Allowing the last name to be updated
    last_name: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    # Allowing the date of birth to be updated
    date_of_birth: Optional[date] = None

    # Allowing the gender to be updated
    gender: Optional[str] = Field(
        default=None,
        max_length=20
    )

    # Allowing the phone to be updated
    phone: Optional[str] = Field(
        default=None,
        max_length=20
    )

    # Allowing the email to be updated
    email: Optional[str] = Field(
        default=None,
        max_length=150
    )

    # Allowing the emergency contact to be updated
    emergency_contact: Optional[str] = Field(
        default=None,
        max_length=150
    )


class PatientResponse(PatientBase):
    """
    Defining patient information returned by the API.
    """

    # Returning the patient database identifier
    patient_id: int

    # Returning the patient creation timestamp
    created_at: Optional[datetime] = None

    # Configuring Pydantic for SQLAlchemy objects
    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# HEALTH PROFILE SCHEMAS
# =========================================================

class HealthProfileBase(BaseModel):
    """
    Defining common health-profile information.
    """

    # Storing the patient's blood type
    blood_type: Optional[str] = Field(
        default=None,
        max_length=10
    )

    # Storing known allergies
    allergies: Optional[str] = None

    # Storing current medications
    medications: Optional[str] = None

    # Storing existing medical conditions
    medical_conditions: Optional[str] = None

    # Storing family medical history
    family_history: Optional[str] = None


class HealthProfileCreate(HealthProfileBase):
    """
    Defining data required for creating a health profile.
    """

    # Connecting the profile to a patient
    patient_id: int


class HealthProfileResponse(HealthProfileBase):
    """
    Defining health-profile information returned by the API.
    """

    # Returning the profile identifier
    profile_id: int

    # Returning the patient identifier
    patient_id: int

    # Returning the creation timestamp
    created_at: Optional[datetime] = None

    # Enabling SQLAlchemy object conversion
    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# VITAL SIGN SCHEMAS
# =========================================================

class VitalSignBase(BaseModel):
    """
    Defining common vital-sign information.
    """

    # Storing heart rate
    heart_rate: Optional[int] = Field(
        default=None,
        ge=0,
        le=300
    )

    # Storing oxygen saturation
    oxygen_saturation: Optional[float] = Field(
        default=None,
        ge=0,
        le=100
    )

    # Storing body temperature in Fahrenheit
    temperature: Optional[float] = Field(
    default=None,
    ge=80,
    le=110
    )

    # Storing systolic blood pressure
    systolic_bp: Optional[int] = Field(
        default=None,
        ge=0,
        le=300
    )

    # Storing diastolic blood pressure
    diastolic_bp: Optional[int] = Field(
        default=None,
        ge=0,
        le=200
    )

    # Storing respiratory rate
    respiratory_rate: Optional[int] = Field(
        default=None,
        ge=0,
        le=100
    )


class VitalSignCreate(VitalSignBase):
    """
    Defining data required for creating a vital-sign record.
    """

    # Connecting the vital-sign record to a patient
    patient_id: int


class VitalSignResponse(VitalSignBase):
    """
    Defining vital-sign information returned by the API.
    """

    # Returning the vital-sign identifier
    vital_id: int

    # Returning the patient identifier
    patient_id: int

    # Returning the measurement timestamp
    recorded_at: Optional[datetime] = None

    # Enabling SQLAlchemy object conversion
    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# ACTIVITY SCHEMAS
# =========================================================

class ActivityBase(BaseModel):
    """
    Defining common activity information.
    """

    # Storing the activity type
    activity_type: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    # Storing activity duration
    duration_minutes: Optional[float] = Field(
        default=None,
        ge=0
    )

    # Storing estimated calories burned
    calories_burned: Optional[float] = Field(
        default=None,
        ge=0
    )


class ActivityCreate(ActivityBase):
    """
    Defining data required for creating an activity record.
    """

    # Connecting the activity to a patient
    patient_id: int


class ActivityResponse(ActivityBase):
    """
    Defining activity information returned by the API.
    """

    # Returning the activity identifier
    activity_id: int

    # Returning the patient identifier
    patient_id: int

    # Returning the activity timestamp
    activity_date: Optional[datetime] = None

    # Enabling SQLAlchemy object conversion
    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# ALERT SCHEMAS
# =========================================================

class AlertBase(BaseModel):
    """
    Defining common alert information.
    """

    # Storing the alert type
    alert_type: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    # Storing alert severity
    severity: str = Field(
        ...,
        min_length=1,
        max_length=30
    )

    # Storing the alert message
    message: str

    # Storing the alert status
    status: str = Field(
        default="Active",
        max_length=30
    )


class AlertCreate(AlertBase):
    """
    Defining data required for creating an alert.
    """

    # Connecting the alert to a patient
    patient_id: int


class AlertResponse(AlertBase):
    """
    Defining alert information returned by the API.
    """

    # Returning the alert identifier
    alert_id: int

    # Returning the patient identifier
    patient_id: int

    # Returning whether the alert is acknowledged
    acknowledged: bool

    # Returning the creation timestamp
    created_at: Optional[datetime] = None

    # Returning the acknowledgement timestamp
    acknowledged_at: Optional[datetime] = None

    # Returning the resolution timestamp
    resolved_at: Optional[datetime] = None

    # Enabling SQLAlchemy object conversion
    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# RISK ASSESSMENT SCHEMAS
# =========================================================

class RiskAssessmentCreate(BaseModel):
    """
    Defining data required for creating a risk assessment.
    """

    # Connecting the assessment to a patient
    patient_id: int

    # Storing the calculated risk score
    risk_score: float = Field(
        ...,
        ge=0
    )

    # Storing the calculated risk level
    risk_level: str = Field(
        ...,
        min_length=1,
        max_length=30
    )

    # Storing the assessment method
    assessment_method: Optional[str] = Field(
        default=None,
        max_length=100
    )

    # Storing the explanation
    explanation: Optional[str] = None


class RiskAssessmentResponse(BaseModel):
    """
    Defining risk-assessment information returned by the API.
    """

    # Returning the risk-assessment identifier
    risk_id: int

    # Returning the patient identifier
    patient_id: int

    # Returning the risk score
    risk_score: float

    # Returning the risk level
    risk_level: str

    # Returning the assessment method
    assessment_method: Optional[str] = None

    # Returning the explanation
    explanation: Optional[str] = None

    # Returning the assessment timestamp
    assessed_at: Optional[datetime] = None

    # Enabling SQLAlchemy object conversion
    model_config = ConfigDict(
        from_attributes=True
    )