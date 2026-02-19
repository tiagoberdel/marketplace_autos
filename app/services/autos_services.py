from app.models.auto import Auto, db

def crear_auto(data):
    nuevo_auto = Auto(
        marca=data["marca"],
        modelo=data["modelo"],
        year=data["year"],
        precio=data["precio"]
    )

    db.session.add(nuevo_auto)
    db.session.commit()

    return nuevo_auto

def listar_autos():
    autos = Auto.query.all()
    return [auto.to_dict() for auto in autos]

def obtener_auto_por_id(id):
    auto = Auto.query.get(id)
    return auto

def eliminar_auto_por_id(id):
    auto = Auto.query.get(id)

    if not auto:
        return None

    db.session.delete(auto)
    db.session.commit()

    return auto

def actualizar_auto(id, data):
    auto = Auto.query.get(id)

    if not auto:
        return None

    auto.marca = data["marca"]
    auto.modelo = data["modelo"]
    auto.year = data["year"]
    auto.precio = data["precio"]

    db.session.commit()

    return auto
