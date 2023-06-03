# Funciones generadoras
# Crea una función generadora llamada cuadrados(numero) que a partir de un número genere todos los números de 1 a X (ambos incluidos) y sus potencias de dos.

# Ejemplo de la conversión del generador a lista:

# list(cuadrados(5))
# Devolverá:

# [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# Una lista con tuplas, cada tupla contiene el número y su cuadrado.

# Notas:

# Única y exclusivamente tienes que programar la función, no debe haber ningún otro código en el ejercicio.

# No tienes que devolver la conversión a lista, solo el generador.

def cuadros(numero):
    return  iter([ (item, item**2) for  item in list(range(1,numero+1))])

pepe= cuadros(5)
print(next(pepe))
print(next(pepe))
print(next(pepe))
print(next(pepe))

# otra solucion
def cuadrados(numero):
    for i in range(1, numero+1):
        yield i, i**2
