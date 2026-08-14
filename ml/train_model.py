"""
HealthTrack Risk Prediction Model

This file is training a machine-learning classification model
using health vital-sign measurements. The trained model is being
saved as risk_model.pkl so the HealthTrack application can use
the model for future risk-level predictions.
"""

# Importing pandas for loading and processing the dataset
import pandas as pd

# Importing joblib for saving the trained model
import joblib

# Importing RandomForestClassifier for training the risk model
from sklearn.ensemble import RandomForestClassifier

# Importing train_test_split for separating training and testing data
from sklearn.model_selection import train_test_split

# Importing classification_report for evaluating model performance
from sklearn.metrics import classification_report, accuracy_score


# Defining the dataset location
DATASET_PATH = "ml/dataset/health_risk_dataset.csv"

# Defining the trained model output location
MODEL_PATH = "ml/risk_model.pkl"


# Loading the HealthTrack health-risk dataset
df = pd.read_csv(DATASET_PATH)


# Defining the input health variables
features = [
    "heart_rate",
    "oxygen_saturation",
    "temperature",
    "systolic_bp",
    "diastolic_bp",
    "respiratory_rate"
]


# Separating input variables from the target variable
X = df[features]

# Selecting the risk level as the prediction target
y = df["risk_level"]


# Splitting the dataset into training and testing portions
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# Creating the Random Forest risk classification model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Training the model using the training data
model.fit(X_train, y_train)


# Generating predictions using the testing data
y_pred = model.predict(X_test)


# Calculating the model accuracy
accuracy = accuracy_score(y_test, y_pred)


# Displaying the model accuracy
print("HealthTrack Risk Model Accuracy:")
print(f"{accuracy:.2f}")


# Displaying the classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Saving the trained model
joblib.dump(model, MODEL_PATH)


# Confirming successful model creation
print(f"\nRisk model saved successfully to: {MODEL_PATH}")