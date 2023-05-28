
while True:
    try:
        n = float(input("intruce un numero: "))
        m= 4
        print("{}/{}={}".format(n,m,n/m))
    except TypeError:
        print(TypeError.__name__)    
