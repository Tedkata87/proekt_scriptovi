from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from config import Config

db = SQLAlchemy()
jwt = JWTManager()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    jwt.init_app(app)

    CORS(app)

    # Routes
    from routes.auth_routes import auth_bp
    from routes.bike_search_routes import bike_search_bp
    from routes.bike_setup_routes import bike_setup_bp

    app.register_blueprint(auth_bp)

    app.register_blueprint(bike_search_bp)

    app.register_blueprint(bike_setup_bp)

    # Create database
    with app.app_context():
        db.create_all()

    # Error handlers

    @app.errorhandler(400)
    def bad_request(error):

        return jsonify({
            "error": "Bad Request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):

        return jsonify({
            "error": "Unauthorized"
        }), 401

    @app.errorhandler(403)
    def forbidden(error):

        return jsonify({
            "error": "Forbidden"
        }), 403

    @app.errorhandler(404)
    def not_found(error):

        return jsonify({
            "error": "Not Found"
        }), 404

    @app.errorhandler(500)
    def server_error(error):

        return jsonify({
            "error": "Server Error"
        }), 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)