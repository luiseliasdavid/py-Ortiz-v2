class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Crear instancias con edades por debajo de 18
personas = [
    Persona("Juan", 14),
    Persona("María", 16),
    Persona("Carlos", 17),
    Persona("Ana", 15),
    Persona("Pedro", 21),
    Persona("Luisa", 30),
    Persona("Laura", 19),
    Persona("Miguel", 25)
]

menores = filter(lambda persona: persona.edad < 18, personas)

for person in menores:
    print(person)
