# /app/services/auth_service.py-1-A+
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from flask import current_app
from ..models.user import User
from .. import db

class AuthService:
    """
    S-auth_service-1-A+: Provides authentication services for the application,
    including user registration, login, and generating/validating JSON Web Tokens.
    """
    def generate_token(self, user_id, expiration=3600):
        """
        Generates a JSON Web Token for a given user ID.
        
        Args:
            user_id (int): The user's ID for whom to generate the token.
            expiration (int): The expiration time of the token in seconds.
            
        Returns:
            str: A JSON Web Token.
        """
        s = Serializer(secret_key=current_app.config['SECRET_KEY'], salt="some_salt")
        return s.dumps({'user_id': user_id})

    def verify_token(self, token):
        """
        Verifies a JSON Web Token and returns the user if valid.
        
        Args:
            token (str): The JSON Web Token to verify.
            
        Returns:
            User: The user associated with the token, or None if invalid.
        """
        s = Serializer(secret_key=current_app.config['SECRET_KEY'], salt="some_salt")
        try:
            data = s.loads(token, max_age=expiration)
            return data['user_id']
        except:
            return None

    def register_user(self, username, email, password):
        """
        Registers a new user with the given username, email, and password.
        
        Args:
            username (str): The user's username.
            email (str): The user's email.
            password (str): The user's password.
            
        Returns:
            User: The registered user.
        """
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    def authenticate_user(self, email, password):
        """
        Authenticates a user by their email and password.
        
        Args:
            email (str): The user's email.
            password (str): The user's password.
            
        Returns:
            bool: True if authentication is successful, otherwise False.
        """
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return True
        return False
