def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def calculadora():
    print("Calculadora Simple")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        opcion = input("Seleccione la operación (1/2/3/4) o 'q' para salir: ")

        if opcion.lower() == 'q':
            print("¡Hasta luego!")
            break

        if opcion in ('1', '2', '3', '4'):
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                print("Resultado:", suma(num1, num2))
            elif opcion == '2':
                print("Resultado:", resta(num1, num2))
            elif opcion == '3':
                print("Resultado:", multiplicacion(num1, num2))
            elif opcion == '4':
                print("Resultado:", division(num1, num2))
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1/2/3/4) o 'q' para salir.")

if __name__ == "__main__":
    calculadora()
