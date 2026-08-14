"""
HealthTrack WebSocket Configuration

This file is creating the HealthTrack WebSocket endpoint for
real-time communication between the FastAPI backend and dashboard.
The WebSocket connection is receiving patient updates and sending
real-time health monitoring messages to connected clients.
"""

# Importing FastAPI WebSocket components
from fastapi import APIRouter, WebSocket, WebSocketDisconnect


# Creating the WebSocket router
router = APIRouter()


# Creating a connection manager for active WebSocket clients
class ConnectionManager:

    # Initializing the active connection list
    def __init__(self):
        self.active_connections = []

    # Accepting a new WebSocket connection
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    # Removing a disconnected WebSocket client
    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    # Sending a message to one connected client
    async def send_message(
        self,
        message: str,
        websocket: WebSocket
    ):
        await websocket.send_text(message)

    # Broadcasting a message to all connected clients
    async def broadcast(self, message: str):

        for websocket in self.active_connections:

            try:
                await websocket.send_text(message)

            except Exception:
                self.disconnect(websocket)


# Creating the WebSocket connection manager
manager = ConnectionManager()


# Creating the HealthTrack WebSocket endpoint
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    # Accepting the WebSocket connection
    await manager.connect(websocket)

    try:

        # Keeping the WebSocket connection active
        while True:

            # Receiving a message from the client
            message = await websocket.receive_text()

            # Sending the received message to connected clients
            await manager.broadcast(
                f"HealthTrack update: {message}"
            )

    except WebSocketDisconnect:

        # Removing the disconnected client
        manager.disconnect(websocket)