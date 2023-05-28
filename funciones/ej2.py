
def separacion(lista):
    pares=[]
    impares=[]

    for num in lista:
        pares.append(num) if num % 2 ==0 else impares.append(num)

    return pares,impares

print(separacion([1,2,3,4,5,6,7,8,9]))