
class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f" {self.color}\n {self.ruedas}\n "
    

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad,cilindrada):
        super().__init__(color, ruedas)
        self.velocidad= velocidad
        self.cilindrada= cilindrada

    def __str__(self):
        return super().__str__()+ f"{self.velocidad}\n {self.cilindrada}\n"

a = Coche("rojo",4,400,500)
print(a)