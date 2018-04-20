def print_all(*args):
    for n in args:
        print(n)

print_all('pera', 'manzana', 'limon')

def print_all_with_position(*args):
    for count, thing in enumerate(args):
        print('{}. {}'.format(count, thing))

print_all_with_position('pera', 'manzana', 'limon')

count = 0
while True:
    count += 1
    print(count)
    if(count == 100):
        break

count = 200
while count < 250:
    count += 1
    print (count)

def show_keyword_arguments(**kwargs):
    for name, value in kwargs.items():
        print('{}: {}'.format(name, value))

show_keyword_arguments(name='Beatriz', age = 25)