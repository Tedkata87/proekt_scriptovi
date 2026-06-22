def generate_bike_recommendation(data):

    height = data.get("height")
    weight = data.get("weight")
    terrain = data.get("terrain")
    budget = data.get("budget")
    preferences = data.get("preferences", "")

    # Логика за препорака врз основа на параметри
    bikes = []

    # Според терен и бюджет
    if budget <= 1000:
        bikes = [
            {
                "name": "Used Trek Remedy 8",
                "price": "€800-1000",
                "type": "Trail Bike",
                "reason": "Добра опција за почетници со мал бюджет"
            },
            {
                "name": "Used Specialized Stumpjumper",
                "price": "€900-1100",
                "type": "Trail Bike",
                "reason": "Квалитетно употребено колело"
            }
        ]

    elif 1000 < budget <= 2000:
        if terrain == "trail":
            bikes = [
                {
                    "name": "Trek Fuel EX 5",
                    "price": "€1,500",
                    "type": "Trail Bike (130mm)",
                    "reason": "Идеално за trail каране со добра суспензија"
                },
                {
                    "name": "Specialized Stumpjumper Evo",
                    "price": "€1,800",
                    "type": "Trail Bike",
                    "reason": "Одлично за технички терен"
                }
            ]
        elif terrain == "enduro":
            bikes = [
                {
                    "name": "Trek Slash 7",
                    "price": "€1,700",
                    "type": "Enduro Bike (150mm)",
                    "reason": "Добра суспензија за агресивно каране"
                },
                {
                    "name": "Specialized Enduro Expert",
                    "price": "€1,900",
                    "type": "Enduro Bike",
                    "reason": "Напредна технологија за експертски пилоти"
                }
            ]
        elif terrain == "downhill":
            bikes = [
                {
                    "name": "Commencal Supreme DH",
                    "price": "€1,750",
                    "type": "Downhill Bike",
                    "reason": "Добро DH колело за средна цена"
                },
                {
                    "name": "Trek Session 8",
                    "price": "€1,850",
                    "type": "Downhill Bike",
                    "reason": "Солидно DH колело"
                }
            ]
        else:
            bikes = [
                {
                    "name": "Canyon Spectral CF 7",
                    "price": "€1,600",
                    "type": "All-Mountain",
                    "reason": "Универзално колело за разни терени"
                },
                {
                    "name": "Trek X-Caliber 9",
                    "price": "€1,899",
                    "type": "XC/Trail",
                    "reason": "Добро за фрирајд"
                }
            ]

    elif 2000 < budget <= 3500:
        if terrain == "enduro":
            bikes = [
                {
                    "name": "YT Capra Core 4",
                    "price": "€2,500",
                    "type": "Enduro Bike (160mm)",
                    "reason": "Професионално enduro колело"
                },
                {
                    "name": "Trek Remedy 9",
                    "price": "€2,800",
                    "type": "Trail Bike (160mm)",
                    "reason": "Напредна геометрија за технички терен"
                }
            ]
        elif terrain == "downhill":
            bikes = [
                {
                    "name": "Commencal Supreme DH 29",
                    "price": "€2,900",
                    "type": "Downhill Bike",
                    "reason": "Специјализирано за брзо спускање"
                },
                {
                    "name": "Trek Session 9.9",
                    "price": "€3,200",
                    "type": "Downhill Bike",
                    "reason": "Елитно DH колело со максимална контрола"
                }
            ]
        elif terrain == "trail":
            bikes = [
                {
                    "name": "Specialized Stumpjumper Expert",
                    "price": "€2,800",
                    "type": "Trail Bike",
                    "reason": "Топ trail колело од Specialized"
                },
                {
                    "name": "Trek Fuel EX 9.8",
                    "price": "€3,200",
                    "type": "Trail Bike (130mm)",
                    "reason": "Премиум trail колело"
                }
            ]
        else:
            bikes = [
                {
                    "name": "Santa Cruz Nomad 5",
                    "price": "€3,000",
                    "type": "Enduro/All-Mountain",
                    "reason": "Многу способно за различни услови"
                },
                {
                    "name": "Canyon Spectral CF 8",
                    "price": "€3,100",
                    "type": "All-Mountain",
                    "reason": "Напредно all-mountain колело"
                }
            ]

    else:  # budget > 3500
        if terrain == "downhill":
            bikes = [
                {
                    "name": "Santa Cruz V10 Carbon CC",
                    "price": "€4,500+",
                    "type": "Downhill Bike",
                    "reason": "Елитна DH опрема со карбонска рама"
                },
                {
                    "name": "Trek Session 9.9 XT",
                    "price": "€4,200+",
                    "type": "Downhill Bike",
                    "reason": "Топ модернизирано DH колело"
                }
            ]
        elif terrain == "enduro":
            bikes = [
                {
                    "name": "Specialized Enduro Expert Carbon",
                    "price": "€4,000+",
                    "type": "Enduro Bike Carbon",
                    "reason": "Карбонска рама со максимална производителност"
                },
                {
                    "name": "Commencal Meta AM 29 Elite",
                    "price": "€3,800+",
                    "type": "All-Mountain",
                    "reason": "Френско инженерство за екстремни услови"
                }
            ]
        elif terrain == "trail":
            bikes = [
                {
                    "name": "Trek Top Fuel 9.9",
                    "price": "€4,000+",
                    "type": "XC/Trail Bike Carbon",
                    "reason": "Лесно и брзо колело за напредни пилоти"
                },
                {
                    "name": "Specialized S-Works Epic",
                    "price": "€4,500+",
                    "type": "XC Trail Bike",
                    "reason": "Топ XC колело за競賽"
                }
            ]
        else:
            bikes = [
                {
                    "name": "Trek Supercaliber 9.8",
                    "price": "€4,200+",
                    "type": "XC Hardtail",
                    "reason": "Елитно XC колело"
                },
                {
                    "name": "Specialized S-Works Epic",
                    "price": "€4,500+",
                    "type": "XC Trail",
                    "reason": "Топ напредно колело"
                }
            ]

    # Додај совет врз основа на висина и тежина
    sizing_advice = get_sizing_advice(height, weight)

    return {
        "bikes": bikes,
        "sizing_advice": sizing_advice,
        "custom_notes": f"Твои преференции: {preferences}" if preferences else ""
    }


