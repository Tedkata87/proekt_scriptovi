import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = "bike_help_secret"

    JWT_SECRET_KEY = "bike_help_jwt_secret"

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///database/bike_help.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )