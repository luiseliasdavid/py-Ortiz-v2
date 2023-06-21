"""
En este problema, se te pide crear una función de Tribonacci que genere los primeros "n" elementos de una secuencia de Tribonacci, dada una secuencia inicial (firma). La secuencia de Tribonacci se genera sumando los últimos 3 números de la secuencia para generar el siguiente número.

Aquí tienes un resumen de lo que debes hacer:

1. Define una función llamada "tribonacci" que tome dos argumentos: una lista de tres números llamada "firma" y un número entero no negativo llamado "n".

2. Si "n" es igual a 0, debes devolver una lista vacía.

3. Crea una lista vacía llamada "result" para almacenar los elementos de la secuencia Tribonacci.

4. Agrega los elementos de la firma inicial a la lista "result".

5. Si "n" es menor o igual a 3 (la longitud de la firma inicial), debes devolver la lista "result" tal como está.

6. De lo contrario, comienza un bucle desde el índice 3 hasta "n-1".

7. En cada iteración del bucle, calcula el siguiente número de Tribonacci sumando los últimos tres elementos de la lista "result" y agrégalo a la lista.

8. Después de completar el bucle, devuelve la lista "result" con los primeros "n" elementos de la secuencia de Tribonacci.

Recuerda que este resumen solo describe el proceso paso a paso sin proporcionar la solución completa. Intenta implementar la función por ti mismo siguiendo estos pasos y, si tienes alguna pregunta o te encuentras con dificultades, estaré aquí para ayudarte.
"""

def tribonacci(signature, n):
    result = []
    if n == 0: return result
    if n <= 3: return signature[0:n-1]
    result=signature
    contador= 3
    while contador < n:
        result.append(result[-1] + result[-2] + result[-3])
        contador = contador + 1
    return result
