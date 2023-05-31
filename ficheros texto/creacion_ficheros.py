from io import open

# Creación y escritura del fichero
texto = "una línea\nOtra línea\notra línea"
fichero = open('fichero.txt', 'w')
fichero.write(texto)
fichero.close()

# Lectura y captura de su contenido
fichero = open('fichero.txt', 'r')
text = fichero.read()

# Cerrar el archivo antes de abrirlo en modo de apendizaje
fichero.close()

lineas = text.split('\n')

# Agregar una línea al final del archivo
fichero = open('fichero.txt', 'a')
fichero.write('\nLínea apendida')
fichero.close()

# Lectura nuevamente para incluir la línea apendida
fichero = open('fichero.txt', 'r')
text = fichero.read()
fichero.close()

print(text)
print(lineas)





