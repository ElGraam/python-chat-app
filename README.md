# Python Chat Room Application

This project implements a chat room application with separate server and client components using Python. It demonstrates the use of both TCP and UDP protocols, room management, and basic security features.

## Features

- Server-client architecture
- TCP for connection establishment and room management
- UDP for real-time message exchange
- Chat room creation and joining with password protection
- User management
- Token-based authentication
- Command-line interface with template-based views
- Multithreading for handling multiple client connections

## Project Structure

- `server.py`: Main server entry point
- `client.py`: Main client entry point
- `server/`: Server-side implementation
  - `models/`: Data models (chat rooms, users)
  - `views/`: Server view templates
  - `controller/`: Server logic
- `client/`: Client-side implementation
  - `models/`: Client data models
  - `views/`: Client view templates
  - `controller/`: Client logic
- `protocol/`: Network protocol implementations (TCP, UDP)

## Requirements

- Python 3.12+
- Additional dependencies listed in `poetry.lock`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/python-chat-app.git
   cd python-chat-app
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

## Usage

1. Start the server:
   ```
   python server.py
   ```

2. Run the client:
   ```
   python client.py
   ```

3. Follow the on-screen prompts to create or join a chat room.


