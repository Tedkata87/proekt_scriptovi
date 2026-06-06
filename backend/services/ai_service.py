def generate_bike_recommendation(data):

     budget = data["budget"]

     terrain = data["terrain"]

     if budget < 1500:
        return {
            "recommendation": [
                {
                     "brand": "Specialized",
                     "model": "Status",
                     "condition": "used"
                }, 
                { 
                    "brand": "Trek", 
                    "model": "Remedy", 
                    "condition": "used"
                } 
            ]
        }

        return {
            "recommendation": [
                {
                    "brand": "Santa Cruz",
                    "model": "Nomad",
                    "condition": "new"
                }
            ]
        }

    def generate_setup(data):

        terrain = data["terrain"]
        if terrain == "downhill":
            return {
                "fork_pressure": "85 PSI",
                "shock_pressure": "175 PSI",
                "sag": "30%",
                "rebound": "medium"
            }

        return {
            "fork_pressure": "75 PSI",
            "shock_pressure": "160 PSI",
            "sag": "28%",
            "rebound": "fast"
        }