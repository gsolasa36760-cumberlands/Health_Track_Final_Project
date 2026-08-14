# Testing the HealthTrack SQLAlchemy models

from app.database import Base

# Importing all HealthTrack models
from app.models import (
    Patient,
    HealthProfile,
    VitalSign,
    Activity,
    Alert,
    RiskAssessment
)


# =========================================================
# TEST REGISTERED TABLES
# =========================================================

def test_healthtrack_tables():

    # Retrieving the registered database table names
    tables = set(Base.metadata.tables.keys())

    # Defining the expected HealthTrack tables
    expected_tables = {
        "patients",
        "health_profiles",
        "vital_signs",
        "activities",
        "alerts",
        "risk_assessments"
    }

    # Confirming that all expected tables are registered
    assert expected_tables.issubset(tables)