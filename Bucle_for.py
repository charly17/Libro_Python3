for nombre in ['pepe', 'ana', 'juan']:
    print('Hola, {0}'.format(nombre))

for i in range(1, 6):
    print(i)

numero = float(input('Dame un numero: '))

for n in range (2, 10):
    print('La raiz {0}-ésima de {1} es {2}'.format(n, numero, numero**(1/n)))