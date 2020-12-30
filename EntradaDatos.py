#Importamos el módulo math
from math import pi

#cadena_leida = input('Dame el radio: ')

#Convertimos la cadena dada en número flotante
#radio = float(cadena_leida)
#Para hacer todo en una sola linea
radio = float(input('Dame el radio: '))

volumen = 4/3 * pi * radio ** 3

print(volumen)