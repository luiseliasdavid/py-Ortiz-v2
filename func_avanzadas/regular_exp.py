import re

# Ejemplo 1: Coincidencia simple
texto = "Hola, ¿cómo estás?"
patron = r"cómo"
resultado = re.search(patron, texto)
if resultado:
    print("Coincidencia encontrada:", resultado.group())
else:
    print("No se encontró ninguna coincidencia.")

# Ejemplo 2: Búsqueda y reemplazo
texto = "La manzana es roja. Me gustan las manzanas."
patron = r"manzanas"
nuevo_texto = re.sub(patron, "peras", texto)
print("Texto original:", texto)
print("Nuevo texto:", nuevo_texto)

# Ejemplo 3: Extracción de números
texto = "El precio es $19.99 por unidad."
patron = r"\d+\.\d+"
resultado = re.search(patron, texto)
if resultado:
    print("Número encontrado:", resultado.group())
else:
    print("No se encontró ningún número.")

# Ejemplo 4: División de cadenas
texto = "Hola|cómo|estás"
patron = r"\|"
partes = re.split(patron, texto)
print("Partes divididas:", partes)
