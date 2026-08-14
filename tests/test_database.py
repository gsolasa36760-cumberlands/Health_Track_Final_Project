# Testing the HealthTrack database connection

from sqlalchemy import text

from app.database import engine


# =========================================================
# TEST DATABASE CONNECTION
# =========================================================

def test_database_connection():

    # Opening a connection to the database
    with engine.connect() as connection:

        # Executing a simple database query
        result = connection.execute(
            text("SELECT 1")
        )

        # Reading the query result
        value = result.scalar()

        # Confirming that the database returned the expected value
        assert value == 1