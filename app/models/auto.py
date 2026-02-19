from app.database import db

class Auto(db.Model):
    __tablename__ = "autos"

    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    year = db.Column(db.Integer)
    precio = db.Column(db.Float)

    def to_dict(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "modelo": self.modelo,
            "year": self.year,
            "precio": self.precio,
        }
