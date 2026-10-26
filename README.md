# Broadcast Server
https://roadmap.sh/projects/broadcast-server  
A real-time WebSocket broadcast server with Django Channels, Redis and Daphne that lets users to connect and send messages that are broadcasted to all connected users.

## Tech Stack
- Python
- Django
- Django Channels
- Redis
- Daphne

## Features
- Real-time WebSocket communication
- Message broadcasting
- Redis-backed channel layer
- Graceful shutdown notifications

### Prerequisites
Python 3.12+  
Redis

### Installation
Clone the repository:  
>bash: `git clone https://github.com/Alexx720p/broadcast_server.git`  
>bash: `cd broadcast_server`

### Install dependencies  
>bash: `pip install -r requirements.txt`

### Running the server
*Start Redis before running the app (a Docker Redis image can be used for that purpose)*  
*Ensure port 6379 is available and that the application configuration points to the correct Redis host and port*

Then:  
>Bash: `daphne broadcast_server.asgi:application`

**WebSocket endpoint to connect:**
ws://localhost:8000/ws/chat/

**To send a message:**  
>JSON: {"message": "Hello everyone"}  

### Server shutdown notification
Broadcasts a shutdown notification to all connected users before the server stops  
>Bash: `python manage.py utils`


## Architecture
Client -> Daphne (ASGI Server) -> Django Channels -> Chat Consumer -> Redis Channel Layer (Broadcasting messaging) -> Redis Client (connection tracking and metadata)
