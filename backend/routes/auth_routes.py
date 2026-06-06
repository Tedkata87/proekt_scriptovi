from flask import Blueprint, request, jsonify

from app import db

from models.user import User

import bcrypt

from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/sign-up", methods=["POST"])
def sign_up():

    data = request.get_json()

    username = data.get("username")

    email = data.get("email")

    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({"error": "Email already exists"}), 400

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    user = User(
        username=username,
        email=email,
        password=hashed_password.decode("utf-8")
    )

    db.session.add(user)

    db.session.commit()

    return jsonify({"message": "User created"}), 201


@auth_bp.route("/sign-in", methods=["POST"])
def sign_in():

    data = request.get_json()

    email = data.get("email")

    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    valid_password = bcrypt.checkpw(
        password.encode("utf-8"),
        user.password.encode("utf-8")
    )

    if not valid_password:
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)

    return jsonify({"token": token}), 200