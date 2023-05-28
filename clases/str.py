class MiClase:
    def __init__(self, parametro):
        self.parametro = parametro

    def __str__(self):
        return f"MiClase: {self.parametro}"

# Crear una instancia de la clase
objeto = MiClase("valor_parametro")

# Imprimir la representación en forma de cadena de la instancia
print(objeto)  # Salida: MiClase: valor_parametro
