# Configuring the FastAPI testing client

import pytest

from fastapi.testclient import TestClient

from app.main import app


# =========================================================
# CREATE FASTAPI TEST CLIENT
# =========================================================

@pytest.fixture
def client():

    # Creating a test client for the FastAPI application
    with TestClient(app) as test_client:

        # Returning the client to individual tests
        yield test_client