import operaciones


def main():
  resSum = operaciones.sumar(5, 7)
  resRest = operaciones.restar(9, 7)
  resMulti = operaciones.multiplicar(9, 7)
  resDiv = operaciones.dividir(8 , 2)

  print('Hola en main():', resSum, resRest, resMulti, resDiv)


if __name__ == '__main__':
  main()
 