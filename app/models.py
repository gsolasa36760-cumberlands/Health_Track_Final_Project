"""
HealthTrack Database Models

This file is defining the SQLAlchemy database models for the
HealthTrack health monitoring system. The models are representing
patients, health profiles, vital signs, activities, alerts, and
risk assessments stored in the MySQL database.
"""

# Importing date and datetime types
from datetime import date, datetime

# Importing SQLAlchemy column and relationship components
from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text
)

# Importing SQLAlchemy ORM components
from sqlalchemy.orm import relationship

# Importing the shared SQLAlchemy Base
from app.database import Base


# =========================================================
# PATIENT MODEL
# =========================================================

class Patient(Base):
    """
    Representing a HealthTrack patient.
    """

    # Defining the database table name
    __tablename__ = "patients"

    # Creating the primary key
    patient_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Storing the patient's first name
    first_name = Column(
        String(100),
        nullable=False
    )

    # Storing the patient's last name
    last_name = Column(
        String(100),
        nullable=False
    )

    # Storing the patient's date of birth
    date_of_birth = Column(
        Date,
        nullable=True
    )

    # Storing the patient's gender
    gender = Column(
        String(20),
        nullable=True
    )

    # Storing the patient's phone number
    phone = Column(
        String(20),
        nullable=True
    )

    # Storing the patient's email address
    email = Column(
        String(150),
        nullable=True
    )

    # Storing the patient's emergency contact
    emergency_contact = Column(
        String(150),
        nullable=True
    )

    # Recording when the patient was created
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # Connecting the patient to the health profile
    health_profile = relationship(
        "HealthProfile",
        back_populates="patient",
        uselist=False,
        cascade="all, delete-orphan"
    )

    # Connecting the patient to vital-sign records
    vital_signs = relationship(
        "VitalSign",
        back_populates="patient",
        cascade="all, delete-orphan"
    )

    # Connecting the patient to activity records
    activities = relationship(
        "Activity",
        back_populates="patient",
        cascade="all, delete-orphan"
    )

    # Connecting the patient to alerts
    alerts = relationship(
        "Alert",
        back_populates="patient",
        cascade="all, delete-orphan"
    )

    # Connecting the patient to risk assessments
    risk_assessments = relationship(
        "RiskAssessment",
        back_populates="patient",
        cascade="all, delete-orphan"
    )


# =========================================================
# HEALTH PROFILE MODEL
# =========================================================

class HealthProfile(Base):
    """
    Representing a patient's health profile.
    """

    # Defining the database table name
    __tablename__ = "health_profiles"

    # Creating the primary key
    profile_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Connecting the profile to a patient
    patient_id = Column(
        Integer,
        ForeignKey("patients.patient_id"),
        nullable=False,
        unique=True
    )

    # Storing the patient's blood type
    blood_type = Column(
        String(10),
        nullable=True
    )

    # Storing known allergies
    allergies = Column(
        Text,
        nullable=True
    )

    # Storing current medications
    medications = Column(
        Text,
        nullable=True
    )

    # Storing existing medical conditions
    medical_conditions = Column(
        Text,
        nullable=True
    )

    # Storing family medical history
    family_history = Column(
        Text,
        nullable=True
    )

    # Recording the profile creation time
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # Connecting back to the patient
    patient = relationship(
        "Patient",
        back_populates="health_profile"
    )


# =========================================================
# VITAL SIGN MODEL
# =========================================================

