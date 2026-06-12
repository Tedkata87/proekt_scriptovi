from datetime import datetime

from app import db


class BikeSearch(db.Model):

    __tablename__ = "bike_searches"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    height = db.Column(
        db.Integer,
        nullable=False
    )

    weight = db.Column(
        db.Integer,
        nullable=False
    )

    terrain = db.Column(
        db.String(50),
        nullable=False
    )

    budget = db.Column(
        db.Integer,
        nullable=False
    )

    preferences = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):

        return {
            "id": self.id,
            "user_id": self.user_id,
            "height": self.height,
            "weight": self.weight,
            "terrain": self.terrain,
            "budget": self.budget,
            "preferences": self.preferences,
            "created_at": str(self.created_at)
        }