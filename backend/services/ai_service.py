def generate_bike_recommendation(data):

    budget = data["budget"]

    terrain = data["terrain"]

    if terrain == "trail":

        if budget < 1500:

            return [
                {
                    "brand": "Trek",
                    "model": "Fuel EX 7",
                    "condition": "used"
                },
                {
                    "brand": "Specialized",
                    "model": "Stumpjumper",
                    "condition": "used"
                }
            ]

        return [
            {
                "brand": "YT",
                "model": "Jeffsy Core 2",
                "condition": "new"
            }
        ]

    if terrain == "enduro":

        return [
            {
                "brand": "Santa Cruz",
                "model": "Nomad",
                "condition": (
                    "used"
                    if budget < 2500
                    else "new"
                )
            }
        ]

    if terrain == "downhill":

        return [
            {
                "brand": "Commencal",
                "model": "Supreme DH",
                "condition": (
                    "used"
                    if budget < 3000
                    else "new"
                )
            }
        ]

    return [
        {
            "brand": "Canyon",
            "model": "Spectral",
            "condition": "new"
        }
    ]