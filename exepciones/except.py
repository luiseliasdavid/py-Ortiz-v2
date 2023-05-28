while(True):
    try:
        n = float(input("intruce un numero: "))
        m= 4
        print("{}/{}={}".format(n,m,n/m))
    except TypeError :
        print("ha ocurrido un errror, vuelve a intrucir un numero")
    else:
        print("todo fue bien")
        break #importante romper la iteracion
    finally:
        print("have a nice day ")