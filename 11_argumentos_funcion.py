"""
Diferentes maneras de usar argumentos
"""

# argumentos posicionales
def hi(name):
    print('hola', name)

#hi() <-- Esto falla porque name es obligatorio

# valores por defecto
def f(n='uno'):
    print(n)

f() #coge el 'uno' como valor por defecto
f(2)


def f2(one, two, three=3):
    print('one:', one, 'two:', two, 'three:', three)

f2('Pepe', 'Lola, 45')

# usar argumentos como keyword
f2(
    three='Carmen',
    one='Pedro',
    two='Sara'
)

def f3(name, *args):
    print('hola', name)
    print(args)

f3('Pedro', 20, 30, 40, True, False, 'hola')

t =('Pedro', 20, 30, 40, True, False, 'hola')

f3('Beatriz', t)

def f4(*args): # <-- Hace una tupla
    print(args)

f4('uno')
f4('uno', 2, 3, 4)
f4(True, False)

def f5(**kwars):    # <-- para keywords
    print(kwars)

f5(nombre='Beatriz', edad = 25, clase = 'python')

O = {'nombre' : 'Beatriz', 'edad' : 25, 'clase' : 'python'}
f5(**O)