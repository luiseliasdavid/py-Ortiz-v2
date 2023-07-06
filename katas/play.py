
#lista = ["a","b","c"]
#lista = [2,4,6,7,8]
a ="aretheyhere" 
#b= "yestheyarehere"

def pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))
# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = pares(lista_numeros)

print(pares)  # Output: [2, 4, 6, 8, 10]