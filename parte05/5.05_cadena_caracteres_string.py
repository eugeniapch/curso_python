""" 
# *! Tipo de dato compuesto string

La información textual se representa en Python con objetos de tipo str, normalmente llamados cadenas de caracteres o simplemente strings. Las cadenas de caracteres son secuencias inmutables de puntos de código Unicode. 

Las cadenas se pueden definir de diferentes maneras:
    * Comillas simples: 'permite incluir comillas "dobles"'
    * Comillas dobles: "permite incluir comillas 'simples'"
    * Triples comillas: ya sea con comillas simples '''Triples comillas simples''' o dobles. 

Las cadenas definidas con comillas tripes pueden incluir varias líneas - todos los espacios en blancos incluidos se incorporan a la cadena de forma literal.

"""

nombre = 'Maria Eugenia Pereira'
email = "eugeniapch@gmail.com"
direccion = '''Carretera Norte km. 8 1/2. Subasta 1 1/2 c.al norte.
Managua Nicaragua 
GMT-05
'''

print(type(nombre))
print(nombre)

print()

mensaje = 'Bienvenido(a), ' + nombre + '. Correo: ' + email
print(type(mensaje))
print(mensaje)

print()


# *! Técnicas para mostrar cadenas de carácteres o secuencias de caracteres
  

# ** Interpolación
mensaje = f'Bienvenido(a), {nombre}. Correo: {email}'
print(mensaje)


# ** Método format() de la clase str:
mensaje = 'Bienvenido(a), {}. Correo: {}'.format(nombre, email)
print(mensaje)

# ** Método específicación de formato con %.
# usamos %s porque es un string
mensaje = 'Bienvenido(a), %s. Correo: %s' % (nombre, email)
print(mensaje)

print()


# *! Inmutabilidad de cadenas de caracteres (str) (son estáticos)


lenguaje = "Python"
print(lenguaje)
print(lenguaje[0])
print(lenguaje[1])
print(lenguaje[2])
print(lenguaje[3])
print(lenguaje[4])
print(lenguaje[5])

print()

# No se puede modificar la cadena
# lenguaje[0] = 'p' # TypeError

# Tendriamos que crear una cadena nueva y asignarla a la misma variable
lenguaje = 'p' + lenguaje[1:]
print(lenguaje)


# Verificando el id de memoria de la cadena.
print(id('python') == id('python'))



