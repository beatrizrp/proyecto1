"""
Ejemplos de cómo importar módulos y funciones en python
"""

import utils # importamos el módulo entero

utils.sumar(6, 8)
utils.restar(10, 4)

from utils import sumar # para solo importar el método sumar

sumar(2, 2)

from libs import bombing # importamos todo el módulo

bombing.where_are_the_bombs()

from libs.bombing import where_are_the_bombs, explosion # importamos las funciones de manera individual

where_are_the_bombs()

from libs.bombing import * # importamos todo
explosion()