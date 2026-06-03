import od

class Config:
    SECRET_KEY = "bikehelpsecret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database/bike_help.db"
    SQLALCHEMY_TRACK_MODYFICATIONS = False
    JWT_SECRET_KEY = "jwtsecret0"