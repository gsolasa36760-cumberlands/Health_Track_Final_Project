# Testing the HealthTrack Patient API endpoints

from datetime import date


# =========================================================
# TEST CREATE PATIENT
# =========================================================

def test_create_patient(client):

    # Creating a unique test patient
    patient_data = {
        "first_name": "API",
        "last_name": "TestPatient",
        "date_of_birth": "1990-01-01",
        "gender": "Male",
        "phone": "555-TEST",
        "email": "api.test.patient@example.com",
        "emergency_contact": "Test Contact"
    }

    # Sending the patient creation request
    response = client.post(
        "/patients",
        json=patient_data
    )

    # Confirming successful patient creation
    assert response.status_code == 201

    # Reading the created patient
    data = response.json()

    # Confirming that an ID was generated
    assert "patient_id" in data

    # Confirming the returned first name
    assert data["first_name"] == "API"


# =========================================================
# TEST GET PATIENTS
# =========================================================

def test_get_patients(client):

    # Requesting the patient list
    response = client.get("/patients")

    # Confirming successful response
    assert response.status_code == 200

    # Reading the returned patient list
    data = response.json()

    # Confirming that the response is a list
    assert isinstance(data, list)