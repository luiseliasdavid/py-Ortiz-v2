def sumatorio(numero):
    """
    Calcula la suma de los números desde 1 hasta el número dado de forma recursiva.
    
    Parámetros:
    - numero (int): El número hasta el cual se realizará la suma.
    
    Retorna:
    El resultado de la suma de los números desde 1 hasta el número dado.
    """
    if numero > 0:
        numero = numero + sumatorio(numero - 1)
    return numero

resultado = sumatorio(5)
print(resultado)
