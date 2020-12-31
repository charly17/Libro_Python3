from math import pi

radio = float(input('Dame el radio de un circulo: '))

# Menú
print('Escoge una opción: ')
print('a) Calcular el diámetro.')
print('b) Calcular el perímetro.')
print('c) Calcular el área.')

opcion = input('Teclea a, b o c y pulsa retorno de carro: ')

if opcion == 'a' or opcion == 'A': # Cálculo de diámetro
    diametro = 2 * radio
    print('El diámetro es {0}.'.format(diametro))
elif opcion == 'b' or opcion == 'B': # Cálculo del perímetro
    perimetro = 2 * pi * radio
    print('El perímetro es {0}.'.format(perimetro))
elif opcion == 'c' or opcion == 'C': #Cálculo de área
    area = pi * radio ** 2
    print('El área es {0}.'.format(area))
else:
    print('Solo hay tres opciones: a, b o c.')
    print('Tú has tecleado "{0}".'.format(opcion))