# /app/models/device.py
from app.extensions import db

class Device(db.Model):
    """
    M-device-1-A+: Represents a user's device in the database, storing device-specific
    information such as device ID, with a foreign key linking to the User model.
    """
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(200), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
