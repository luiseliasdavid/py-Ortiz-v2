import inspect

class MiClase:
    def metodo1(self):
        pass

    def metodo2(self):
        pass

objeto = MiClase()

# Obtener la lista de métodos declarados en la propia clase
metodos = [nombre for nombre, valor in inspect.getmembers(objeto) if inspect.ismethod(valor) and valor.__self__ == objeto]

# Imprimir los métodos
for metodo in metodos:
    print(metodo)


