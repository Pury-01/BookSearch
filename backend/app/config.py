import os
import secrets
"""
configuration file
"""


class Config:
    """
    configuration class
    """
    # secret key to secure session data
    SECRET_KEY = secrets.token_urlsafe(16)

    # Database configuration
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
