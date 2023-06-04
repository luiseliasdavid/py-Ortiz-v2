import inspect


class OtraClase:
    def __init__(self, parametro):
        """
        Constructor de la clase OtraClase.
        
        Parámetros:
        - parametro (any): Un parámetro genérico que representa algo en la clase.
        """
        self.parametro = parametro


class Producto(OtraClase):
    def __init__(self, parametro, nombre):
        """
        Constructor de la clase Producto, heredada de OtraClase.
        
        Parámetros:
        - parametro (any): Un parámetro genérico que representa algo en la clase.
        - nombre (str): El nombre del producto.
        """
        super().__init__(parametro)
        self.nombre = nombre


class Alimento(Producto):
    def __init__(self, parametro, nombre, vencimiento):
        """
        Constructor de la clase Alimento, heredada de Producto.
        
        Parámetros:
        - parametro (any): Un parámetro genérico que representa algo en la clase.
        - nombre (str): El nombre del alimento.
        - vencimiento (str): La fecha de vencimiento del alimento en formato YYYY-MM-DD.
        """
        super().__init__(parametro, nombre)
        self.vencimiento = vencimiento


alimento1 = Alimento("Manzana", "Parámetro", "2023-05-30")
print(alimento1.nombre)  # Salida: Manzana
print(alimento1.parametro)  # Salida: Parámetro
print(alimento1.vencimiento)  # Salida: 2023-05-30

print("parametros requeridos: ", inspect.signature(Alimento.__init__))
