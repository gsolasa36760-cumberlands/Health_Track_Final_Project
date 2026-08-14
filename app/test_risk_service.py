# Testing the HealthTrack risk calculation service

from services.risk_service import calculate_risk


# =========================================================
# TEST NORMAL VITAL SIGNS
# =========================================================

# Calculating risk for normal vital signs
normal_result = calculate_risk(
    heart_rate=72,
    oxygen_saturation=98,
    temperature=98.6,
    systolic_bp=120,
    diastolic_bp=80,
    respiratory_rate=16
)

print("Normal vital signs result:")
print(normal_result)


# =========================================================
# TEST HIGH-RISK VITAL SIGNS
# =========================================================

# Calculating risk for abnormal vital signs
high_risk_result = calculate_risk(
    heart_rate=120,
    oxygen_saturation=90,
    temperature=102,
    systolic_bp=160,
    diastolic_bp=100,
    respiratory_rate=25
)

print("\nHigh-risk vital signs result:")
print(high_risk_result)