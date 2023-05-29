cadena = "Hola Mundo"

# Métodos de formato
resultado = cadena.capitalize()  # Hola mundo
resultado = cadena.upper()  # HOLA MUNDO
resultado = cadena.lower()  # hola mundo
resultado = cadena.title()  # Hola Mundo

# Métodos de búsqueda y reemplazo
resultado = cadena.startswith("Hola")  # True
resultado = cadena.endswith("Mundo")  # True
resultado = cadena.find("Mundo")  # 5
resultado = cadena.replace("Mundo", "Amigo")  # Hola Amigo

# Métodos de manipulación
resultado = cadena.split()  # ['Hola', 'Mundo']
resultado = cadena.strip()  # "Hola Mundo" (elimina espacios en blanco al inicio y al final)
resultado = cadena.join(['Hola', 'Mundo'])  # HolaHolaMundo
resultado = len(cadena)  # 10 (longitud de la cadena)

# Métodos de verificación
resultado = cadena.isalpha()  # False (verifica si todos los caracteres son letras)
resultado = cadena.isdigit()  # False (verifica si todos los caracteres son dígitos)
resultado = cadena.islower()  # False (verifica si todos los caracteres están en minúsculas)
resultado = cadena.isupper()  # False (verifica si todos los caracteres están en mayúsculas)

# Métodos de formato avanzado
resultado = cadena.center(20, '-')  # ---Hola Mundo---
resultado = cadena.ljust(15, '.')  # Hola Mundo.....
resultado = cadena.rjust(15, '.')  # .....Hola Mundo

print(resultado)
