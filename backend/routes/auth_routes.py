import bcrypt

from flask import Blueprint
from flask import request

from flask_jwt_extended import (
    create_access_token,
    jwt_required
)

from extensions import db

from models.user import User

from utils.response import (
    success,
    error
)

auth_bp = Blueprint(
    "auth",
    __name__
)
@auth_bp.route(
    "/sign-up",
    methods=["POST"]
)
def sign_up():

    data = request.get_json()

    if not data:

        return error(
            "JSON body required",
            400
        )

    username = data.get("username")

    email = data.get("email")

    password = data.get("password")

    if (
        not username
        or not email
        or not password
    ):

        return error(
            "Missing fields",
            400
        )

    existing = User.query.filter_by(
        email=email
    ).first()

    if existing:

        return error(
            "Email already exists",
            400
        )

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    user = User(
        username=username,
        email=email,
        password=hashed.decode()
    )

    db.session.add(user)

    db.session.commit()

    return success(
        {
            "message":
            "User created"
        },
        201
    )

@auth_bp.route(
    "/sign-in",
    methods=["POST"]
)

def sign_in():

    data = request.get_json()

    if not data:

        return error(
            "JSON body required",
            400
        )

    email = data.get(
        "email"
    )

    password = data.get(
        "password"
    )

    if not email or not password:

        return error(
            "Missing credentials",
            400
        )

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:

        return error(
            "Invalid credentials",
            401
        )

    valid = bcrypt.checkpw(
        password.encode(),
        user.password.encode()
    )

    if not valid:

        return error(
            "Invalid credentials",
            401
        )

    token = create_access_token(
        identity=user.id
    )

    return success(
        {
            "token": token,

            "user": {
                "id": user.id,

                "username":
                user.username,

                "email":
                user.email
            }
        }
    )

@auth_bp.route(
    "/logout",
    methods=["POST"]
)
@jwt_required()
def logout():

    return success(
        {
            "message":
            "Logged out"
        }
    )

@auth_bp.route(
    "/users/me",
    methods=["GET"]
)
@jwt_required()
def me():

    from flask_jwt_extended import (
        get_jwt_identity
    )

    user_id = get_jwt_identity()

    user = User.query.get(
        user_id
    )

    if not user:

        return error(
            "User not found",
            404
        )

    return success(
        user.to_dict()
    )