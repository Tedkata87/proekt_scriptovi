from app import app
from extensions import db
from models.bike import Bike

with app.app_context():

    bikes = [

        Bike(
            name="Trek Fuel EX 5",
            brand="Trek",
            terrain="trail",
            bike_type="Trail",
            price=1500,
            condition="new",
            description="130mm Trail Bike"
        ),

        Bike(
            name="YT Capra Core 4",
            brand="YT",
            terrain="enduro",
            bike_type="Enduro",
            price=2500,
            condition="new",
            description="160mm Enduro Bike"
        ),

        Bike(
            name="Commencal Supreme DH",
            brand="Commencal",
            terrain="downhill",
            bike_type="Downhill",
            price=1750,
            condition="new",
            description="DH Race Bike"
        ),

        Bike(
            name="Used Trek Remedy 8",
            brand="Trek",
            terrain="trail",
            bike_type="Trail",
            price=900,
            condition="used",
            description="Second hand bike"
        )
    ]

    db.session.add_all(bikes)
    db.session.commit()

    print("Bikes added.")