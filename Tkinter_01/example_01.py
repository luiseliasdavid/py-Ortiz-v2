import tkinter as tk
from tkinter import Frame
from mi_modulo import crear_boton
# Crear la ventana
ventana = tk.Tk()

frame = Frame(ventana, width=480, height=320)

# Configurar el título de la ventana
ventana.title("Ejemplo de Tkinter")

# Crear el botón utilizando la función del módulo
boton = crear_boton(ventana)

# Posicionar el botón en la ventana
boton.pack()

# Iniciar el bucle de eventos de Tkinter
ventana.mainloop()
