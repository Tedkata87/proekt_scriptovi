from flask import Blueprint, request, jsonify

from app import db

from models.bike_search import BikeSearch

from services.ai_service import generate_bike_recommendation

bike_search_bp = Blueprint("bike_search_bp", __name__)

@bike_search_bp.route("/bike-searches", methods=["POST"])
def create_search():

    data = request.get_json()

    search = BikeSearch(
        height=data["height"],
        weight=data["weight"],
        terrain=data["terrain"],
        budget=data["budget"],
        preferences=data.get("preferences")
    )

    db.session.add(search)
    db.session.commit()

    ai_result = generate_bike_recommendation(data)

    return jsonify(ai_result), 201