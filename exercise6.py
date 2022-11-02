class Vehiculo():

  def __init__(self,color,ruedas,puertas):
    self.color = color
    self.ruedas = ruedas
    self.puertas = puertas

  def __str__(self):
    return "color {}, {} ruedas, {} puertas".format(self.color, self.puertas, self.ruedas )

class Coche(Vehiculo):

  def __init__(self, color, ruedas, puertas,velocidad,cilindrada):
    super().__init__(color, ruedas, puertas)
    self.velocidad = velocidad
    self.cilindrada = cilindrada
  
  def __str__(self):
    return super().__str__() + ", {} cilindrada, alcanza una velocidad de {} km/h".format(self.cilindrada, self.velocidad)

mi_coche = Coche('verde', 5, 5, 240, 90)
print(mi_coche)
