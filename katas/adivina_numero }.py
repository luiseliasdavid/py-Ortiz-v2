# El objetivo del juego es que el jugador adivine un número aleatorio generado por el programa. 


import random

def adivinar_numero():
    numero_secreto = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100. ¡Adivina cuál es!")

    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta nuevamente.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta nuevamente.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break

adivinar_numero()
