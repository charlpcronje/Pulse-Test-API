# /app/config/config.py-1-A+
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration class that loads settings from environment variables and
    contains configurations like database URI, Firebase API keys, and other
    application settings.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://user:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FIREBASE_CONFIG_FILE = os.environ.get('FIREBASE_CONFIG_FILE') or 'path/to/firebase_config.json'
