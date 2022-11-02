class Alumno():
  def __init__(self,nombre,nota):

    self.nombre = nombre
    self.nota = nota
  
  def imprimir(self):

    print(f"Nombre: {self.nombre}")
    print(f"Nota: {self.nota}")
  

  def resultado(self):
    if self.nota < 5:
      print(f"{self.nombre} ha suspendido")
    else:
      print(f"{self.nombre} ha aprobado")

if __name__ == "__main__":
  alumno1 = Alumno("Juan", 10)
  alumno2 = Alumno("Ana", 4)
  alumno3 = Alumno("Jesús", 7)


alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()

alumno3.imprimir()
alumno3.resultado()