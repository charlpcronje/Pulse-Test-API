# Pulse Test API

The Pulse Test API is a comprehensive Flask-based backend designed for managing user authentication and sending push notifications via Firebase. It's built with extensibility and security in mind, ensuring seamless integration with front-end applications and services.

## Features

- **User Management**: Supports user registration and login with password hashing for security.
- **Token Authentication**: Utilizes JSON Web Tokens (JWT) to manage user sessions and secure API access.
- **Push Notifications**: Integrates Firebase Cloud Messaging (FCM) for sending notifications to users' devices.
- **Data Persistence**: Leverages SQLAlchemy ORM for robust database interactions and migrations support with Flask-Migrate.

## Project Structure

- **app/__init__.py**: Initializes the Flask application, registers blueprints, and sets up extensions like SQLAlchemy and Flask-Migrate.
- **app/config/config.py**: Contains configuration settings loaded from environment variables for flexibility across different deployment environments.
- **app/models**: Defines SQLAlchemy models for users and devices, enabling data persistence.
- **app/services**: Includes services for authentication and interacting with Firebase for notifications.
- **app/api**: Houses the Flask blueprints defining the API endpoints for user management and notification sending.

## Dependencies

- **Flask**: Micro web framework for Python, providing the scaffolding for web applications.
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy.
- **Flask-Migrate**: Handles SQLAlchemy database migrations for Flask applications as an Alembic wrapper.
- **python-dotenv**: Reads key-value pairs from a `.env` file and can set them as environment variables.
- **firebase-admin**: The official Firebase Admin SDK for accessing Firebase services server-side.
- **Werkzeug**: A WSGI utility library for Python, utilized here for password hashing.
- **itsdangerous**: Safely pass data to untrusted environments and back, used for token generation.

## Configuration (.env File)

Create a `.env` file in the project root with the following variables:

```
SECRET_KEY=your_flask_secret_key
DATABASE_URL=mysql+pymysql://username:password@localhost/database_name
FIREBASE_CONFIG_FILE=path/to/firebase_config.json
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000
```

- `SECRET_KEY`: A secret key for Flask application sessions and signing.
- `DATABASE_URL`: Database connection URL.
- `FIREBASE_CONFIG_FILE`: Path to the Firebase admin SDK JSON file.
- `FLASK_RUN_HOST` & `FLASK_RUN_PORT`: Configure the host and port for the Flask server.

## API Endpoints and Usage

**Register User**

- **POST** `/api/user/register`
- **Body**:
  ```json
  {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securePassword123"
  }
  ```
- **Response**: A message indicating successful registration.

**Login User**

- **POST** `/api/user/login`
- **Body**:
  ```json
  {
    "email": "john@example.com",
    "password": "securePassword123"
  }
  ```
- **Response**: A JSON Web Token for authenticated access to protected endpoints.

**Send Notification**

- **POST** `/api/notification/send_notification`
- **Headers**: Authorization: Bearer <your_jwt_token>
- **Body**:
  ```json
  {
    "user_id": 1,
    "title": "Hello",
    "body": "Your notification content here."
  }
  ```
- **Response**: Confirmation that the notification was sent.

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone git@github.com:charlpcronje/Pulse-Test-API.git
   cd Pulse-Test-API
   ```

2. **Set Up the Environment**
   - Follow the installation and configuration steps outlined above.

3. **Run the Application**
   ```bash
   python run.py
   ```

## Authors

- **Charl P. Cronje** - [GitHub](https://github.com/charlpcronje)