import json

# Crear un diccionario con datos
datos = {
    'nombre': 'Juan',
    'edad': 25,
    'país': 'España'
}

# Escribir los datos en un archivo JSON
with open('datos.json', 'w') as archivo_json:
    json.dump(datos, archivo_json)

# Leer los datos desde un archivo JSON
with open('datos.json', 'r') as archivo_json:
    datos_cargados = json.load(archivo_json)
    print(datos_cargados)

# Manipulación de datos en un archivo JSON
with open('datos.json', 'r+') as archivo_json:
    datos = json.load(archivo_json)
    datos['edad'] = 26
    datos['país'] = 'Argentina'
    archivo_json.seek(0)  # Mover el puntero de escritura al inicio del archivo
    json.dump(datos, archivo_json, indent=4)
    archivo_json.truncate()  # Truncar el archivo desde la posición actual
