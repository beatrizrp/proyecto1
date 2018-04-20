from colorama import init, Fore, Back, Style
init()

print('hola')
print(Fore.BLUE + 'Esto es azul')
print(Fore.CYAN + 'Más cosas')
print(Fore.RED + 'Esto es rojo')

print(Back.GREEN + 'Fondo verde')
print(Style.RESET_ALL) # para resetear
print('hola')
