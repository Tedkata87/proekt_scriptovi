class Config:

    SECRET_KEY = "bike_help_secret"

    JWT_SECRET_KEY = "bike_help_jwt_secret"

    SQLALCHEMY_DATABASE_URI = "sqlite:///bike_help.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
