def indeterminados_args(*args):
    for item in args:
        print(item)

def indeterminados_diccionario(**kwargs):
    print(kwargs)  

indeterminados_args("dsdfds",546546, [56465,546,654,654])  

indeterminados_diccionario(a=234, b=[5456,65465,654], c="hola")