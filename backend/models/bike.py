from extensions import db

class Bike(db.Model):

    __tablename__ = "bikes"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200), nullable=False)

    brand = db.Column(db.String(100), nullable=False)

    terrain = db.Column(db.String(50), nullable=False)

    bike_type = db.Column(db.String(50), nullable=False)

    price = db.Column(db.Integer, nullable=False)

    condition = db.Column(db.String(20), nullable=False)

    description = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "brand": self.brand,
            "terrain": self.terrain,
            "bike_type": self.bike_type,
            "price": self.price,
            "condition": self.condition,
            "description": self.description
        }