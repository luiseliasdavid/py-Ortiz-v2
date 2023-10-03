def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso de la función factorial
resultado = factorial(5)
print("El factorial de 5 es:", resultado)
