from flask import Flask

def crear_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return {"mensaje": "API corriendo"}
    
    return app