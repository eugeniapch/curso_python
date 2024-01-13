'''
Ejercicio 4.2: Mostrar en pantalla la fecha y hora actuales del sistema.
'''

import datetime
from datetime import timedelta, date

ahora = datetime.datetime.now()

print('Fecha y hora actuales:', ahora)

print(type(ahora))

print()

ahora_formato = ahora.strftime('%H:%M:%S %d-%m-%Y')

print(ahora_formato)

print(f'timezone {datetime.timezone}')


delta = timedelta(days = 50, seconds = 27, microseconds = 10, milliseconds = 29000,
                  minutes = 5, hours = 8, weeks = 2)
print(f'delta: {delta}')

print(f'isoformat: {date(2024, 1, 12).isoformat()}')