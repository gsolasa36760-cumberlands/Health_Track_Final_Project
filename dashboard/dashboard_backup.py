"""
HealthTrack Dashboard

This dashboard is connecting to the FastAPI backend,
retrieving patient health information, displaying
vital signs, risk history, activities, and alerts,
and presenting historical health information using
interactive Plotly line charts with automatic refreshing.
"""

# Importing Dash components
from dash import Dash, html, dcc, Input, Output

# Importing Plotly graph objects
import plotly.graph_objects as go

# Importing requests for communicating with FastAPI
import requests


# Defining the FastAPI backend address
API_URL = "http://127.0.0.1:8000"


# Creating the Dash application
app = Dash(__name__)

# Defining the dashboard browser title
app.title = "HealthTrack Dashboard"


# Creating a function for retrieving patient information
def get_patient(patient_id):

    try:

        response = requests.get(
            f"{API_URL}/patients/{patient_id}",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

    except requests.RequestException:
        pass

    return None


# Creating a function for retrieving vital signs
def get_vitals(patient_id):

    try:

        response = requests.get(
            f"{API_URL}/vitals/patient/{patient_id}",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

    except requests.RequestException:
        pass

    return []


# Creating a function for retrieving activities
def get_activities(patient_id):

    try:

        response = requests.get(
            f"{API_URL}/activities/patient/{patient_id}",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

    except requests.RequestException:
        pass

    return []


# Creating a function for retrieving risk assessments
def get_risk(patient_id):

    try:

        response = requests.get(
            f"{API_URL}/risk/patient/{patient_id}",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

    except requests.RequestException:
        pass

    return []


# Creating a function for retrieving alerts
def get_alerts(patient_id):

    try:

        response = requests.get(
            f"{API_URL}/alerts/patient/{patient_id}",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

    except requests.RequestException:
        pass

    return []


# Creating the dashboard layout
app.layout = html.Div(

    [

        # Creating the main dashboard heading
        html.H1(
            "HealthTrack Patient Monitoring Dashboard",
            style={
                "textAlign": "center",
                "marginBottom": "20px"
            }
        ),

        # Creating the patient ID input section
        html.Div(

            [

                html.Label(
                    "Patient ID:",
                    style={
                        "fontWeight": "bold",
                        "marginRight": "10px"
                    }
                ),

                dcc.Input(
                    id="patient-id",
                    type="number",
                    value=1,
                    min=1,
                    step=1
                )

            ],

            style={
                "textAlign": "center",
                "marginBottom": "20px"
            }
        ),

        # Creating automatic dashboard refresh
        dcc.Interval(
            id="refresh-interval",
            interval=10 * 1000,
            n_intervals=0
        ),

        # Creating patient information section
        html.Div(

            [

                html.H2("Patient Information"),

                html.Div(
                    id="patient-information"
                )

            ],

            style={
                "padding": "20px",
                "marginBottom": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "8px"
            }
        ),

        # Creating latest vital signs section
        html.Div(

            [

                html.H2("Latest Vital Signs"),

                html.Div(
                    id="vital-information"
                )

            ],

            style={
                "padding": "20px",
                "marginBottom": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "8px"
            }
        ),

        # Creating heart rate chart
        html.Div(

            [

                html.H2("Heart Rate History"),

                dcc.Graph(
                    id="heart-rate-chart"
                )

            ],

            style={
                "padding": "20px",
                "marginBottom": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "8px"
            }
        ),

        # Creating oxygen saturation chart
        html.Div(

            [

                html.H2("Oxygen Saturation History"),

                dcc.Graph(
                    id="oxygen-chart"
                )

            ],

            style={
                "padding": "20px",
                "marginBottom": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "8px"
            }
        ),

        # Creating temperature chart
        html.Div(

            [

                html.H2("Temperature History"),

                dcc.Graph(
                    id="temperature-chart"
                )

            ],

            style={
                "padding": "20px",
                "marginBottom": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "8px"
            }
        ),

        # Creating blood pressure chart
        html.Div(

            [

                html.H2("Blood Pressure History"),

                dcc.Graph(
                    id="blood-pressure-chart"
                )

            ],

            style={
                "padding": "20px",
                "marginBottom": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "8px"
            }
        ),

        # Creating risk assessment section
        html.Div(

            [

                html.H2("Risk Assessment"),

                html.Div(
                    id="risk-information"
                ),

                dcc.Graph(
                    id="risk-chart"
                ),

                dcc.Graph(
                    id="risk-history-chart"
                )

            ],

            style={
                "padding": "20px",
                "marginBottom": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "8px"
            }
        ),

        # Creating activity section
        html.Div(

            [

                html.H2("Recent Activities"),

                html.Div(
                    id="activity-information"
                ),

                dcc.Graph(
                    id="activity-chart"
                )

            ],

            style={
                "padding": "20px",
                "marginBottom": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "8px"
            }
        ),

        # Creating alert section
        html.Div(

            [

                html.H2("Alerts"),

                html.Div(
                    id="alert-information"
                )

            ],

            style={
                "padding": "20px",
                "marginBottom": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "8px"
            }
        )

    ],

    style={
        "fontFamily": "Arial",
        "maxWidth": "1200px",
        "margin": "auto",
        "padding": "20px"
    }
)


# Creating the dashboard callback
@app.callback(

    [

        Output("patient-information", "children"),
        Output("vital-information", "children"),
        Output("heart-rate-chart", "figure"),
        Output("oxygen-chart", "figure"),
        Output("temperature-chart", "figure"),
        Output("blood-pressure-chart", "figure"),
        Output("risk-information", "children"),
        Output("risk-chart", "figure"),
        Output("risk-history-chart", "figure"),
        Output("activity-information", "children"),
        Output("activity-chart", "figure"),
        Output("alert-information", "children")

    ],

    [

        Input("patient-id", "value"),
        Input("refresh-interval", "n_intervals")

    ]
)


# Defining the dashboard update function
def update_dashboard(patient_id, n_intervals):

    # Handling a missing patient ID
    if not patient_id:
        patient_id = 1

    # Retrieving patient information
    patient = get_patient(patient_id)

    # Retrieving vital signs
    vitals = get_vitals(patient_id)

    # Retrieving risk assessments
    risks = get_risk(patient_id)

    # Retrieving activities
    activities = get_activities(patient_id)

    # Retrieving alerts
    alerts = get_alerts(patient_id)


    # Creating patient information
    if patient:

        patient_information = html.Div(

            [

                html.P(
                    f"Patient ID: "
                    f"{patient.get('patient_id', 'N/A')}"
                ),

                html.P(
                    f"Name: "
                    f"{patient.get('first_name', '')} "
                    f"{patient.get('last_name', '')}"
                ),

                html.P(
                    f"Gender: "
                    f"{patient.get('gender', 'N/A')}"
                ),

                html.P(
                    f"Date of Birth: "
                    f"{patient.get('date_of_birth', 'N/A')}"
                ),

                html.P(
                    f"Phone: "
                    f"{patient.get('phone', 'N/A')}"
                ),

                html.P(
                    f"Email: "
                    f"{patient.get('email', 'N/A')}"
                )

            ]
        )

    else:

        patient_information = html.P(
            "Patient information could not be retrieved."
        )


    # Creating latest vital-sign information
    if vitals:

        latest_vital = vitals[-1]

        vital_information = html.Div(

            [

                html.P(
                    f"Heart Rate: "
                    f"{latest_vital.get('heart_rate', 'N/A')} bpm"
                ),

                html.P(
                    f"Oxygen Saturation: "
                    f"{latest_vital.get('oxygen_saturation', 'N/A')}%"
                ),

                html.P(
                    f"Temperature: "
                    f"{latest_vital.get('temperature', 'N/A')} °F"
                ),

                html.P(
                    f"Systolic Blood Pressure: "
                    f"{latest_vital.get('systolic_bp', 'N/A')} mmHg"
                ),

                html.P(
                    f"Diastolic Blood Pressure: "
                    f"{latest_vital.get('diastolic_bp', 'N/A')} mmHg"
                ),

                html.P(
                    f"Respiratory Rate: "
                    f"{latest_vital.get('respiratory_rate', 'N/A')} breaths/min"
                )

            ]
        )

    else:

        vital_information = html.P(
            "No vital signs available."
        )


    # Creating empty chart figures
    heart_rate_figure = go.Figure()
    oxygen_figure = go.Figure()
    temperature_figure = go.Figure()
    blood_pressure_figure = go.Figure()
    risk_history_figure = go.Figure()
    activity_figure = go.Figure()


    # Creating vital-sign charts
    if vitals:

        # Extracting recorded timestamps
        times = [
            vital.get("recorded_at", "")
            for vital in vitals
        ]

        # Extracting heart-rate values
        heart_rates = [
            vital.get("heart_rate")
            for vital in vitals
        ]

        # Extracting oxygen values
        oxygen_values = [
            vital.get("oxygen_saturation")
            for vital in vitals
        ]

        # Extracting temperature values
        temperatures = [
            vital.get("temperature")
            for vital in vitals
        ]

        # Extracting systolic values
        systolic_values = [
            vital.get("systolic_bp")
            for vital in vitals
        ]

        # Extracting diastolic values
        diastolic_values = [
            vital.get("diastolic_bp")
            for vital in vitals
        ]


        # Creating the heart-rate line chart
        heart_rate_figure.add_trace(

            go.Scatter(
                x=times,
                y=heart_rates,
                mode="lines+markers",
                name="Heart Rate"
            )

        )

        heart_rate_figure.update_layout(
            title="Heart Rate Over Time",
            xaxis_title="Recorded Time",
            yaxis_title="Heart Rate (bpm)"
        )


        # Creating the oxygen-saturation line chart
        oxygen_figure.add_trace(

            go.Scatter(
                x=times,
                y=oxygen_values,
                mode="lines+markers",
                name="Oxygen Saturation"
            )

        )

        oxygen_figure.update_layout(
            title="Oxygen Saturation Over Time",
            xaxis_title="Recorded Time",
            yaxis_title="Oxygen Saturation (%)"
        )


        # Creating the temperature line chart
        temperature_figure.add_trace(

            go.Scatter(
                x=times,
                y=temperatures,
                mode="lines+markers",
                name="Temperature"
            )

        )

        temperature_figure.update_layout(
            title="Temperature Over Time",
            xaxis_title="Recorded Time",
            yaxis_title="Temperature (°F)"
        )


        # Creating the blood-pressure line chart
        blood_pressure_figure.add_trace(

            go.Scatter(
                x=times,
                y=systolic_values,
                mode="lines+markers",
                name="Systolic BP"
            )

        )

        blood_pressure_figure.add_trace(

            go.Scatter(
                x=times,
                y=diastolic_values,
                mode="lines+markers",
                name="Diastolic BP"
            )

        )

        blood_pressure_figure.update_layout(
            title="Blood Pressure Over Time",
            xaxis_title="Recorded Time",
            yaxis_title="Blood Pressure (mmHg)"
        )


    # Creating risk information
    if risks:

        latest_risk = risks[-1]

        risk_score = latest_risk.get(
            "risk_score",
            0
        )

        risk_information = html.Div(

            [

                html.P(
                    f"Risk Score: {risk_score}"
                ),

                html.P(
                    f"Risk Level: "
                    f"{latest_risk.get('risk_level', 'N/A')}"
                ),

                html.P(
                    f"Assessment Method: "
                    f"{latest_risk.get('assessment_method', 'N/A')}"
                ),

                html.P(
                    f"Explanation: "
                    f"{latest_risk.get('explanation', 'N/A')}"
                )

            ]
        )

    else:

        risk_score = 0

        risk_information = html.P(
            "No risk assessment available."
        )


    # Creating the current risk gauge
    risk_figure = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=risk_score,

            title={
                "text": "Current Risk Score"
            },

            gauge={
                "axis": {
                    "range": [0, 100]
                },

                "steps": [

                    {
                        "range": [0, 30]
                    },

                    {
                        "range": [30, 60]
                    },

                    {
                        "range": [60, 100]
                    }

                ]

            }

        )

    )


    # Creating risk history chart
    if risks:

        risk_times = [
            risk.get("assessed_at", "")
            for risk in risks
        ]

        risk_scores = [
            risk.get("risk_score", 0)
            for risk in risks
        ]

        risk_history_figure.add_trace(

            go.Scatter(
                x=risk_times,
                y=risk_scores,
                mode="lines+markers",
                name="Risk Score"
            )

        )

        risk_history_figure.update_layout(
            title="Risk Score History",
            xaxis_title="Assessment Time",
            yaxis_title="Risk Score",
            yaxis=dict(
                range=[0, 100]
            )
        )


    # Creating activity information
    if activities:

        activity_information = [

            html.P(
                f"{activity.get('activity_type', 'N/A')} - "
                f"{activity.get('duration_minutes', 'N/A')} minutes - "
                f"{activity.get('calories_burned', 'N/A')} calories"
            )

            for activity in activities[-5:]

        ]

        # Extracting activity values
        activity_names = [
            activity.get("activity_type", "Unknown")
            for activity in activities
        ]

        activity_duration = [
            activity.get("duration_minutes", 0)
            for activity in activities
        ]

        # Creating activity chart
        activity_figure.add_trace(

            go.Bar(
                x=activity_names,
                y=activity_duration,
                name="Duration"
            )

        )

        activity_figure.update_layout(
            title="Activity Duration",
            xaxis_title="Activity",
            yaxis_title="Duration (minutes)"
        )

    else:

        activity_information = html.P(
            "No activities available."
        )


    # Creating alert information
    if alerts:

        alert_information = [

            html.P(
                f"{alert.get('alert_type', 'N/A')} | "
                f"Severity: "
                f"{alert.get('severity', 'N/A')} | "
                f"Status: "
                f"{alert.get('status', 'N/A')} | "
                f"{alert.get('message', '')}"
            )

            for alert in alerts[-10:]

        ]

    else:

        alert_information = html.P(
            "No alerts available."
        )


    # Returning all dashboard components
    return (

        patient_information,

        vital_information,

        heart_rate_figure,

        oxygen_figure,

        temperature_figure,

        blood_pressure_figure,

        risk_information,

        risk_figure,

        risk_history_figure,

        activity_information,

        activity_figure,

        alert_information

    )


# Starting the dashboard server
if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=8050,
        debug=True
    )