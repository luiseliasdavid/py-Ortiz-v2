
lista=[1,2,3,4]

try:
    lista[10]
except IndexError as error:
    print("se ha producido el siguuiente error: ", error)