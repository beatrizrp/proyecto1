"""
Ejemplos para trabajar con diccionarios
"""

ALUMNO = {
    'nombre': 'Beatriz',
    'edad' : 25,
    'clase' : 'python'
}

print(ALUMNO)
print(ALUMNO['nombre'])
print(ALUMNO['edad'])

ALUMNO['edad'] = 22
print(ALUMNO)

ALUMNO['sexo'] = 'femenino'

del ALUMNO['sexo']
print(ALUMNO)

ALUMNO.clear()
print(ALUMNO)