# Testing the HealthTrack Activity API endpoints


# =========================================================
# TEST CREATE ACTIVITY
# =========================================================

def test_create_activity(client):

    # Creating a sample activity
    activity_data = {
        "patient_id": 1,
        "activity_type": "Walking",
        "duration_minutes": 30,
        "calories_burned": 150
    }

    # Sending the activity creation request
    response = client.post(
        "/activities",
        json=activity_data
    )

    # Confirming successful creation
    assert response.status_code == 201

    # Reading the created activity
    data = response.json()

    # Confirming the patient ID
    assert data["patient_id"] == 1


# =========================================================
# TEST GET PATIENT ACTIVITIES
# =========================================================

def test_get_patient_activities(client):

    # Requesting activities for patient 1
    response = client.get("/activities/patient/1")

    # Confirming successful response
    assert response.status_code == 200

    # Reading the activities
    data = response.json()

    # Confirming list response
    assert isinstance(data, list)