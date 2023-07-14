def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

# Ejemplo de uso
numeros = [5, 10, 15, 20, 25]
promedio = calcular_promedio(numeros)
print("El promedio es:", promedio)
