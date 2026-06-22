from datetime import datetime

from extensions import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(50),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    bike_searches = db.relationship(
        "BikeSearch",
        backref="user",
        cascade="all, delete"
    )

    bike_setups = db.relationship(
        "BikeSetup",
        backref="user",
        cascade="all, delete"
    )

    def to_dict(self):

        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": str(self.created_at)
        }