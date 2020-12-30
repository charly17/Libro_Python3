from math import pi

print('Programa para el cálculo del volumen de una esfera.')

radio = float(input('Dame el radio (en metros): '))

volumen = 4/3 * pi * radio ** 3

#Evitar el salto de linea en print e insertar variables
print('Voluen: {0:.4f} metros cúbicos. '.format(volumen), end='')
print('Gracias por usar el programa. Adios.')