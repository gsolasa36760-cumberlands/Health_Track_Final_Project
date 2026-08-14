"""
HealthTrack Alembic Migration Configuration

This file is configuring Alembic to detect SQLAlchemy models
and generate database migrations for the HealthTrack system.
"""

# Importing the logging configuration
from logging.config import fileConfig
import os
from dotenv import load_dotenv

# Importing Alembic context
from alembic import context

# Importing SQLAlchemy engine configuration
from sqlalchemy import engine_from_config
from sqlalchemy import pool

# Importing the HealthTrack SQLAlchemy Base
from app.database import Base

# Importing all HealthTrack models
# This import is registering the models with Base.metadata
from app import models

# ---------------------------------------------------------
# ALEMBIC CONFIGURATION
# ---------------------------------------------------------

# Getting the Alembic configuration object
config = context.config

# Loading environment variables from the .env file
load_dotenv()

# Loading the database URL from the .env file
database_url = os.getenv("DATABASE_URL")


# Checking whether the database URL is available
if not database_url:
    raise ValueError(
        "DATABASE_URL is not configured."
    )


# Escaping percent signs for Alembic ConfigParser
# The %40 in the encoded password is being converted to %%40
# so that ConfigParser can process the database URL correctly
database_url_for_alembic = database_url.replace("%", "%%")


# Providing the database URL to Alembic
config.set_main_option(
    "sqlalchemy.url",
    database_url_for_alembic
)

# ---------------------------------------------------------
# LOGGING CONFIGURATION
# ---------------------------------------------------------

# Loading logging configuration from alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# ---------------------------------------------------------
# TARGET METADATA
# ---------------------------------------------------------

# Providing SQLAlchemy metadata to Alembic
target_metadata = Base.metadata


# ---------------------------------------------------------
# OFFLINE MIGRATIONS
# ---------------------------------------------------------

def run_migrations_offline() -> None:
    """
    Running migrations without creating a database connection.
    """

    # Getting the database URL from Alembic configuration
    url = config.get_main_option("sqlalchemy.url")

    # Configuring Alembic for offline migration
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={
            "paramstyle": "named"
        },
    )

    # Running the migration transaction
    with context.begin_transaction():

        # Running migrations
        context.run_migrations()


# ---------------------------------------------------------
# ONLINE MIGRATIONS
# ---------------------------------------------------------

def run_migrations_online() -> None:
    """
    Running migrations using an active database connection.
    """

    # Creating the SQLAlchemy engine
    connectable = engine_from_config(
        config.get_section(
            config.config_ini_section,
            {}
        ),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # Creating a database connection
    with connectable.connect() as connection:

        # Configuring Alembic with the SQLAlchemy metadata
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        # Starting the migration transaction
        with context.begin_transaction():

            # Running the migrations
            context.run_migrations()


# ---------------------------------------------------------
# SELECTING MIGRATION MODE
# ---------------------------------------------------------

if context.is_offline_mode():

    # Running offline migrations
    run_migrations_offline()

else:

    # Running online migrations
    run_migrations_online()