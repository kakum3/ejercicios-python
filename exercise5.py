año =int(input('Introduce un año por favor: '))
def bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        print ('El año introducido  es bisiesto')
    else:
        print('El año introducido no es bisiesto')

bisiesto(año)