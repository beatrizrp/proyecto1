"""
Trabajando con fechas en Python
"""

import time

seconds = time.time()
print('Número de ticks desde las 00:00 del 01 de Enero de 1970', seconds)

# Hora local

local_time = time.localtime(seconds)
print(local_time)
print(type(local_time))

# Hora local formateada

asctime = time.asctime(local_time)
print(asctime)

# Hora con formato personalizado

date_format = '%d-%b-%Y a las %H:%M:%S'
date_formated = time.strftime(date_format, time.gmtime(seconds))
print(date_formated)