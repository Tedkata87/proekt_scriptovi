from flask import Blueprint
from flask import request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from extensions import db

from models.bike_search import BikeSearch

from utils.response import (
    success,
    error
)

from services.ai_service import (
    generate_bike_recommendation
)

bike_search_bp = Blueprint(
    "bike_searches",
    __name__
)


# GET ALL SEARCHES
@bike_search_bp.route(
    "/bike-searches",
    methods=["GET"]
)
@jwt_required()
def get_all_searches():

    user_id = get_jwt_identity()

    searches = BikeSearch.query.filter_by(
        user_id=user_id
    ).all()

    return success(
        [
            search.to_dict()
            for search in searches
        ]
    )


# GET SEARCH BY ID
@bike_search_bp.route(
    "/bike-searches/<int:search_id>",
    methods=["GET"]
)
@jwt_required()
def get_search(search_id):

    user_id = get_jwt_identity()

    search = BikeSearch.query.filter_by(
        id=search_id,
        user_id=user_id
    ).first()

    if not search:

        return error(
            "Search not found",
            404
        )

    return success(
        search.to_dict()
    )


# CREATE SEARCH
@bike_search_bp.route(
    "/bike-searches",
    methods=["POST"]
)
@jwt_required()
def create_search():

    user_id = get_jwt_identity()

    data = request.get_json()

    if not data:

        return error(
            "JSON body required",
            400
        )

    required_fields = [
        "height",
        "weight",
        "terrain",
        "budget"
    ]

    for field in required_fields:

        if field not in data:

            return error(
                f"{field} is required",
                400
            )

    try:

        search = BikeSearch(
            user_id=user_id,
            height=data["height"],
            weight=data["weight"],
            terrain=data["terrain"],
            budget=data["budget"],
            preferences=data.get(
                "preferences",
                ""
            )
        )

        db.session.add(search)

        db.session.commit()

        # Генериран препорака
        recommendation = generate_bike_recommendation(data)

        return success(
            {
                "id": search.id,
                "height": search.height,
                "weight": search.weight,
                "terrain": search.terrain,
                "budget": search.budget,
                "preferences": search.preferences,
                "created_at": str(search.created_at),
                "bikes": recommendation.get("bikes", []),
                "sizing_advice": recommendation.get("sizing_advice", {}),
                "custom_notes": recommendation.get("custom_notes", "")
            },
            201
        )

    except Exception as e:

        db.session.rollback()

        return error(
            f"Error creating search: {str(e)}",
            500
        )


# FULL UPDATE
@bike_search_bp.route(
    "/bike-searches/<int:search_id>",
    methods=["PUT"]
)
@jwt_required()
def update_search(search_id):

    user_id = get_jwt_identity()

    search = BikeSearch.query.filter_by(
        id=search_id,
        user_id=user_id
    ).first()

    if not search:

        return error(
            "Search not found",
            404
        )

    data = request.get_json()

    if not data:

        return error(
            "JSON body required",
            400
        )

    required_fields = [
        "height",
        "weight",
        "terrain",
        "budget"
    ]

    for field in required_fields:

        if field not in data:

            return error(
                f"{field} is required",
                400
            )

    search.height = data["height"]

    search.weight = data["weight"]

    search.terrain = data["terrain"]

    search.budget = data["budget"]

    search.preferences = data.get(
        "preferences",
        ""
    )

    db.session.commit()

    return success(
        search.to_dict()
    )
    

# PARTIAL UPDATE
@bike_search_bp.route(
    "/bike-searches/<int:search_id>",
    methods=["PATCH"]
)
@jwt_required()
def patch_search(search_id):

    user_id = get_jwt_identity()

    search = BikeSearch.query.filter_by(
        id=search_id,
        user_id=user_id
    ).first()

    if not search:

        return error(
            "Search not found",
            404
        )

    data = request.get_json()

    if not data:

        return error(
            "JSON body required",
            400
        )

    if "height" in data:
        search.height = data["height"]

    if "weight" in data:
        search.weight = data["weight"]

    if "terrain" in data:
        search.terrain = data["terrain"]

    if "budget" in data:
        search.budget = data["budget"]

    if "preferences" in data:
        search.preferences = data["preferences"]

    db.session.commit()

    return success(
        search.to_dict()
    )


# DELETE
@bike_search_bp.route(
    "/bike-searches/<int:search_id>",
    methods=["DELETE"]
)
@jwt_required()
def delete_search(search_id):

    user_id = get_jwt_identity()

    search = BikeSearch.query.filter_by(
        id=search_id,
        user_id=user_id
    ).first()

    if not search:

        return error(
            "Search not found",
            404
        )

    db.session.delete(search)

    db.session.commit()

    return "", 204