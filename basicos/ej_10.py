

texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

lista = texto.split("#")
lista[0]= lista[0] + "..."

nueva_lista = []

for i, cadena in enumerate(lista):
    if i != 0:
        nueva_cadena = f"- {cadena}"
        nueva_lista.append(nueva_cadena)
        
    else:
        nueva_lista.append(cadena)
    
    nueva_lista[i] = cadena + "\n"

resultado = "-".join(nueva_lista)
print(resultado)
