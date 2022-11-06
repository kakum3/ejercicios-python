from  functools import reduce

def ejemplo(lista):
  result = list(filter((lambda x: x % 2), lista))
  print(result)

  result = reduce((lambda x, y: x + y), result)
  print(result)

lista = list(range(50))

ejemplo(lista)