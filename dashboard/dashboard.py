"""
HealthTrack Real-Time Patient Monitoring Dashboard

This dashboard is connecting to the HealthTrack FastAPI backend,
retrieving patient information, vital signs, activities, alerts,
and risk assessments, while displaying current and historical
health information through interactive Plotly charts and
maintaining a WebSocket connection for real-time communication.
"""


# =========================================================
# IMPORTING REQUIRED LIBRARIES
# =========================================================

# Importing Dash components for creating the dashboard
from dash import Dash, html, dcc, Input, Output

# Importing Plotly graph objects for creating interactive charts
import plotly.graph_objects as go

# Importing requests for communicating with FastAPI REST endpoints
import requests

# Importing WebSocket client for checking real-time communication
import websocket


# =========================================================
# CONFIGURING BACKEND CONNECTIONS
# =========================================================

# Defining the FastAPI backend address
API_URL = "http://127.0.0.1:8000"

# Defining the HealthTrack WebSocket address
WEBSOCKET_URL = "ws://127.0.0.1:8000/ws"


# =========================================================
# CREATING DASH APPLICATION
# =========================================================

# Creating the Dash application
app = Dash(__name__)

# Defining the browser page title
app.title = "HealthTrack Dashboard"


# =========================================================
# CREATING API HELPER FUNCTIONS
# =========================================================

# Creating a function for retrieving patient information
def get_patient(patient_id):

    try:

        # Sending a GET request for patient information
        response = requests.get(
            f"{API_URL}/patients/{patient_id}",
            timeout=5
        )

        # Checking whether the request is successful
        if response.status_code == 200:
            return response.json()

    except requests.RequestException:

        # Handling backend connection errors
        pass

    # Returning an empty result when patient information is unavailable
    return None


# Creating a function for retrieving patient vital signs
def get_vitals(patient_id):

    try:

        # Sending a GET request for patient vital signs
        response = requests.get(
            f"{API_URL}/vitals/patient/{patient_id}",
            timeout=5
        )

        # Checking whether the request is successful
        if response.status_code == 200:
            return response.json()

    except requests.RequestException:

        # Handling backend connection errors
        pass

    # Returning an empty list when vital information is unavailable
    return []


# Creating a function for retrieving patient activities
def get_activities(patient_id):

    try:

        # Sending a GET request for patient activities
        response = requests.get(
            f"{API_URL}/activities/patient/{patient_id}",
            timeout=5
        )

        # Checking whether the request is successful
        if response.status_code == 200:
            return response.json()

    except requests.RequestException:

        # Handling backend connection errors
        pass

    # Returning an empty list when activities are unavailable
    return []


# Creating a function for retrieving patient risk assessments
def get_risk(patient_id):

    try:

        # Sending a GET request for risk assessments
        response = requests.get(
            f"{API_URL}/risk/patient/{patient_id}",
            timeout=5
        )

        # Checking whether the request is successful
        if response.status_code == 200:
            return response.json()

    except requests.RequestException:

        # Handling backend connection errors
        pass

    # Returning an empty list when risk information is unavailable
    return []


# Creating a function for retrieving patient alerts
def get_alerts(patient_id):

    try:

        # Sending a GET request for patient alerts
        response = requests.get(
            f"{API_URL}/alerts/patient/{patient_id}",
            timeout=5
        )

        # Checking whether the request is successful
        if response.status_code == 200:
            return response.json()

    except requests.RequestException:

        # Handling backend connection errors
        pass

    # Returning an empty list when alert information is unavailable
    return []


# =========================================================
# CREATING WEBSOCKET CONNECTION CHECK
# =========================================================

# Creating a function for checking WebSocket availability
def check_websocket_connection():

    try:

        # Creating a temporary WebSocket connection
        connection = websocket.create_connection(
            WEBSOCKET_URL,
            timeout=2
        )

        # Closing the temporary WebSocket connection
        connection.close()

        # Returning the connected status
        return "Connected"

    except Exception:

        # Returning the disconnected status
        return "Disconnected"


# =========================================================
# CREATING EMPTY CHART FUNCTIONS
# =========================================================

