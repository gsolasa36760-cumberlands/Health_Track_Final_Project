# Testing the HealthTrack Alert API endpoints


# =========================================================
# TEST CREATE ALERT
# =========================================================

def test_create_alert(client):

    # Creating a sample alert
    alert_data = {
        "patient_id": 1,
        "alert_type": "Test Alert",
        "severity": "Medium",
        "message": "Testing HealthTrack alert management.",
        "status": "Active"
    }

    # Sending the alert creation request
    response = client.post(
        "/alerts",
        json=alert_data
    )

    # Confirming successful creation
    assert response.status_code == 201

    # Reading the created alert
    data = response.json()

    # Confirming the patient ID
    assert data["patient_id"] == 1


# =========================================================
# TEST GET PATIENT ALERTS
# =========================================================

def test_get_patient_alerts(client):

    # Requesting alerts for patient 1
    response = client.get("/alerts/patient/1")

    # Confirming successful response
    assert response.status_code == 200

    # Reading the alerts
    data = response.json()

    # Confirming list response
    assert isinstance(data, list)