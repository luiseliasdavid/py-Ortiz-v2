import inspect


class OtraClase:
    def __init__(self, parametro):
        self.parametro = parametro

class Producto(OtraClase):
    def __init__(self, parametro, nombre):
        super().__init__(parametro)
        self.nombre = nombre

class Alimento(Producto):
    def __init__(self, nombre, parametro, vencimiento):
        super().__init__(nombre, parametro)
        self.vencimiento = vencimiento

alimento1 = Alimento("Manzana", "Parámetro", "2023-05-30")
print(alimento1.nombre)  # Salida: Manzana
print(alimento1.parametro)  # Salida: Parámetro
print(alimento1.vencimiento)  # Salida: 2023-05-30

print("parametros requeridos: ",inspect.signature(Alimento.__init__))