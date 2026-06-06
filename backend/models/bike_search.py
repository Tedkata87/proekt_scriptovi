from app import db

class BikeSearch(db.Model):
    __tablename__ = "bike_searches"

    id = db.Column(db.Integer, primary_key=True)

    height = db.Column(db.Integer, nullable=False)

    weight = db.Column(db.Integer, nullable=False)

    terrain = db.Column(db.String(50), nullable=False)

    budget = db.Column(db.Integer, nullable=False)

    preferences = db.Column(db.String(255))