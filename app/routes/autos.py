from flask import Blueprint, request, jsonify
from app.models.auto import Auto, db
from app.utils.validators import validar_auto
from app.services.autos_services import crear_auto, listar_autos, obtener_auto_por_id, eliminar_auto_por_id, actualizar_auto

autos_bp = Blueprint("autos", __name__, url_prefix="/autos")

# /POST auto

@autos_bp.route("/", methods=["POST"])
def agregar_auto():
    data = request.get_json()

    es_valido, resultado = validar_auto(data)

    if not es_valido:
        return jsonify({"error": resultado}), 400

    auto_creado = crear_auto(resultado)

    return jsonify({
        "mensaje": "Auto creado con éxito",
        "id": auto_creado.id
    }), 201

# / GET autos

@autos_bp.route("/", methods=["GET"])
def obtener_autos():
    autos = listar_autos()
    return jsonify(autos), 200

# / GET auto

@autos_bp.route("/<id>", methods=["GET"])
def obtener_auto(id):
    auto = obtener_auto_por_id(id)

    if not auto:
        return {"mensaje": f"Auto con id {id} no encontrado"}, 404

    return jsonify(auto.to_dict()), 200

# / DELETE auto

@autos_bp.route("/<id>", methods=["DELETE"])
def eliminar_auto(id):
    auto = eliminar_auto_por_id(id)

    if not auto:
        return {"mensaje": f"Auto con id {id} no encontrado"}, 404

    return {"mensaje": f"Auto con id {id} eliminado con éxito"}, 200

# / PUT auto

@autos_bp.route("/<id>", methods=["PUT"])
def editar_auto(id):
    data = request.get_json()

    es_valido, resultado = validar_auto(data)
    if not es_valido:
        return jsonify({"error": resultado}), 400

    auto = actualizar_auto(id, resultado)

    if not auto:
        return {"mensaje": f"Auto con id {id} no encontrado"}, 404

    return {"mensaje": f"Auto con id {id} modificado con éxito"}, 200
