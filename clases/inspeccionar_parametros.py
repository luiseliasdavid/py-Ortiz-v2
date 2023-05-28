import inspect

class MiClase:
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2

# Obtener la firma del método __init__ de la clase
firma_init = inspect.signature(MiClase.__init__)
print("este es el inspect", firma_init)

# Obtener los nombres de los parámetros requeridos
parametros_requeridos = [nombre for nombre, parametro in firma_init.parameters.items()
                         if parametro.default == inspect.Parameter.empty]

# Imprimir los nombres de los parámetros requeridos
print(parametros_requeridos)
