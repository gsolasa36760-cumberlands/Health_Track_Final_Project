# Testing the HealthTrack Vital Signs API endpoints


# =========================================================
# TEST CREATE VITAL SIGN
# =========================================================

def test_create_vital(client):

    # Creating a sample vital-sign record
    vital_data = {
        "patient_id": 1,
        "heart_rate": 72,
        "oxygen_saturation": 98,
        "temperature": 98.6,
        "systolic_bp": 120,
        "diastolic_bp": 80,
        "respiratory_rate": 16
    }

    # Sending the vital-sign creation request
    response = client.post(
        "/vitals",
        json=vital_data
    )

    # Confirming successful creation
    assert response.status_code == 201

    # Reading the response
    data = response.json()

    # Confirming the patient ID
    assert data["patient_id"] == 1


# =========================================================
# TEST GET PATIENT VITALS
# =========================================================

def test_get_patient_vitals(client):

    # Requesting vital signs for patient 1
    response = client.get("/vitals/patient/1")

    # Confirming successful response
    assert response.status_code == 200

    # Reading the returned records
    data = response.json()

    # Confirming that the response is a list
    assert isinstance(data, list)