"""
# *! Números complejos:
    class complex(real=0, imag=0)
    class complex(string)
    Retorna el número complejo con el valor real + imag*1j o convierte una cadena o un número a un número complejo. 
    
    # ** Si el primer parámetro es una cadena, será interpretada como un número complejo y la función debe ser llamada sin un segundo parámetro. 
    # ** El segundo parámetro nunca puede ser una cadena. 
    
    Cada argumento puede ser de cualquier tipo numérico (incluyendo complex). Si se omite imag, su valor por defecto es cero y el constructor sirve como un conversor numérico como int y float. Si ambos argumentos son omitidos, retorna 0j.
"""

# *! Primera forma de crear números complejos (forma literal)
numero_complejo = 2 - 3j
print('Contenido variable compleja:', numero_complejo)
print('El tipo de dato de la variable numero_complejo es:', type(numero_complejo))

print()

# *! Segunda forma de crear números complejos (instanciando la clase complex())
numero_complejo = complex(2, -3) 
print('Contenido variable compleja:', numero_complejo)
print('El tipo de dato de la variable numero_complejo es:', type(numero_complejo))

print()

print('Operaciones aritméticas sobre números complejos:')

# *! Operación suma de números complejos (sumamos las partes reales y luego las imaginarias)
suma = 2 - 3j + (1 + 5j)
print('Suma:', suma)

# *! Operación resta (restamos las partes reales y las imaginarias)
resta = 2 - 3j - complex(1, 5)
print('Resta:', resta)

# *! Operación de multiplicación (recordemos que j^2 = -1)
# (2 - 3j)(1 + 5j) = 2 + 10j - 3j - 15j^2 = 2 + 7j - 15(-1) = 17 + j
producto = (2 - 3j) * complex(1, 5)
print('Producto:', producto)

# *! Operación de division ()
division = 2 - 3j / complex(1, 5)
print('División:', division)