class VitalSign(Base):
    """
    Representing patient vital-sign measurements.
    """

    # Defining the database table name
    __tablename__ = "vital_signs"

    # Creating the primary key
    vital_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Connecting the vital record to a patient
    patient_id = Column(
        Integer,
        ForeignKey("patients.patient_id"),
        nullable=False,
        index=True
    )

    # Storing the heart-rate measurement
    heart_rate = Column(
        Integer,
        nullable=True
    )

    # Storing the oxygen-saturation measurement
    oxygen_saturation = Column(
        Float,
        nullable=True
    )

    # Storing the body-temperature measurement
    temperature = Column(
        Float,
        nullable=True
    )

    # Storing systolic blood pressure
    systolic_bp = Column(
        Integer,
        nullable=True
    )

    # Storing diastolic blood pressure
    diastolic_bp = Column(
        Integer,
        nullable=True
    )

    # Storing respiratory rate
    respiratory_rate = Column(
        Integer,
        nullable=True
    )

    # Recording when the vital signs were measured
    recorded_at = Column(
        DateTime,
        default=datetime.utcnow,
        index=True
    )

    # Connecting the vital record back to the patient
    patient = relationship(
        "Patient",
        back_populates="vital_signs"
    )


# =========================================================
# ACTIVITY MODEL
# =========================================================

class Activity(Base):
    """
    Representing patient physical-activity information.
    """

    # Defining the database table name
    __tablename__ = "activities"

    # Creating the primary key
    activity_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Connecting the activity to a patient
    patient_id = Column(
        Integer,
        ForeignKey("patients.patient_id"),
        nullable=False,
        index=True
    )

    # Storing the activity type
    activity_type = Column(
        String(100),
        nullable=False
    )

    # Storing activity duration in minutes
    duration_minutes = Column(
        Float,
        nullable=True
    )

    # Storing estimated calories burned
    calories_burned = Column(
        Float,
        nullable=True
    )

    # Recording when the activity occurred
    activity_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    # Connecting the activity back to the patient
    patient = relationship(
        "Patient",
        back_populates="activities"
    )


# =========================================================
# ALERT MODEL
# =========================================================

class Alert(Base):
    """
    Representing health alerts generated by the HealthTrack system.
    """

    # Defining the database table name
    __tablename__ = "alerts"

    # Creating the primary key
    alert_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Connecting the alert to a patient
    patient_id = Column(
        Integer,
        ForeignKey("patients.patient_id"),
        nullable=False,
        index=True
    )

    # Storing the type of alert
    alert_type = Column(
        String(100),
        nullable=False
    )

    # Storing the alert severity
    severity = Column(
        String(30),
        nullable=False
    )

    # Storing the alert message
    message = Column(
        Text,
        nullable=False
    )

    # Storing the alert status
    status = Column(
        String(30),
        default="Active",
        nullable=False
    )

    # Recording whether the alert has been acknowledged
    acknowledged = Column(
        Boolean,
        default=False
    )

    # Recording when the alert was generated
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        index=True
    )

    # Recording when the alert was acknowledged
    acknowledged_at = Column(
        DateTime,
        nullable=True
    )

    # Recording when the alert was resolved
    resolved_at = Column(
        DateTime,
        nullable=True
    )

    # Connecting the alert back to the patient
    patient = relationship(
        "Patient",
        back_populates="alerts"
    )


# =========================================================
# RISK ASSESSMENT MODEL
# =========================================================

class RiskAssessment(Base):
    """
    Representing patient health-risk assessment results.
    """

    # Defining the database table name
    __tablename__ = "risk_assessments"

    # Creating the primary key
    risk_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Connecting the risk assessment to a patient
    patient_id = Column(
        Integer,
        ForeignKey("patients.patient_id"),
        nullable=False,
        index=True
    )

    # Storing the calculated risk score
    risk_score = Column(
        Float,
        nullable=False
    )

    # Storing the risk category
    risk_level = Column(
        String(30),
        nullable=False
    )

    # Storing the assessment method
    assessment_method = Column(
        String(100),
        nullable=True
    )

    # Storing additional assessment information
    explanation = Column(
        Text,
        nullable=True
    )

    # Recording when the assessment was performed
    assessed_at = Column(
        DateTime,
        default=datetime.utcnow,
        index=True
    )

    # Connecting the risk assessment back to the patient
    patient = relationship(
        "Patient",
        back_populates="risk_assessments"
    )