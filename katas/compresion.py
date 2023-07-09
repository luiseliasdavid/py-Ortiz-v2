# Ejemplo de compresión de listas: Obtener los cuadrados de los números pares de una lista

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Compresión de lista para obtener los cuadrados de los números pares
cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]

# Imprimir la lista resultante
print(cuadrados_pares)