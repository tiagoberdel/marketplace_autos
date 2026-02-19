MAX_PRECIO = 10_000_000

def validar_auto(data):

    if not isinstance(data, dict):
        return False, "Formato inválido"
    
    # validación de marca
    marca = data.get("marca")

    if marca is None:
        return False, "El campo 'marca' es obligatorio"
    
    if not isinstance(marca, str):
        return False, "El campo 'marca' debe ser texto"
    
    marca = marca.strip()

    if marca == "":
        return False, "El campo 'marca' no puede estar vacío"
    
    # validación de modelo
    modelo = data.get("modelo")

    if modelo is None:
        return False, "El campo 'modelo' es obligatorio"
    
    if not isinstance(modelo, str):
        return False, "El campo 'modelo' debe ser texto"
    
    modelo = modelo.strip()

    if modelo == "":
        return False, "El campo 'modelo' no puede estar vacío"
    
    # Validación del año
    year = data.get("year")

    if year is None:
        return False, "El campo 'año' es obligatorio"
    
    try:
        year = int(year)
    except (ValueError, TypeError):
        return False, "El campo 'año' debe ser un número válido"
    
    if year < 1900 or year > 2026:
        return False, "Ingrese un año válido"
    
    # Validación del precio
    precio = data.get("precio")

    if precio is None:
        return False, "El campo 'precio es obligatorio'"
    
    try:
        precio = float(precio)
    except (ValueError, TypeError):
        return False, "El campo 'precio' debe ser un numero válido"
    
    if precio <= 0:
        return False, "El precio debe ser mayor a 0"
    elif precio > MAX_PRECIO:
        return False, "El precio es muy elevado"

    return True, {
        "marca": marca.strip(),
        "modelo": modelo.strip(),
        "year": year,
        "precio": precio
    }