""" 
class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
Retorna una representación en forma de cadena de caracteres de object. Si no se proporciona ningún valor, retorna una cadena vacía. Si se proporciona, el comportamiento de str() depende de los valores pasados en los parámetros encoding y errors, como veremos

# *? Métodos de las cadenas de caracteres str
https://docs.python.org/es/3/library/stdtypes.html#str

str.capitalize() -> Retorna una copia de la cadena con el primer carácter en mayúsculas y el resto en minúsculas
* str.casefold() -> Retorna el texto de la cadena, normalizado a minúsculas. Los textos así normalizados pueden usarse para
                    realizar búsquedas textuales independientes de mayúsculas y minúsculas.
str.center(width[, fillchar]) -> Retorna el texto de la cadena, centrado en una cadena de longitud width.
str.count(sub[, start[, end]]) -> Retorna el número de ocurrencias no solapadas de la cadena sub en el rango [start, end]. 
str.encode(encoding='utf-8', errors='strict') -> Return the string encoded to bytes.
* str.endswith(suffix[, start[, end]]) -> Retorna True si la cadena termina con el suffix especificado y False en caso contrario.
str.expandtabs(tabsize=8) -> Retorna una copia de la cadena, con todos los caracteres de tipo tabulador reemplazados por uno o 
                            más espacios, dependiendo de la columna actual y del tamaño definido para el tabulador. 
* str.find(sub[, start[, end]]) -> Retorna el menor índice de la cadena s donde se puede encontrar la cadena sub, 
                                    considerando solo el intervalo s[start:end]. Los parámetros opcionales start y end se interpretan como notación de segmento. Retorna -1 si no se encuentra la cadena.
str.format(*args, **kwargs) 
str.format_map(mapping) -> Similar a str.format(**mapping), pero se usa mapping de forma directa y no se copia a un diccionario.
str.index(sub[, start[, end]]) -> Como find(), pero lanza una excepción de tipo ValueError si no se encuentra la cadena a buscar.
str.isalnum() -> Retorna True si todos los caracteres de la cadena son alfanuméricos y hay, al menos, un carácter.
str.isalpha() -> Devuelve Verdadero si todos los caracteres de la cadena son alfabéticos y hay al menos un carácter.
str.isascii() -> Retorna True si la cadena de caracteres está vacía, o si todos los caracteres de la cadena son ASCII
str.isdecimal() -> Retorna True si todos los caracteres de la cadena son caracteres decimales y hay
str.isdigit() -> Retorna True si todos los caracteres de la cadena son dígitos y hay, al menos, un carácter.
str.isidentifier() -> Retorna True si la cadena de caracteres es un identificador válido de acuerdo a la especificación del lenguaje
str.islower() -> Retorna True si todos los caracteres de la cadena que tengan formas en mayúsculas y minúsculas, 
                están en minúsculas y hay, al menos, un carácter de ese tipo
str.isnumeric() -> Retorna True si todos los caracteres de la cadena son caracteres numéricos y hay, al menos, un carácter.
str.isprintable() -> Retorna True si todos los caracteres de la cadena son imprimibles o si la cadena está vacía.
str.isspace() -> Retorna True si todos los caracteres de la cadena son espacios en blanco y hay, al menos, un carácter.
str.istitle() -> Retorna True si las palabras en la cadena tiene forma de título y hay, al menos, un carácter.
str.isupper() -> Retorna True si todos los caracteres de la cadena que tengan formas en mayúsculas y minúsculas están en mayúsculas
                y hay, al menos, un carácter de ese tipo.
str.join(iterable) -> Retorna una cadena de caracteres formada por la concatenación de las cadenas en el iterable
str.ljust(width[, fillchar]) -> Retorna el texto de la cadena, justificado a la izquierda en una cadena de longitud width. 
                            El carácter de relleno a usar viene definido por el parámetro fillchar (por defecto se usa el carácter espacio ASCII). Si la cadena original tiene una longitud len(s) igual o superior a width, se retorna el texto sin modificar.
* str.lower() -> Retorna una copia de la cadena de caracteres con todas las letras en minúsculas
str.lstrip([chars]) -> 
static str.maketrans(x[, y[, z]]) -> Este método estático retorna una tabla de traducción apta para ser usada
                                    por el método str.translate().
str.partition(sep) -> Retorna una copia de la cadena, eliminado determinados caracteres si se encuentren al principio. 
str.removeprefix(prefix, /) -> 
str.removesuffix(suffix, /) -> 
str.replace(old, new[, count]) -> 
str.rfind(sub[, start[, end]]) -> 
str.rindex(sub[, start[, end]]) -> 
str.rjust(width[, fillchar]) -> 
str.rpartition(sep) -> 
str.rsplit(sep=None, maxsplit=-1) -> 
str.rstrip([chars]) -> 
* str.split(sep=None, maxsplit=-1) -> 
* str.splitlines(keepends=False) -> 
str.startswith(prefix[, start[, end]]) -> 
str.strip([chars]) -> 
str.swapcase() -> 
str.title() -> 
str.translate(table) -> 
str.upper() -> 
str.zfill(width) -> 

"""


# *! str.lower() -> Retorna una copia de la cadena de caracteres con todas las letras en minúsculas
lenguaje = 'Python'
print(f'método lower() a Python: {lenguaje} aplicando el método -> {lenguaje.lower()}')

print()

# *! str.split(sep=None, maxsplit=-1) -> Retorna una lista con las palabras que componen la cadena de caracteres original, usando como separador el valor de sep. Si se utiliza el parámetro maxsplit, se realizan como máximo maxsplit divisiones, retornando los que están más a la derecha. Si no se especifica sep o se pasa con valor None, se usa como separador cualquier carácter de espacio en blanco. Si no contamos la diferencia de empezar las divisiones desde la derecha, el comportamiento de este método rsplit() es equivalente al de split(), que se describe con detalle más adelante.

valores = '2,3,5,7,11'
numeros = valores.split(',')

print(f'La variable contiene {valores}')
print(f'Usando split -> {numeros} con longitud {len(numeros)}')
print(type(numeros[0]))

print()

# *! Uso del método str.find()
indice = valores.find('2')
print('El índice del elemento "2" es igual a', indice)

indice = valores.find('1') # encuentra el 1 del valor 11
print('El índice del elemento "1" es igual a', indice)

indice = valores.find('8')
print('El índice del elemento "8" es igual a', indice)

print()

# Creación de una función (proceso) personalizado para buscar una cadena dentro de otra:
def encontrar(cadena, caracter):
    indice = -1
    for i in range(0, len(cadena)):
        if caracter == cadena[i]:
            indice = i
            break
    
    return indice

indice = encontrar(valores, '2')
print('El índice del elemento "2" es igual a', indice)
indice = encontrar(valores, '8')
print('El índice del elemento "8" es igual a', indice)
print()

# *! str.casefold()
cadena = "Maria Eugenia Pereira"
print(f'casefold() -> {cadena.casefold()}')

# *! Vamos a ilustrar el método str.endswith() 
cadena = 'Maria Gabriela le gusta comer queso'
result = cadena.endswith('queso')
print(f'Texto original: {cadena}')
print(f'aplicando endswith():{result}')


