"""
HealthTrack Dashboard Plotting Module

Creating reusable Plotly graphs for displaying HealthTrack patient
vital signs, activities, risk assessments, and alerts. Connecting
dashboard visualizations with data retrieved from the FastAPI backend.
"""


# Importing Plotly graph objects
import plotly.graph_objects as go


# Creating a heart-rate line chart
def create_heart_rate_chart(vitals):

    # Creating an empty figure
    figure = go.Figure()

    # Checking whether vital-sign data is available
    if not vitals:

        # Displaying an empty-state message
        figure.add_annotation(
            text="No heart-rate data available",
            x=0.5,
            y=0.5,
            showarrow=False
        )

        return figure

    # Extracting recorded times
    times = [
        vital.get("recorded_at")
        for vital in vitals
    ]

    # Extracting heart-rate values
    heart_rates = [
        vital.get("heart_rate")
        for vital in vitals
    ]

    # Adding the heart-rate line
    figure.add_trace(
        go.Scatter(
            x=times,
            y=heart_rates,
            mode="lines+markers",
            name="Heart Rate"
        )
    )

    # Configuring the chart title
    figure.update_layout(
        title="Heart Rate Over Time",
        xaxis_title="Recorded Time",
        yaxis_title="Heart Rate (BPM)"
    )

    return figure


# Creating an oxygen-saturation line chart
def create_oxygen_chart(vitals):

    # Creating an empty figure
    figure = go.Figure()

    # Checking whether vital-sign data is available
    if not vitals:

        # Displaying an empty-state message
        figure.add_annotation(
            text="No oxygen-saturation data available",
            x=0.5,
            y=0.5,
            showarrow=False
        )

        return figure

    # Extracting recorded times
    times = [
        vital.get("recorded_at")
        for vital in vitals
    ]

    # Extracting oxygen-saturation values
    oxygen_values = [
        vital.get("oxygen_saturation")
        for vital in vitals
    ]

    # Adding the oxygen-saturation line
    figure.add_trace(
        go.Scatter(
            x=times,
            y=oxygen_values,
            mode="lines+markers",
            name="Oxygen Saturation"
        )
    )

    # Configuring the chart
    figure.update_layout(
        title="Oxygen Saturation Over Time",
        xaxis_title="Recorded Time",
        yaxis_title="Oxygen Saturation (%)"
    )

    return figure


# Creating a blood-pressure line chart
def create_blood_pressure_chart(vitals):

    # Creating an empty figure
    figure = go.Figure()

    # Checking whether vital-sign data is available
    if not vitals:

        # Displaying an empty-state message
        figure.add_annotation(
            text="No blood-pressure data available",
            x=0.5,
            y=0.5,
            showarrow=False
        )

        return figure

    # Extracting recorded times
    times = [
        vital.get("recorded_at")
        for vital in vitals
    ]

    # Extracting systolic values
    systolic = [
        vital.get("systolic_bp")
        for vital in vitals
    ]

    # Extracting diastolic values
    diastolic = [
        vital.get("diastolic_bp")
        for vital in vitals
    ]

    # Adding the systolic-pressure line
    figure.add_trace(
        go.Scatter(
            x=times,
            y=systolic,
            mode="lines+markers",
            name="Systolic"
        )
    )

    # Adding the diastolic-pressure line
    figure.add_trace(
        go.Scatter(
            x=times,
            y=diastolic,
            mode="lines+markers",
            name="Diastolic"
        )
    )

    # Configuring the chart
    figure.update_layout(
        title="Blood Pressure Over Time",
        xaxis_title="Recorded Time",
        yaxis_title="Blood Pressure (mmHg)"
    )

    return figure


# Creating an activity-duration chart
def create_activity_chart(activities):

    # Creating an empty figure
    figure = go.Figure()

    # Checking whether activity data is available
    if not activities:

        # Displaying an empty-state message
        figure.add_annotation(
            text="No activity data available",
            x=0.5,
            y=0.5,
            showarrow=False
        )

        return figure

    # Extracting activity names
    activity_types = [
        activity.get("activity_type")
        for activity in activities
    ]

    # Extracting activity durations
    durations = [
        activity.get("duration_minutes", 0)
        for activity in activities
    ]

    # Adding the activity bars
    figure.add_trace(
        go.Bar(
            x=activity_types,
            y=durations,
            name="Activity Duration"
        )
    )

    # Configuring the chart
    figure.update_layout(
        title="Physical Activity Duration",
        xaxis_title="Activity",
        yaxis_title="Duration (Minutes)"
    )

    return figure


# Creating a risk-score line chart
def create_risk_chart(risk_assessments):

    # Creating an empty figure
    figure = go.Figure()

    # Checking whether risk data is available
    if not risk_assessments:

        # Displaying an empty-state message
        figure.add_annotation(
            text="No risk assessment data available",
            x=0.5,
            y=0.5,
            showarrow=False
        )

        return figure

    # Extracting assessment times
    times = [
        risk.get("assessed_at")
        for risk in risk_assessments
    ]

    # Extracting risk scores
    scores = [
        risk.get("risk_score", 0)
        for risk in risk_assessments
    ]

    # Adding the risk-score line
    figure.add_trace(
        go.Scatter(
            x=times,
            y=scores,
            mode="lines+markers",
            name="Risk Score"
        )
    )

    # Configuring the chart
    figure.update_layout(
        title="Health Risk Score Over Time",
        xaxis_title="Assessment Time",
        yaxis_title="Risk Score"
    )

    return figure