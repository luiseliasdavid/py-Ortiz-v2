import tkinter as tk

def on_button_click():
    global label
    label.config(text="¡Hola desde Tkinter!")

def crear_boton(ventana):
    global label
    # Crear un botón
    boton = tk.Button(ventana, text="Haz clic", command=on_button_click)

    # Crear una etiqueta para mostrar el mensaje
    label = tk.Label(ventana, text="Presiona el botón")

    # Posicionar la etiqueta en la ventana
    label.pack()

    return boton
