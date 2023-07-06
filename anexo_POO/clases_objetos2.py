#clases objetos

class Persona:
    def __init__(self,n1,n2) -> None:
        self.n1 = n1
        self.n2 = n2
    def suma(self):
        return self.n2 + self.n1

per = Persona(2,3)

print(per.suma)
print(per.n1)