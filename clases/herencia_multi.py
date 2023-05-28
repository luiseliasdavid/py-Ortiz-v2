class Mamifero:
    def comer(self):
        print("El mamífero come")

class Volador:
    def volar(self):
        print("El animal vuela")

class Pajaro(Mamifero, Volador):
    def __init__(self, nombre):
        self.nombre = nombre

    def cantar(self):
        print(f"{self.nombre} está cantando")

# Crear una instancia de la clase Pajaro
pajaro = Pajaro("Canario")

# Utilizar métodos heredados de ambas clases base
pajaro.comer()  # Salida: El mamífero come
pajaro.volar()  # Salida: El animal vuela
pajaro.cantar()  # Salida: Canario está cantando


class A:
    def metodo(self):
        print("Método de la clase A")

class B:
    def metodo(self):
        print("Método de la clase B")

#tiene prevalencia el metodo de la clase heredada a la izquierda
class C(A, B):
    pass

# Crear una instancia de la clase C
objeto = C()

# Llamar al método que causa ambigüedad
objeto.metodo()
