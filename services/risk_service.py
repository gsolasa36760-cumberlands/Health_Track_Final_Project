# Creating the HealthTrack risk calculation service


# =========================================================
# RISK CALCULATION
# =========================================================

# Calculating a risk score from vital signs
def calculate_risk(
    heart_rate: int,
    oxygen_saturation: float,
    temperature: float,
    systolic_bp: int,
    diastolic_bp: int,
    respiratory_rate: int
):
    # Starting the risk score at zero
    risk_score = 0

    # Creating a list to store explanations
    explanations = []

    # =====================================================
    # HEART RATE
    # =====================================================

    # Increasing risk when heart rate is above normal range
    if heart_rate > 100:
        risk_score += 20
        explanations.append("Elevated heart rate")

    # Increasing risk when heart rate is below normal range
    elif heart_rate < 60:
        risk_score += 10
        explanations.append("Low heart rate")

    # =====================================================
    # OXYGEN SATURATION
    # =====================================================

    # Increasing risk when oxygen saturation is below 95 percent
    if oxygen_saturation < 95:
        risk_score += 25
        explanations.append("Low oxygen saturation")

    # =====================================================
    # TEMPERATURE
    # =====================================================

    # Increasing risk when temperature indicates fever
    if temperature >= 100.4:
        risk_score += 15
        explanations.append("Elevated temperature")

    # Increasing risk when temperature is unusually low
    elif temperature < 95:
        risk_score += 10
        explanations.append("Low temperature")

    # =====================================================
    # BLOOD PRESSURE
    # =====================================================

    # Increasing risk for elevated systolic blood pressure
    if systolic_bp >= 140:
        risk_score += 15
        explanations.append("Elevated systolic blood pressure")

    # Increasing risk for elevated diastolic blood pressure
    if diastolic_bp >= 90:
        risk_score += 15
        explanations.append("Elevated diastolic blood pressure")

    # =====================================================
    # RESPIRATORY RATE
    # =====================================================

    # Increasing risk when respiratory rate is elevated
    if respiratory_rate > 20:
        risk_score += 15
        explanations.append("Elevated respiratory rate")

    # Increasing risk when respiratory rate is unusually low
    elif respiratory_rate < 12:
        risk_score += 10
        explanations.append("Low respiratory rate")

    # =====================================================
    # LIMITING SCORE
    # =====================================================

    # Limiting the maximum risk score to 100
    risk_score = min(risk_score, 100)

    # =====================================================
    # DETERMINING RISK LEVEL
    # =====================================================

    # Classifying scores from 0 through 29 as Low risk
    if risk_score < 30:
        risk_level = "Low"

    # Classifying scores from 30 through 59 as Moderate risk
    elif risk_score < 60:
        risk_level = "Moderate"

    # Classifying scores from 60 through 100 as High risk
    else:
        risk_level = "High"

    # Creating the explanation
    if explanations:
        explanation = "; ".join(explanations)
    else:
        explanation = "Vital signs are within the configured normal ranges."

    # Returning the calculated assessment
    return {
        "risk_score": float(risk_score),
        "risk_level": risk_level,
        "explanation": explanation
    }