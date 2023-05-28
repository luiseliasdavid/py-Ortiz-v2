class MiClase:
    def __init__(self, elementos):
        self.elementos = elementos

    def __str__(self):
        return f'MiClase: {self.elementos}'

    def __repr__(self):
        return f'MiClase({self.elementos})'

    def __len__(self):
        return len(self.elementos)

    def __getitem__(self, indice):
        return self.elementos[indice]

    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor

    def __delitem__(self, indice):
        del self.elementos[indice]

# Crear una instancia de la clase
objeto = MiClase([1, 2, 3, 4, 5])

# Sobrescribir los métodos y utilizarlos
print(objeto)  # Salida: MiClase: [1, 2, 3, 4, 5]
print(repr(objeto))  # Salida: MiClase([1, 2, 3, 4, 5])
print(len(objeto))  # Salida: 5
print(objeto[2])  # Salida: 3
objeto[3] = 10
print(objeto)  # Salida: MiClase: [1, 2, 3, 10, 5]
del objeto[1]
print(objeto)  # Salida: MiClase: [1, 3, 10, 5]
