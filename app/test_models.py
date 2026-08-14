"""
HealthTrack Model Test

This file is testing whether all HealthTrack SQLAlchemy models
are loading correctly.
"""

# Importing the SQLAlchemy Base
from app.database import Base

# Importing all HealthTrack database models
from app.models import (
    Patient,
    HealthProfile,
    VitalSign,
    Activity,
    Alert,
    RiskAssessment
)


# Displaying the registered database tables
print("HealthTrack models loaded successfully!")

print("\nRegistered tables:")

# Displaying each registered table name
for table_name in Base.metadata.tables:
    print("-", table_name)