def get_sizing_advice(height, weight):
    """Дава совет за величина врз основа на височина и тежина"""

    frame_size = "M"
    
    if height < 160:
        frame_size = "XS"
    elif height < 170:
        frame_size = "S"
    elif height < 180:
        frame_size = "M"
    elif height < 190:
        frame_size = "L"
    else:
        frame_size = "XL"

    return {
        "frame_size": frame_size,
        "height_cm": height,
        "weight_kg": weight,
        "advice": f"Препоръчана величина на рама: {frame_size}"
    }


def generate_setup(data):

    rider_height = data.get("rider_height", 170)
    rider_weight = data.get("rider_weight", 70)
    terrain = data.get("terrain", "trail")
    bike_type = data.get("bike_type", "trail bike")

    setup = {
        "bike_info": {
            "brand": data.get("brand", "Unknown"),
            "model": data.get("model", "Unknown"),
            "type": bike_type,
            "terrain": terrain
        },
        "suspension_setup": get_suspension_setup(terrain, rider_weight),
        "tire_pressure": get_tire_pressure(terrain, rider_weight),
        "rider_info": {
            "height": rider_height,
            "weight": rider_weight
        },
        "components": {}
    }

    # Додај информации за компоненти
    if data.get("fork"):
        setup["components"]["fork"] = data.get("fork")
    if data.get("shock"):
        setup["components"]["shock"] = data.get("shock")
    if data.get("brakes"):
        setup["components"]["brakes"] = data.get("brakes")
    if data.get("drivetrain"):
        setup["components"]["drivetrain"] = data.get("drivetrain")

    return setup


def get_suspension_setup(terrain, weight):
    """Враќа суспензијски подесувања врз основа на терен и тежина"""

    weight = float(weight) if weight else 70

    if terrain == "downhill":
        return {
            "fork_pressure": f"{int(80 + (weight - 70) * 0.5)} PSI",
            "shock_pressure": f"{int(200 + (weight - 70) * 0.7)} PSI",
            "sag_fork": "25-30%",
            "sag_shock": "30-35%",
            "rebound": "Medium-Fast"
        }
    elif terrain == "enduro":
        return {
            "fork_pressure": f"{int(70 + (weight - 70) * 0.4)} PSI",
            "shock_pressure": f"{int(180 + (weight - 70) * 0.6)} PSI",
            "sag_fork": "28-32%",
            "sag_shock": "28-32%",
            "rebound": "Medium"
        }
    else:  # trail или default
        return {
            "fork_pressure": f"{int(60 + (weight - 70) * 0.3)} PSI",
            "shock_pressure": f"{int(160 + (weight - 70) * 0.5)} PSI",
            "sag_fork": "30-35%",
            "sag_shock": "25-30%",
            "rebound": "Medium-Slow"
        }


def get_tire_pressure(terrain, weight):
    """Враќа препорачана притисок на гуми врз основа на терен и тежина"""

    weight = float(weight) if weight else 70
    base_front = 1.8
    base_rear = 2.0

    if weight > 85:
        base_front += 0.3
        base_rear += 0.3

    if terrain == "downhill":
        return {
            "front_tire": f"{base_front + 0.4:.1f} bar",
            "rear_tire": f"{base_rear + 0.4:.1f} bar",
            "advice": "По-висок натиск за повече контрола"
        }
    elif terrain == "enduro":
        return {
            "front_tire": f"{base_front + 0.1:.1f} bar",
            "rear_tire": f"{base_rear + 0.2:.1f} bar",
            "advice": "Балансиран натиск за брза каране"
        }
    else:  # trail
        return {
            "front_tire": f"{base_front:.1f} bar",
            "rear_tire": f"{base_rear:.1f} bar",
            "advice": "По-нисък натиск за по-добра хватка на терена"
        }