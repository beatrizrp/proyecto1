"""
Operadores de comparación
"""

a = 21
b = 10
c = 0

if a == b:
    print('a == b')
else:
    print('a no es igual a b')

if a != b:
    print('a no es igual b')
else:
    print ('a es igual a b')

print( a < b)
print (a > b)

ES_MAYOR = a > b
print(type(ES_MAYOR))

print (a <= b)
print (a >= b)
print (a is b)

d = 5
f = 5

print(d is f)
print (d is not f)