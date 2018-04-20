"""
Trabajando con clases y POO (Programación Orientada a Objetos)
"""

class Thing:
    pass

cosa = Thing()

class Fruit:
    def __init__(self):
        print('Objeto fruta iniciado')

fruit = Fruit()

# Argumentos del constructor

class Person:
    """ Esta es la documentación de la clase Person """
    COUNTER = 0

    def __init__(self, name):
        self.name = name
        self.knowledge = []
        Person.COUNTER +=1

    def __str__(self):
        return 'Me llamo {} y sé{}'.format(self.name, self.knowledge)
    
    def learn(self, what):
        self.knowledge.append(what)

p1 = Person('Beatriz')
p2 = Person('Pedro')
p3 = Person('David')
p1.learn("phyton")
p2.learn("javascript")
p3.learn("C#")

print(p1)
print(p2)
print(p3)
print(Person.COUNTER)

