from flask import Flask
from app.database import db
from app.routes.autos import autos_bp
from flask_cors import CORS

def crear_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///autos.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    CORS(app)

    app.register_blueprint(autos_bp, url_prefix="/autos")

    with app.app_context():
        db.create_all()

    return app
