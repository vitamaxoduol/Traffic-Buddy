import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///traffic_buddy.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    API_KEY = os.environ.get("API_KEY")