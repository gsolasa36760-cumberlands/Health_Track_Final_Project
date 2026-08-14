"""
HealthTrack WebSocket Testing

This file is testing the HealthTrack WebSocket endpoint and
verifying that the FastAPI application can establish a real-time
WebSocket connection and exchange messages with a client.
"""

# Importing the WebSocket client library
import websocket


# Defining the WebSocket server address
WEBSOCKET_URL = "ws://127.0.0.1:8000/ws"


# Testing the WebSocket connection
def test_websocket_connection():

    # Creating a WebSocket connection
    connection = websocket.create_connection(
        WEBSOCKET_URL,
        timeout=5
    )

    # Sending a test HealthTrack message
    connection.send(
        "Test health monitoring update"
    )

    # Receiving the server response
    response = connection.recv()

    # Verifying the response
    assert response == (
        "HealthTrack update: "
        "Test health monitoring update"
    )

    # Closing the WebSocket connection
    connection.close()