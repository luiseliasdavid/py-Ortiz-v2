numeros = [1, 2, 3]

#al comvertir el iterador en una lista puede iterarse de multiples veces
cuadrados = list(map(lambda x: x**2, numeros))


for resultado in cuadrados:
    print(resultado)

print("-------------")

for resultado in cuadrados:
    print(resultado)

 #################################   
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"{self.nombre} de {self.edad} años "

personas= [
    Persona("juan",19),
    Persona("pepe",20),
    Persona("clau",25),
    Persona("manual",24),
    Persona("kiko",36),
]

# para usar lambda con clases se deven volver a crear en tiempo de ejecucion del map
personas = map(lambda persona: Persona(persona.nombre,persona.edad + 1),personas)

for persona in personas:
    print(persona)

