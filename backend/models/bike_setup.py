from datetime import datetime

from app import db


class BikeSetup(db.Model):

    __tablename__ = "bike_setups"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    rider_height = db.Column(
        db.Integer,
        nullable=False
    )

    rider_weight = db.Column(
        db.Integer,
        nullable=False
    )

    terrain = db.Column(
        db.String(50),
        nullable=False
    )

    bike_type = db.Column(
        db.String(50),
        nullable=False
    )

    brand = db.Column(
        db.String(100),
        nullable=False
    )

    model = db.Column(
        db.String(100),
        nullable=False
    )

    fork = db.Column(
        db.String(120)
    )

    shock = db.Column(
        db.String(120)
    )

    frame_size = db.Column(
        db.String(30)
    )

    wheel_size = db.Column(
        db.String(30)
    )

    drivetrain = db.Column(
        db.String(120)
    )

    brakes = db.Column(
        db.String(120)
    )

    handlebars = db.Column(
        db.String(120)
    )

    ai_result = db.Column(
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
            "rider_height": self.rider_height,
            "rider_weight": self.rider_weight,
            "terrain": self.terrain,
            "bike_type": self.bike_type,
            "brand": self.brand,
            "model": self.model,
            "fork": self.fork,
            "shock": self.shock,
            "frame_size": self.frame_size,
            "wheel_size": self.wheel_size,
            "drivetrain": self.drivetrain,
            "brakes": self.brakes,
            "handlebars": self.handlebars,
            "ai_result": self.ai_result,
            "created_at": str(self.created_at)
        }