# Creating a function for creating an empty chart
def create_empty_chart(title, y_axis_title):

    # Creating an empty Plotly figure
    figure = go.Figure()

    # Adding a message when data is unavailable
    figure.add_annotation(
        text="No data available",
        x=0.5,
        y=0.5,
        xref="paper",
        yref="paper",
        showarrow=False
    )

    # Configuring the chart layout
    figure.update_layout(
        title=title,
        xaxis_title="Reading",
        yaxis_title=y_axis_title
    )

    # Returning the empty figure
    return figure


# =========================================================
# CREATING DASHBOARD LAYOUT
# =========================================================

# Defining the complete dashboard interface
app.layout = html.Div(

    [

        # Creating the dashboard title
        html.H1(
            "HealthTrack Patient Monitoring Dashboard",
            style={
                "textAlign": "center",
                "marginBottom": "10px"
            }
        ),

        # Creating the WebSocket status indicator
        html.Div(
            id="websocket-status",
            children="Real-Time Connection: Checking...",
            style={
                "textAlign": "center",
                "fontWeight": "bold",
                "marginBottom": "20px"
            }
        ),

        # Creating the patient ID input section
        html.Div(

            [

                # Creating the patient ID label
                html.Label(
                    "Patient ID:",
                    style={
                        "fontWeight": "bold",
                        "marginRight": "10px"
                    }
                ),

                # Creating the patient ID input
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

        # =================================================
        # PATIENT INFORMATION
        # =================================================

        html.Div(

            [

                # Creating the patient information heading
                html.H2("Patient Information"),

                # Creating the patient information container
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

        # =================================================
        # LATEST VITAL SIGNS
        # =================================================

        html.Div(

            [

                # Creating the latest vital-sign heading
                html.H2("Latest Vital Signs"),

                # Creating the latest vital-sign container
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

        # =================================================
        # VITAL SIGNS HISTORY
        # =================================================

        html.Div(

            [

                # Creating the vital history heading
                html.H2("Vital Signs History"),

                # Creating the heart-rate graph
                dcc.Graph(
                    id="heart-rate-chart"
                ),

                # Creating the oxygen-saturation graph
                dcc.Graph(
                    id="oxygen-chart"
                ),

                # Creating the temperature graph
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

        # =================================================
        # RISK ASSESSMENT
        # =================================================

        html.Div(

            [

                # Creating the risk assessment heading
                html.H2("Risk Assessment"),

                # Creating the risk information container
                html.Div(
                    id="risk-information"
                ),

                # Creating the current risk gauge
                dcc.Graph(
                    id="risk-chart"
                )

            ],

            style={
                "padding": "20px",
                "marginBottom": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "8px"
            }
        ),

        # =================================================
        # RISK HISTORY
        # =================================================

        html.Div(

            [

                # Creating the risk history heading
                html.H2("Risk Score History"),

                # Creating the risk history line chart
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

        # =================================================
        # ACTIVITY INFORMATION
        # =================================================

        html.Div(

            [

                # Creating the activity heading
                html.H2("Recent Activities"),

                # Creating the activity information container
                html.Div(
                    id="activity-information"
                )

            ],

            style={
                "padding": "20px",
                "marginBottom": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "8px"
            }
        ),

        # =================================================
        # ALERT INFORMATION
        # =================================================

        html.Div(

            [

                # Creating the alert heading
                html.H2("Alerts"),

                # Creating the alert information container
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


# =========================================================
# CREATING DASHBOARD CALLBACK
# =========================================================

# Updating all dashboard information automatically
@app.callback(

    [

        # Updating patient information
        Output(
            "patient-information",
            "children"
        ),

        # Updating latest vital information
        Output(
            "vital-information",
            "children"
        ),

        # Updating risk information
        Output(
            "risk-information",
            "children"
        ),

        # Updating current risk gauge
        Output(
            "risk-chart",
            "figure"
        ),

        # Updating heart-rate graph
        Output(
            "heart-rate-chart",
            "figure"
        ),

        # Updating oxygen graph
        Output(
            "oxygen-chart",
            "figure"
        ),

        # Updating temperature graph
        Output(
            "temperature-chart",
            "figure"
        ),

        # Updating risk history graph
        Output(
            "risk-history-chart",
            "figure"
        ),

        # Updating activity information
        Output(
            "activity-information",
            "children"
        ),

        # Updating alert information
        Output(
            "alert-information",
            "children"
        ),

        # Updating WebSocket status
        Output(
            "websocket-status",
            "children"
        )

    ],

    [

        # Updating when patient ID is changed
        Input(
            "patient-id",
            "value"
        ),

        # Updating automatically according to interval
        Input(
            "refresh-interval",
            "n_intervals"
        )

    ]
)


# =========================================================
# DEFINING DASHBOARD UPDATE FUNCTION
# =========================================================

# Defining the function for updating dashboard information
def update_dashboard(
    patient_id,
    n_intervals
):

    # Handling a missing patient ID
    if not patient_id:
        patient_id = 1

    # Retrieving patient information
    patient = get_patient(patient_id)

    # Retrieving vital-sign records
    vitals = get_vitals(patient_id)

    # Retrieving risk assessments
    risks = get_risk(patient_id)

    # Retrieving activity records
    activities = get_activities(patient_id)

    # Retrieving alert records
    alerts = get_alerts(patient_id)

    # Checking WebSocket connection
    websocket_connection = check_websocket_connection()


    # =====================================================
    # CREATING PATIENT INFORMATION
    # =====================================================

    # Checking whether patient information is available
    if patient:

        # Creating patient information elements
        patient_information = html.Div(

            [

                html.P(
                    f"Patient ID: "
                    f"{patient.get('patient_id', patient.get('id', 'N/A'))}"
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

        # Displaying a message when patient information is unavailable
        patient_information = html.P(
            "Patient information could not be retrieved."
        )


    # =====================================================
    # CREATING LATEST VITAL INFORMATION
    # =====================================================

    # Checking whether vital records are available
    if vitals:

        # Retrieving the latest vital-sign record
        latest_vital = vitals[-1]

        # Creating latest vital-sign information
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

        # Displaying a message when vital records are unavailable
        vital_information = html.P(
            "No vital signs available."
        )


    # =====================================================
    # CREATING HEART-RATE HISTORY GRAPH
    # =====================================================

    # Creating the heart-rate figure
    heart_rate_figure = go.Figure()

    # Checking whether vital records are available
    if vitals:

        # Extracting heart-rate values
        heart_rate_values = [

            vital.get("heart_rate")

            for vital in vitals

            if vital.get("heart_rate") is not None

        ]

        # Creating the heart-rate line
        if heart_rate_values:

            heart_rate_figure.add_trace(

                go.Scatter(

                    x=list(
                        range(
                            1,
                            len(heart_rate_values) + 1
                        )
                    ),

                    y=heart_rate_values,

                    mode="lines+markers",

                    name="Heart Rate"

                )

            )

    # Configuring the heart-rate chart
    heart_rate_figure.update_layout(

        title="Heart Rate History",

        xaxis_title="Reading",

        yaxis_title="Heart Rate (bpm)"

    )


    # =====================================================
    # CREATING OXYGEN HISTORY GRAPH
    # =====================================================

    # Creating the oxygen-saturation figure
    oxygen_figure = go.Figure()

    # Checking whether vital records are available
    if vitals:

        # Extracting oxygen-saturation values
        oxygen_values = [

            vital.get("oxygen_saturation")

            for vital in vitals

            if vital.get("oxygen_saturation") is not None

        ]

        # Creating the oxygen-saturation line
        if oxygen_values:

            oxygen_figure.add_trace(

                go.Scatter(

                    x=list(
                        range(
                            1,
                            len(oxygen_values) + 1
                        )
                    ),

                    y=oxygen_values,

                    mode="lines+markers",

                    name="Oxygen Saturation"

                )

            )

    # Configuring the oxygen chart
    oxygen_figure.update_layout(

        title="Oxygen Saturation History",

        xaxis_title="Reading",

        yaxis_title="Oxygen Saturation (%)"

    )


    # =====================================================
    # CREATING TEMPERATURE HISTORY GRAPH
    # =====================================================

    # Creating the temperature figure
    temperature_figure = go.Figure()

    # Checking whether vital records are available
    if vitals:

        # Extracting temperature values
        temperature_values = [

            vital.get("temperature")

            for vital in vitals

            if vital.get("temperature") is not None

        ]

        # Creating the temperature line
        if temperature_values:

            temperature_figure.add_trace(

                go.Scatter(

                    x=list(
                        range(
                            1,
                            len(temperature_values) + 1
                        )
                    ),

                    y=temperature_values,

                    mode="lines+markers",

                    name="Temperature"

                )

            )

    # Configuring the temperature chart
    temperature_figure.update_layout(

        title="Temperature History",

        xaxis_title="Reading",

        yaxis_title="Temperature (°F)"

    )


    # =====================================================
    # CREATING RISK INFORMATION
    # =====================================================

    # Initializing the risk score
    risk_score = 0

    # Checking whether risk assessments are available
    if risks:

        # Retrieving the latest risk assessment
        latest_risk = risks[-1]

        # Retrieving the latest risk score
        risk_score = latest_risk.get(
            "risk_score",
            0
        )

        # Creating risk information
        risk_information = html.Div(

            [

                html.P(
                    f"Risk Score: "
                    f"{risk_score}"
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

        # Displaying a message when risk information is unavailable
        risk_information = html.P(
            "No risk assessment available."
        )


    # =====================================================
    # CREATING CURRENT RISK GAUGE
    # =====================================================

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


    # =====================================================
    # CREATING RISK HISTORY GRAPH
    # =====================================================

    # Creating the risk-history figure
    risk_history_figure = go.Figure()

    # Checking whether risk records are available
    if risks:

        # Extracting risk-score values
        risk_values = [

            risk.get("risk_score")

            for risk in risks

            if risk.get("risk_score") is not None

        ]

        # Creating the risk-score line
        if risk_values:

            risk_history_figure.add_trace(

                go.Scatter(

                    x=list(
                        range(
                            1,
                            len(risk_values) + 1
                        )
                    ),

                    y=risk_values,

                    mode="lines+markers",

                    name="Risk Score"

                )

            )

    # Configuring the risk-history chart
    risk_history_figure.update_layout(

        title="Risk Score History",

        xaxis_title="Assessment",

        yaxis_title="Risk Score",

        yaxis={
            "range": [0, 100]
        }

    )


    # =====================================================
    # CREATING ACTIVITY INFORMATION
    # =====================================================

    # Checking whether activity records are available
    if activities:

        # Creating recent activity elements
        activity_information = [

            html.P(

                f"{activity.get('activity_type', 'N/A')} - "

                f"{activity.get('duration_minutes', 'N/A')} minutes - "

                f"{activity.get('calories_burned', 'N/A')} calories"

            )

            for activity in activities[-5:]

        ]

    else:

        # Displaying a message when activities are unavailable
        activity_information = html.P(
            "No activities available."
        )


    # =====================================================
    # CREATING ALERT INFORMATION
    # =====================================================

    # Checking whether alerts are available
    if alerts:

        # Creating recent alert elements
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

        # Displaying a message when alerts are unavailable
        alert_information = html.P(
            "No alerts available."
        )


    # =====================================================
    # CREATING WEBSOCKET STATUS
    # =====================================================

    # Creating the WebSocket status message
    websocket_status = (
        f"Real-Time Connection: "
        f"{websocket_connection}"
    )


    # =====================================================
    # RETURNING DASHBOARD RESULTS
    # =====================================================

    # Returning all dashboard components
    return (

        patient_information,

        vital_information,

        risk_information,

        risk_figure,

        heart_rate_figure,

        oxygen_figure,

        temperature_figure,

        risk_history_figure,

        activity_information,

        alert_information,

        websocket_status

    )


# =========================================================
# RUNNING DASHBOARD APPLICATION
# =========================================================

# Starting the Dash development server
if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=8050,

        debug=True

    )