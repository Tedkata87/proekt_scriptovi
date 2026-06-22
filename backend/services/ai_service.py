def generate_bike_recommendation(data):

    terrain = data.get("terrain")
    budget = data.get("budget")

    if budget <= 1000:
        bike = "Used Trek Remedy"
    elif terrain == "trail":
        bike = "Trek Fuel EX"
    elif terrain == "enduro":
        bike = "YT Capra"
    elif terrain == "downhill":
        bike = "Commencal Supreme DH"
    else:
        bike = "Canyon Spectral"

    return {
        "recommendation": f"Recommended bike: {bike}"
    }


def generate_setup(data):

    return {
        "recommendation": """
Fork Pressure: 80 PSI

Shock Pressure: 180 PSI

Sag: 28%

Rebound: Medium

Front Tire Pressure: 22 PSI

Rear Tire Pressure: 25 PSI
"""
    }