import inspect


class MiClase:
    def __init__(self, parametro_publico, parametro_privado):
        self.parametro_publico = parametro_publico
        self.__parametro_privado = parametro_privado

    def metodo_publico(self):
        print("Método público")
        self.__metodo_privado()

    def __metodo_privado(self):
        print("Método privado")
        print(self.parametro_publico)
        print(self.__parametro_privado)

    def __metodo_privado2(self):
        print("Otro método privado")


# Crear una instancia de la clase
objeto = MiClase("Parámetro público", "Parámetro privado")

# Acceder a los atributos públicos
print(objeto.parametro_publico)  # Salida: Parámetro público

# Llamar a los métodos públicos
objeto.metodo_publico()
# Salida:
# Método público
# Método privado
# Parámetro público
# Parámetro privado

# Acceder a los atributos privados (generará un AttributeError)
# print(objeto.__parametro_privado)

# Llamar a los métodos privados (generará un AttributeError)
# objeto.__metodo_privado()

# Llamar a un método privado desde otro método público
objeto.metodo_publico()
# Salida:
# Método público
# Método privado
# Parámetro público
# Parámetro privado
