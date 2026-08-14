"""
HealthTrack Database Connection Test

This file is testing whether SQLAlchemy can connect successfully
to the HealthTrack MySQL database.
"""

# Importing the SQLAlchemy engine from the app database module
from app.database import engine


# Testing the database connection
try:

    # Opening a connection to the MySQL database
    with engine.connect() as connection:

        # Displaying a successful connection message
        print("Database connection successful!")

except Exception as error:

    # Displaying a failed connection message
    print("Database connection failed.")

    # Displaying the actual database error
    print("Error:", error)