# Completa el ejercicio
def sumatorio(numero):
   
    if numero > 0:
        numero = numero + sumatorio(numero-1)
        print(numero)
    return numero

resultado = sumatorio(5)

print(resultado)

