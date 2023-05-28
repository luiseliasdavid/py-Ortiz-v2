
def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("no se permite None")
    except ValueError as error:
        print(error)

mi_funcion()