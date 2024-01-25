"""
# *! Los booleanos representan valores de verdad
El tipo bool tiene exactamente dos instancias constantes: Verdadero y Falso.

La función incorporada bool() convierte cualquier valor a booleano, si el valor puede interpretarse como un valor de verdad (consulte la sección Evaluar como valor verdadero/falso más arriba).

Para operaciones lógicas, utilice los operadores booleanos and, or, and not. Al aplicar los operadores &, | ,  ^ a dos booleanos, devuelven un booleano equivalente a las operaciones lógicas «and», «or», «xor». Sin embargo, los operadores lógicos and, or and != deben preferirse a &, | y ^.

Obsoleto desde la versión 3.12: El uso del operador de ~ está obsoleto y generará un error en Python 3.14.

bool es una subclase de int. En muchos contextos numéricos, False y True se comportan como los números enteros 0 y 1, respectivamente. Sin embargo, no se recomienda confiar en esto; convertir explícitamente usando int() en su lugar.

"""

llueve = False
print(type(llueve))
print(llueve)
if llueve:
    print('El día está lluvioso.')
else:
    print('El día está espléndido.')

print()

llueve = not llueve
print(type(llueve))
print(llueve)

if llueve:
    print('El día está lluvioso.')
else:
    print('El día está espléndido.')

print()

# *! Operaciones con variables o valores booleanos (lógicos):

llave_1 = True
llave_2 = False

# *! Operadores lógicos: and (conjunción - y), or (disyunción - o)
print(llave_1 and llave_2)
print(llave_1 and not llave_2)
print(llave_2 or llave_1)
print(llave_2 or not llave_1)

print()

if llave_1 and llave_2:
    print('Sí hay agua')
else:
    print('No hay agua')

print()

if llave_1 and not llave_2:
    print('Sí hay agua')
else:
    print('No hay agua')

print()

if llave_1 or llave_2:
    print('Sí hay agua')
else:
    print('No hay agua')

print()

if not llave_1 or llave_2:
    print('Sí hay agua')
else:
    print('No hay agua')

print()

"""
# *! class bool(x=False)
Retorna un booleano, es decir, o bien True o False. x es convertido usando el estándar truth testing procedure. Si x es falso u omitido, retorna False; en caso contrario retorna True. La clase bool es una subclase de int (véase Tipos numéricos — int, float, complex). De ella no pueden derivarse más subclases. Sus únicas instancias son False y True (véase Boolean Type - bool).

Cualquier número distinto de 0 siempre regresará True.
"""

print('Uso de la clase bool():')
x = bool(1)
print(f'el tipo de x = bool(1) -> {type(x)}')
print(f'el valor de x = bool(1) -> {x}')

print()

x = bool(123)
print(f'x = bool(123): {type(x)}')
print(f'x: {x}')

print()

x = bool(-123)
print(f'x = bool(-123): {type(x)}')
print(f' valor de x: {x}')

print()

x = bool(0)
print(f'El tipo de x = bool(0) -> {type(x)}')
print(f'El calor de x = bool(0) -> {x}')

print()

x = bool('False')
print(f"El tipo de x = bool('False') -> {type(x)}")
print(f"El calor de x = bool('False') -> {x}")

x = bool('True')
print(f"El tipo de x = bool('True') -> {type(x)}")
print(f"El calor de x = bool('True') -> {x}")

print()

x = bool(123 < 124)
print(f"El tipo de x = bool(123 < 124) -> {type(x)}")
print(f"El calor de x = bool(123 < 124) -> {x}")

x = 123 > 124
print(f"El tipo de x = 123 > 124 -> {type(x)}")
print(f"El calor de x = 123 > 124 -> {x}")