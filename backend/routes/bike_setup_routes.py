from flask import Blueprint, request, jsonify

from app import db

from models.bike_setup import BikeSetup

from services.ai_service import generate_setup

bike_setup_bp = Blueprint("bike_setup_bp", __name__)

@bike_setup_bp.route("/bike-setups", methods=["POST"])
def create_setup():

    data = request.get_json()
    setup = BikeSetup(
        bike_model=data["bike_model"],
        fork=data["fork"],
        shock=data["shock"],
        frame_size=data["frame_size"],
        wheel_size=data["wheel_size"],
        terrain=data["terrain"]
    )

    db.session.add(setup)
    db.session.commit()
    ai_result = generate_setup(data)
    return jsonify(ai_result), 201