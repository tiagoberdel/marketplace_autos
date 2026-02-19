from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(30), nullable=False)
    modelo = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
