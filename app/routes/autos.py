from flask import Blueprint, request, jsonify, HTTPException
from app.models.auto import Auto, db

autos_bp = Blueprint("autos", __name__, url_prefix="/autos")

@autos_bp.route("/", methods=["POST"])
def agregar_auto():
    data = request.get_json()

    nuevo_auto = Auto(
        marca=data["marca"],
        modelo=data["modelo"],
        year=data["year"],
        precio=data["precio"]
    )

    db.session.add(nuevo_auto)
    db.session.commit()

    return jsonify({"mensaje": "Auto creado con éxito"}), 201

@autos_bp.route("/", methods=["GET"])
def obtener_autos():
    autos = Auto.query.all()

    resultado = []
    for auto in autos:
        resultado.append({
            "id": auto.id,
            "marca": auto.marca,
            "modelo": auto.modelo,
            "año": auto.year,
            "precio": auto.precio
        })

    return jsonify(resultado), 200

@autos_bp.route("/<id>", methods=["GET"])
def obtener_auto(id):
    auto = Auto.query.get(id)
    if not auto:
        return {"mensaje": "Auto con la id f{id} no encontrado"}, 404
    
    resultado = {
        "id": auto.id,
        "marca": auto.marca,
        "modelo": auto.modelo,
        "año": auto.year,
        "precio": auto.precio
    }
    return jsonify(resultado), 200 

@autos_bp.route("/<id>", methods=["DELETE"])
def eliminar_auto(id):
    auto = Auto.query.get(id)
    if not auto:
        return {"mensaje": f"Auto con la id {id} no encontrado"}, 404
    
    db.session.delete(auto)
    db.session.commit()
    return {"mensaje": f"Auto con el id {id} eliminado con exito"}, 200

@autos_bp.route("/<id>", methods=["PUT"])
def editar_auto(id):
    data = request.get_json()
    auto = Auto.query.get(id)
    if not auto:
        return {"mensaje": f"Auto con la id {id} no encontrado"}, 404
    elif not data:
        return {"mensaje": "Faltan datos para modificar"}, 400
    auto.marca= data["marca"]
    auto.modelo= data["modelo"]
    auto.year= data["year"]
    auto.precio= data["precio"]
    db.session.commit()
    return {"mensaje": f"Auto con id {id} modificado con éxito"}, 200