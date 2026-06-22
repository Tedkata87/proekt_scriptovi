from models.bike import Bike

def generate_bike_recommendation(data):

    terrain = data["terrain"]
    budget = data["budget"]

    bikes = Bike.query.filter(
        Bike.terrain == terrain,
        Bike.price <= budget
    ).all()

    return [
        bike.to_dict()
        for bike in bikes
    ]