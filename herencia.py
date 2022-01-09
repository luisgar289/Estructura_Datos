
class vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        

class coche(vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        


class camioneta(coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
        

class bicicleta(vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        


class motocicleta(bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        


coche1 = coche("Azul", 4, 200, 1200)
camioneta1 = camioneta("Verde", 4, 200, 1200, 2000)
bicicleta1 = bicicleta("Amarillo", 2, "urbana")
motocicleta1 = motocicleta("Blanco", 2, "urbana", 200, 1200)
print("")
print("Coche")
print("Color:", coche1.color)
print("Ruedas:", coche1.ruedas)
print("velocidad", coche1.velocidad, "km/h")
print("cilindrada", coche1.cilindrada , "cc")
print("")
print("Camioneta")
print("Color: ",camioneta1.color)
print("Ruedas: ",camioneta1.ruedas)
print("Velocidad: ",camioneta1.velocidad , "km/h")
print("Cilindrada: ",camioneta1.cilindrada , "cc")
print("Carga: ",camioneta1.carga , "kg")
print("")
print("Bicicleta")
print("color", bicicleta1.color)
print("ruedas", bicicleta1.ruedas)
print("tipo", bicicleta1.tipo)
print("")
print("Motocicleta")
print("color", motocicleta1.color)
print("ruedas", motocicleta1.ruedas)
print("tipo", motocicleta1.tipo)
print("velocidad", motocicleta1.velocidad , "km/h")
print("cilindrada", motocicleta1.cilindrada , "cc")
print("")