# /app/__init__.py
from flask import Flask
from .config.config import Config
# Removing the direct SQLAlchemy() initialization here since we'll import it from extensions.
from .extensions import db, migrate  # Assuming migrate is correctly initialized in extensions.py

def create_app():
    """
    Initialize the Flask application, configure it from the Config class,
    and initialize extensions like SQLAlchemy and Migrate.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize plugins with the app context
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register Blueprints here
    # Correcting the duplicated imports by removing the redundant lines
    from .api.user_api import user_api_blueprint
    from .api.notification_api import notification_api_blueprint

    # Register blueprints
    app.register_blueprint(user_api_blueprint, url_prefix='/api/user')
    app.register_blueprint(notification_api_blueprint, url_prefix='/api/notification')

    return app
