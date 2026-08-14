/*
Creating the HealthTrack healthcare monitoring database for the final project.
Defining patient information, health profiles, vital signs, physical activities,
alerts, and risk assessments with appropriate primary keys and foreign-key
relationships. Inserting sample healthcare data for demonstrating the system
functionality and verifying the database structure.
*/

-- Removing the existing HealthTrack database
DROP DATABASE IF EXISTS healthtrackDB;

-- Creating the HealthTrack database
CREATE DATABASE healthtrackDB;

-- Selecting the HealthTrack database
USE healthtrackDB;

-- Creating the patients table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(30),
    phone VARCHAR(30),
    email VARCHAR(255),
    emergency_contact VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Creating the health_profiles table
CREATE TABLE health_profiles (
    profile_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    blood_type VARCHAR(10),
    height FLOAT,
    weight FLOAT,
    medical_conditions TEXT,
    medications TEXT,
    allergies TEXT,
    smoking_status VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_health_profiles_patient
    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id)
    ON DELETE CASCADE
);

-- Creating the vital_signs table
CREATE TABLE vital_signs (
    vital_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    heart_rate INT,
    oxygen_saturation FLOAT,
    temperature FLOAT,
    systolic_bp INT,
    diastolic_bp INT,
    respiratory_rate INT,
    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_vital_signs_patient
    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id)
    ON DELETE CASCADE
);

-- Creating the activities table
CREATE TABLE activities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    activity_type VARCHAR(100) NOT NULL,
    duration_minutes FLOAT,
    calories_burned FLOAT,
    activity_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_activities_patient
    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id)
    ON DELETE CASCADE
);

-- Creating the alerts table
CREATE TABLE alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    alert_type VARCHAR(100) NOT NULL,
    severity VARCHAR(30) NOT NULL,
    message TEXT,
    status VARCHAR(30) NOT NULL DEFAULT 'Active',
    acknowledged BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    acknowledged_at DATETIME NULL,
    resolved_at DATETIME NULL,
    CONSTRAINT fk_alerts_patient
    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id)
    ON DELETE CASCADE
);

-- Creating the risk_assessments table
CREATE TABLE risk_assessments (
    risk_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    risk_score FLOAT NOT NULL,
    risk_level VARCHAR(50) NOT NULL,
    assessment_method VARCHAR(100),
    explanation TEXT,
    assessed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_risk_assessments_patient
    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id)
    ON DELETE CASCADE
);

-- Inserting sample patient information
INSERT INTO patients
(
    first_name,
    last_name,
    date_of_birth,
    gender,
    phone,
    email,
    emergency_contact
)

VALUES
(
    'John',
    'Smith',
    '1985-05-15',
    'Male',
    '555-0100',
    'john.smith@example.com',
    'Jane Smith'
);


-- Inserting sample health profile information
INSERT INTO health_profiles
(
    patient_id,
    blood_type,
    height,
    weight,
    medical_conditions,
    medications,
    allergies,
    smoking_status
)

VALUES
(
    1,
    'O+',
    175.0,
    75.0,
    'None reported',
    'None reported',
    'None reported',
    'Non-Smoker'
);


-- Inserting sample vital-sign information
INSERT INTO vital_signs
(
    patient_id,
    heart_rate,
    oxygen_saturation,
    temperature,
    systolic_bp,
    diastolic_bp,
    respiratory_rate
)

VALUES
(
    1,
    72,
    98.0,
    98.6,
    120,
    80,
    16
);


-- Inserting sample physical activity information
INSERT INTO activities
(
    patient_id,
    activity_type,
    duration_minutes,
    calories_burned
)

VALUES
(
    1,
    'Walking',
    30.0,
    150.0
);


-- Inserting sample alert information
INSERT INTO alerts
(
    patient_id,
    alert_type,
    severity,
    message,
    status,
    acknowledged
)

VALUES
(
    1,
    'High Heart Rate',
    'Medium',
    'Heart rate exceeded the configured threshold.',
    'Active',
    FALSE
);

-- Inserting sample risk assessment information
INSERT INTO risk_assessments
(patient_id,
    risk_score,
    risk_level,
    assessment_method,
    explanation
)

VALUES
(1,
    0.0,
    'Low',
    'HealthTrack Risk Model',
    'Vital signs are within the configured normal ranges.'
);

-- Displaying the created HealthTrack tables
SHOW TABLES;

-- Displaying the inserted patient information
SELECT * FROM patients;

-- Displaying the inserted health profile information
SELECT * FROM health_profiles;

-- Displaying the inserted vital-sign information
SELECT * FROM vital_signs;

-- Displaying the inserted activity information
SELECT * FROM activities;

-- Displaying the inserted alert information
SELECT * FROM alerts;

-- Displaying the inserted risk assessment information
SELECT * FROM risk_assessments;
