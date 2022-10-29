# Ejercicio 3: calcular indice masa corporal(IMC).


def imc(altura,peso):
    return peso / altura**2

peso = float(input('Introduzca su peso en (kg):  '))
altura = float(input('Introduzca su altura en (m):  '))

indice = imc(altura,peso)

print('Su IMC es: {:.2f}'.format(indice))
