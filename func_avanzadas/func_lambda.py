# Función lambda que suma dos números
suma = lambda x, y: x + y

# Llamada a la función lambda
resultado = suma(5, 3)
print(resultado)  # Salida: 8


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Utilizando una función lambda con filter para filtrar los números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)  # Salida: [2, 4, 6, 8, 10]
