lista = [1, 2, 3, 4, 5]

# Métodos de modificación
lista.append(6)  # Agrega un elemento al final de la lista
lista.insert(2, 7)  # Inserta un elemento en una posición específica
lista.extend([8, 9, 10])  # Extiende la lista agregando varios elementos al final
lista.remove(3)  # Elimina la primera aparición de un elemento específico
lista.pop()  # Elimina y devuelve el último elemento de la lista

# Métodos de búsqueda
resultado = lista.index(4)  # Devuelve el índice de la primera aparición de un elemento
resultado = lista.count(2)  # Cuenta cuántas veces aparece un elemento en la lista

# Métodos de ordenamiento y reversión
lista.sort()  # Ordena la lista en orden ascendente
lista.reverse()  # Invierte el orden de la lista

# Métodos de copia y limpieza
copia_lista = lista.copy()  # Crea una copia superficial de la lista
lista.clear()  # Elimina todos los elementos de la lista

print(lista)
print(resultado)
