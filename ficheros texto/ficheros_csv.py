import csv

# Crear un archivo CSV y escribir datos en él
datos = [
    ['Nombre', 'Edad', 'País'],
    ['Juan', 25, 'España'],
    ['María', 30, 'México'],
    ['Pedro', 35, 'Argentina']
]

# Crear el archivo CSV y escribir los datos
with open('datos.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(datos)

# Leer datos desde un archivo CSV
with open('datos.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)

# Manipulación de datos en un archivo CSV
with open('datos.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    encabezados = next(lector_csv)  # Leer la primera fila como encabezados
    print(encabezados)  # Imprimir los encabezados
    for fila in lector_csv:
        nombre = fila[0]
        edad = int(fila[1])
        pais = fila[2]
        # Realizar manipulación adicional de los datos según sea necesario
        # ...
