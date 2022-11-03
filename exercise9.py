import time

hora = time.strftime("%H")
minutos = time.strftime("%M")

if int(hora) >= 18:
  print('Es la hora de ir a casa')
else:
  print("Aun quedan: {} horas y {} minutos para ir a casa".format(17 - int(hora), 59 - int(minutos)))