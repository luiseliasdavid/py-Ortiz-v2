class Forma:
    def area(self):
        pass

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

# Crear instancias de las clases Cuadrado y Circulo
cuadrado = Cuadrado(5)
circulo = Circulo(3)

# Llamar al método area() en ambos objetos
print(cuadrado.area())  # Salida: 25
print(circulo.area())  # Salida: 28.27431
