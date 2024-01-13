edad = 29
dias_vividos = edad * 365
cantidad_hijos = 10
anno_experiencia = 10
otro_dato = 29.0

print(edad)
print(dias_vividos)

print('Tipo de dato de la variable edad:', type(edad))
print('Tipo de dato de la variable dias_vividos:', type(dias_vividos))
print('Tipo de dato de cantidad hijos', type(cantidad_hijos))
print('Tipo de datos de anno_experiencia:',type(anno_experiencia))
print('Tipo de datos de otro_datos:', type(otro_dato))

print()

# Buscando la ubicación en memoria de las variables
print('Posición en memoria de la variable edad:', id(edad))
print('Posición en memoria de la variable dias_vividos:', id(dias_vividos))
print('Posición de memoria de la cantidad_hijos', id(cantidad_hijos))
print('Posición de memoria de la anno_experiencia', id(anno_experiencia))
print('Posición de memoria de la otro_dato', id(otro_dato))

print()

# Buscamos la ubicación en memoria del valor de la variable
print('Posición en memoria del valor 29:', id(29))
print('Posición en memoria del valor 10585:', id(10585))
print('Posición en memoria del valor 10:', id(10))
print('Posición en memoria del valor 10:', id(29.0))

"""
Internamente Python optimiza el uso de la memoria, es decir si hay 10 variables y todas tienen el mismo valor , todas van a tener el mismo identificador
"""