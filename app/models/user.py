# /app/models/user.py-1-A+
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    """
    M-user-1-A+: Represents a user in the database with the fields id, username, email,
    password_hash, and a relationship to the Device model for storing device IDs.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    devices = db.relationship('Device', backref='owner', lazy='dynamic')

    def set_password(self, password):
        """
        Generates a hash for the provided password and stores it.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verifies the password against the stored hash.
        """
        return check_password_hash(self.password_hash, password)
