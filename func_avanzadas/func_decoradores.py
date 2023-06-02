def hola():

    def bienvenido():
        return "Hola"
    #print(locals())
    #print(globals())
    return bienvenido

#el segundo parentensis ejecuta la funcion interna bienvenido
print(hola()())

bienvenido= hola()
print(bienvenido())

######################################
def aa():
    return "hola que tal"



def test(funcion):
    return funcion()

print(test(aa))
########################################
#DECORADOR
def monitorizar(funcion):

    #recibe los argumentos de la funcion
    def decorar(*args,**kwargs):
        print( "\n se esta ejecutando ",funcion.__name__ ,"\n" )
        
        #los pasa a la funcion monitorizada
        funcion(*args,**kwargs)
        print( "\n se termino de ejecutar ",funcion.__name__ )
    return decorar

@monitorizar
def bb(args):
    print(f"hola, bienvenido {args}")

bb("luis")

