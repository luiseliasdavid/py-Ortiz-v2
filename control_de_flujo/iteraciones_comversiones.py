multiplos = []

# Completa el ejercicio 
numero = int(input("ingresa un numero entre 1 y 9: "))

while numero < 1  or numero > 9 :
    numero= int(input("error, ingresa un numero entre 1 y 9: "))

multiplos = list(range(numero,101,numero))

print(multiplos)
