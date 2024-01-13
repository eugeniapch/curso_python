"""
    Vamos a ejemplificar variables que guardan texto
"""

nombre = 'Maria'
apellido = "Pereira"
nombre_completo = nombre + ' ' + apellido

print('Nombre:', nombre)
print('Apellido:', apellido)
print('Nombre completo:', nombre_completo)

print()

print('Tipo de dato de la variable nombre:', type(nombre))
print('Tipo de dato de la variable apellido:', type(apellido))
print('Tipo de dato de la variable nombre_completo:', type(nombre_completo))

print()

edad = 55

resultado = nombre_completo + ' tiene ' + str(edad) + ' años.'
print(resultado)

print()

# Otra forma de hacerlo
resultado = '{} tiene {} años.'.format(nombre_completo, edad)
print(resultado)