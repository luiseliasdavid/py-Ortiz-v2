import pickle

# Objeto a serializar
datos = [1, 2, 3, 4, 5]

# Guardar el objeto en un archivo
with open('archivo.pickle', 'wb') as archivo:
    pickle.dump(datos, archivo)

# Cargar el objeto desde el archivo
with open('archivo.pickle', 'rb') as archivo:
    datos_cargados = pickle.load(archivo)

print(datos_cargados)  # [1, 2, 3, 4, 5]
