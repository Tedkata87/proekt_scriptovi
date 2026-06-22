from flask import Blueprint
from flask import request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from extensions import db

from models.bike_setup import BikeSetup

from utils.response import (
    success,
    error
)

from services.ai_service import (
    generate_setup
)

bike_setup_bp = Blueprint(
    "bike_setups",
    __name__
)


# GET ALL
@bike_setup_bp.route(
    "/bike-setups",
    methods=["GET"]
)
@jwt_required()
def get_all_setups():

    user_id = get_jwt_identity()

    setups = BikeSetup.query.filter_by(
        user_id=user_id
    ).all()

    return success(
        [
            setup.to_dict()
            for setup in setups
        ]
    )


# GET ONE
@bike_setup_bp.route(
    "/bike-setups/<int:setup_id>",
    methods=["GET"]
)
@jwt_required()
def get_setup(setup_id):

    user_id = get_jwt_identity()

    setup = BikeSetup.query.filter_by(
        id=setup_id,
        user_id=user_id
    ).first()

    if not setup:

        return error(
            "Setup not found",
            404
        )

    return success(
        setup.to_dict()
    )


# CREATE
@bike_setup_bp.route(
    "/bike-setups",
    methods=["POST"]
)
@jwt_required()
def create_setup():

    user_id = get_jwt_identity()

    data = request.get_json()

    if not data:

        return error(
            "JSON body required",
            400
        )

    required_fields = [
        "rider_height",
        "rider_weight",
        "terrain",
        "bike_type",
        "brand",
        "model"
    ]

    for field in required_fields:

        if field not in data:

            return error(
                f"{field} is required",
                400
            )

    try:

        # Генериран setup препорака
        setup_recommendation = generate_setup(data)

        setup = BikeSetup(
            user_id=user_id,

            rider_height=data[
                "rider_height"
            ],

            rider_weight=data[
                "rider_weight"
            ],

            terrain=data[
                "terrain"
            ],

            bike_type=data[
                "bike_type"
            ],

            brand=data[
                "brand"
            ],

            model=data[
                "model"
            ],

            fork=data.get(
                "fork"
            ),

            shock=data.get(
                "shock"
            ),

            frame_size=data.get(
                "frame_size"
            ),

            wheel_size=data.get(
                "wheel_size"
            ),

            drivetrain=data.get(
                "drivetrain"
            ),

            brakes=data.get(
                "brakes"
            ),

            handlebars=data.get(
                "handlebars"
            ),

            ai_result=str(setup_recommendation)
        )

        db.session.add(setup)

        db.session.commit()

        return success(
            {
                "id": setup.id,
                "brand": setup.brand,
                "model": setup.model,
                "rider_height": setup.rider_height,
                "rider_weight": setup.rider_weight,
                "terrain": setup.terrain,
                "bike_type": setup.bike_type,
                "created_at": str(setup.created_at),
                "suspension_setup": setup_recommendation.get("suspension_setup", {}),
                "tire_pressure": setup_recommendation.get("tire_pressure", {})
            },
            201
        )

    except Exception as e:

        db.session.rollback()

        return error(
            f"Error creating setup: {str(e)}",
            500
        )


# PUT
@bike_setup_bp.route(
    "/bike-setups/<int:setup_id>",
    methods=["PUT"]
)
@jwt_required()
def update_setup(setup_id):

    user_id = get_jwt_identity()

    setup = BikeSetup.query.filter_by(
        id=setup_id,
        user_id=user_id
    ).first()

    if not setup:

        return error(
            "Setup not found",
            404
        )

    data = request.get_json()

    if not data:

        return error(
            "JSON body required",
            400
        )

    required_fields = [
        "rider_height",
        "rider_weight",
        "terrain",
        "bike_type",
        "brand",
        "model"
    ]

    for field in required_fields:

        if field not in data:

            return error(
                f"{field} is required",
                400
            )

    setup.rider_height = data[
        "rider_height"
    ]

    setup.rider_weight = data[
        "rider_weight"
    ]

    setup.terrain = data[
        "terrain"
    ]

    setup.bike_type = data[
        "bike_type"
    ]

    setup.brand = data[
        "brand"
    ]

    setup.model = data[
        "model"
    ]

    setup.fork = data.get(
        "fork"
    )

    setup.shock = data.get(
        "shock"
    )

    setup.frame_size = data.get(
        "frame_size"
    )

    setup.wheel_size = data.get(
        "wheel_size"
    )

    setup.drivetrain = data.get(
        "drivetrain"
    )

    setup.brakes = data.get(
        "brakes"
    )

    setup.handlebars = data.get(
        "handlebars"
    )

    db.session.commit()

    return success(
        setup.to_dict()
    )


# PATCH
@bike_setup_bp.route(
    "/bike-setups/<int:setup_id>",
    methods=["PATCH"]
)
@jwt_required()
def patch_setup(setup_id):

    user_id = get_jwt_identity()

    setup = BikeSetup.query.filter_by(
        id=setup_id,
        user_id=user_id
    ).first()

    if not setup:

        return error(
            "Setup not found",
            404
        )

    data = request.get_json()

    if not data:

        return error(
            "JSON body required",
            400
        )

    for key, value in data.items():

        if hasattr(
            setup,
            key
        ):
            setattr(
                setup,
                key,
                value
            )

    db.session.commit()

    return success(
        setup.to_dict()
    )


# DELETE
@bike_setup_bp.route(
    "/bike-setups/<int:setup_id>",
    methods=["DELETE"]
)
@jwt_required()
def delete_setup(setup_id):

    user_id = get_jwt_identity()

    setup = BikeSetup.query.filter_by(
        id=setup_id,
        user_id=user_id
    ).first()

    if not setup:

        return error(
            "Setup not found",
            404
        )

    db.session.delete(
        setup
    )

    db.session.commit()

    return "", 204

setup_result = db.Column(db.Text)
setup.setup_result = str(result)