#convertir una cadena que contiene letras MAYUSCULAS
cadena = 'Un EJEMPLO de Cadena'
#cadena.lower()
print(cadena.lower())

#Pasar una cadena de minusculas a mayúsculas
print('Otro ejemplo'.upper())

#MÉTODO FORMAT
print('Método format, DAR FORMATO A CADENAS')
test = 'El número {0} ha sido interpolado.'.format(1.23)
print(test)
#LO MISMO PERO CON OTRO MÉTODO
texto1 = 'El número {0} ha sido interpolado.'.replace('{0}', '1.23')
print(texto1)

#MAS VARIABLES
texto2 = 'El número {0} y {1} han sido interpolados.'.format(1.23, 9.9999)
print(texto2)

