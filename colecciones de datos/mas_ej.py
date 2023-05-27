
usuarios= {"marta","david","elvira","juan","marcos"}

administradores= {"juan","elvira"}

administradores.discard("juan")
administradores.add("marcos")

for i in usuarios:
    if i in administradores:
       print(f"El usuario {i} es administrador")
    else:
       print(f"el usuario {i} no es administrador")


