# Testing the HealthTrack risk calculation service

from services.risk_service import calculate_risk


# TEST NORMAL VITAL SIGNS
def test_normal_vitals_produce_low_risk():

    # Calculating risk using normal vital signs
    result = calculate_risk(
        heart_rate=72,
        oxygen_saturation=98,
        temperature=98.6,
        systolic_bp=120,
        diastolic_bp=80,
        respiratory_rate=16
    )

    # Confirming the expected risk level
    assert result["risk_level"] == "Low"

    # Confirming the expected score
    assert result["risk_score"] == 0


# TEST HIGH-RISK VITAL SIGNS
def test_abnormal_vitals_produce_high_risk():

    # Calculating risk using abnormal vital signs
    result = calculate_risk(
        heart_rate=120,
        oxygen_saturation=90,
        temperature=102,
        systolic_bp=160,
        diastolic_bp=100,
        respiratory_rate=25
    )

    # Confirming the expected risk level
    assert result["risk_level"] == "High"

    # Confirming the maximum risk score
    assert result["risk_score"] == 100

# TEST RISK EXPLANATION
def test_risk_explanation_is_created():

    # Calculating risk using abnormal heart rate
    result = calculate_risk(
        heart_rate=120,
        oxygen_saturation=98,
        temperature=98.6,
        systolic_bp=120,
        diastolic_bp=80,
        respiratory_rate=16
    )

    # Confirming that an explanation was generated
    assert "Elevated heart rate" in result["explanation"]