"""
HealthTrack Machine Learning Risk Service

This file is loading the trained HealthTrack risk model and
using patient vital-sign measurements to predict the patient's
risk level. The service is being separated from the API layer
so the trained model can be reused by different application components.
"""

# Importing os for creating the model file path
import os

# Importing joblib for loading the trained model
import joblib


# Defining the project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)


# Defining the trained model location
MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml",
    "risk_model.pkl"
)


# Loading the trained HealthTrack risk model
model = joblib.load(MODEL_PATH)


# Defining the machine-learning prediction function
def predict_risk(
    heart_rate,
    oxygen_saturation,
    temperature,
    systolic_bp,
    diastolic_bp,
    respiratory_rate
):

    # Creating the feature values required by the trained model
    features = [[
        heart_rate,
        oxygen_saturation,
        temperature,
        systolic_bp,
        diastolic_bp,
        respiratory_rate
    ]]

    # Generating the risk-level prediction
    prediction = model.predict(features)[0]

    # Returning the predicted risk level
    return prediction