# Variables del ejercicio (no las modifiques)
grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

add= ["Ana","Ramón","Marta","Eric","David"]
discard=["Mario","Ramón","Miguel"]

# Completa el ejercicio
for name in add:
    grupo.add(name)
for name in discard:
    grupo.discard(name)

print(grupo)