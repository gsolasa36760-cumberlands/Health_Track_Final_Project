"""
HealthTrack Database Configuration

This file is configuring the SQLAlchemy connection for the
HealthTrack MySQL database. Environment variables are being
used to keep database credentials separate from application code.
"""

# Importing os for reading environment variables
import os

# Importing dotenv for loading environment variables
from dotenv import load_dotenv

# Importing SQLAlchemy components
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# Loading variables from the .env file
load_dotenv()


# Reading the database connection URL
DATABASE_URL = os.getenv("DATABASE_URL")


# Checking whether the database URL exists
if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is not configured. "
        "Please create a .env file containing DATABASE_URL."
    )


# Creating the SQLAlchemy database engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600
)


# Creating the database session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Creating the SQLAlchemy Base class
Base = declarative_base()


# Creating the FastAPI database dependency
def get_db():
    """
    Providing a SQLAlchemy database session to FastAPI endpoints.
    """

    # Creating a new database session
    db = SessionLocal()

    try:

        # Providing the database session
        yield db

    finally:

        # Closing the database session
        db.close()