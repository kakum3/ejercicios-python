from pickle import *

class Vehiculo:

  def __init__(self, color, puertas) -> None:
    self.color = color
    self.puertas = puertas

  def __str__(self) -> str:
    return self.color + " " + self.puertas

berlingo= Vehiculo('rojo', '5')
print(berlingo)

f = open('vehiculo_obj', 'w+b')
dump(berlingo , f)

f.seek(0)
nuevo_berlingo = load(f)

print(nuevo_berlingo)
f.close()
    