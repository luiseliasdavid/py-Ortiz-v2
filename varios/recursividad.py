def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
num = 5
print(f"El factorial de {num} es: {factorial(num)}")
