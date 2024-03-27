# /app/services/firebase_service.py-1-A+
import firebase_admin
from firebase_admin import credentials, messaging
from flask import current_app

class FirebaseService:
    """
    S-firebase_service-1-A+: Manages interactions with Firebase for sending push notifications.
    Initializes the Firebase app using the configuration file specified in the app's config.
    """
    def __init__(self):
        # self.initialize_firebase_app()
        pass

    def initialize_firebase_app(self):
        """
        Initializes the Firebase app with the credentials from the Firebase configuration file.
        """
        if not firebase_admin._apps:
            firebase_cred = credentials.Certificate(current_app.config['FIREBASE_CONFIG_FILE'])
            firebase_admin.initialize_app(firebase_cred)

    def send_notification(self, device_token, title, body):
        """
        Sends a push notification to a single device.
        
        Args:
            device_token (str): The token of the device to send the notification to.
            title (str): The title of the notification.
            body (str): The body content of the notification.
        """
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=device_token,
        )
        response = messaging.send(message)
        return response
