f = open('hola mundo.txt', 'w')
f.write('Hola mundo\n')
f.close()

f = open('hola mundo.txt', 'r+')
f.readline()
f.write('Esta es la segunda vez que escribo.\n')

f.seek(0)
print(f.read())
f.close()