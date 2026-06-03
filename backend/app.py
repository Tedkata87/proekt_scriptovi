from flask import flask
from flask sqalchemy import SQLAlchemy 
from flask jwt extended import JWTManager
from flask cors impotr CORS 

from config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create app():
    app = Flask(_name_)

    app.config.form_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    CORS(app)

    from routes.auth_routes import auth bp 
    from routes.bike_search_routes import bike_search_bp
    from routes.bike_setup_routes import bike_setup_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(bike_search_bp)
    app.register_blueprint(bike_setup_bp)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if _name_ == "_main_":
    app.run(debug=True)