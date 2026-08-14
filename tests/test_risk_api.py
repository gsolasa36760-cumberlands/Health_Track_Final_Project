# Testing the HealthTrack Risk Assessment API endpoints


# =========================================================
# TEST CREATE RISK ASSESSMENT
# =========================================================

def test_create_risk_assessment(client):

    # Creating a sample risk assessment
    risk_data = {
        "patient_id": 1,
        "risk_score": 25,
        "risk_level": "Low",
        "assessment_method": "HealthTrack Risk Model",
        "explanation": "Testing risk assessment creation."
    }

    # Sending the risk creation request
    response = client.post(
        "/risk",
        json=risk_data
    )

    # Confirming successful creation
    assert response.status_code == 201

    # Reading the risk assessment
    data = response.json()

    # Confirming patient ID
    assert data["patient_id"] == 1


# =========================================================
# TEST GET PATIENT RISK ASSESSMENTS
# =========================================================

def test_get_patient_risk(client):

    # Requesting risk assessments for patient 1
    response = client.get("/risk/patient/1")

    # Confirming successful response
    assert response.status_code == 200

    # Reading the assessments
    data = response.json()

    # Confirming list response
    assert isinstance(data, list)


# =========================================================
# TEST AUTOMATIC RISK CALCULATION
# =========================================================

def test_calculate_patient_risk(client):

    # Calculating the patient's risk using the latest vital signs
    response = client.post(
        "/risk/calculate/1"
    )

    # Confirming successful risk calculation
    assert response.status_code == 201

    # Reading the calculated assessment
    data = response.json()

    # Confirming that a risk score was generated
    assert "risk_score" in data

    # Confirming that a risk level was generated
    assert "risk_level" in data