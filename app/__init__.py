from flask import Flask
from config import Config
from app.models.auto import db
from app.routes.autos import autos_bp

def crear_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(autos_bp)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return {"mensaje": "API corriendo"}
    
    return app