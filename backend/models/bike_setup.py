from app import db 

class BikeSetup(db.Model):
    __tablename__ = "bike_setups"

    id = db.Column(db.Integer, primary_key=True)

    bike_model = db.Column(db.String(100), nullable=False)

    fork = db.Column(db.String(100))

    shock = db.Column(db.String(100))

    frame_size = db.Column(db.String(50))
    
    wheel_size = db.Column(db.String(50))

    terrain = db.Column(db.String(50))