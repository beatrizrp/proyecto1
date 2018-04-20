from colorama import init, Fore, Back, Style
import requests
import msvcrt
import random
init()


class Player:
    def __init__(self, player_id, name, gender, power, lives, gems = 0):
        self.player_id = player_id
        self.name = name
        self.gender = gender
        self.power = power
        self.lives = lives
        self.gems = gems

    def __str__(self):
        return self.name

class FightGame:
    def __init__(self, author, default_lives, default_power):
        self.author = author
        self.last_player_id = 0
        self.default_lives = default_lives
        self.default_power = default_power
        self.players = []

    def run(self):
        print(Fore.BLUE + """  _______  ___   _______  __   __  _______    _______  _______  __   __  _______ 
|       ||   | |       ||  | |  ||       |  |       ||   _   ||  |_|  ||       |
|    ___||   | |    ___||  |_|  ||_     _|  |    ___||  |_|  ||       ||    ___|
|   |___ |   | |   | __ |       |  |   |    |   | __ |       ||       ||   |___ 
|    ___||   | |   ||  ||       |  |   |    |   ||  ||       ||       ||    ___|
|   |    |   | |   |_| ||   _   |  |   |    |   |_| ||   _   || ||_|| ||   |___ 
|___|    |___| |_______||__| |__|  |___|    |_______||__| |__||_|   |_||_______|  by {}""".format(self.author))
   
        print(Fore.WHITE)
        self.__get_players()
        self.__menu()
        # self.__status()

        while True:
            option = msvcrt.getch()
            # print(option)
            if option == b'\x1b': # es la tecla escape
                break
            if option == b'0':
                self.__menu()
            elif option == b'1':
                self.__status()
            elif option == b'2':
                self.__fight() 
            elif option == b'3':
                self.__add_player()

    def __menu(self):
        print('\nAyuda\n')
        print('0. Mostrar ayuda')
        print('1. Status')
        print('2. Luchar')
        print('3. Añadir jugador')
        print('Esc. Salir\n')


    def __status(self):
        print(Fore.WHITE + 'Id'.ljust(5)
         + ' | ' + 'Nombre'.ljust(22)
         + ' | ' + 'Genero'.ljust(10) 
         + ' | ' + 'Vidas'.ljust(7) 
         + ' | ' + 'Poder'.ljust(7) 
         + ' | ' + 'Gemas'.ljust(7))

        print('---------------------------------------------------------------------------')

        players_sorted = sorted(self.players, key=lambda x: x.power, reverse=True)
        players_sorted = sorted(players_sorted, key=lambda x: x.lives, reverse = True)

        for p in players_sorted:
            color = Fore.RED if p.lives <= 0 else Fore.WHITE
            print(color + '{} | {} | {} | {} | {} | {}'.format(
                str(p.player_id).ljust(5),
                p.name.ljust(22), 
                p.gender.ljust(10), 
                str(p.lives).ljust(7), 
                str(p.power).ljust(7), 
                str(p.gems).ljust(7)))
        print(Fore.WHITE + '---------------------------------------------------------------------------')
    
    def __fight(self):

        # current_players = []
        # for x in self.players:
        #     if x.lives > 0:
        #         current_players.append(x)

        # el código de abajo es lo mismo que el de arriba que está comentado
        # esto de abajo se llama Compehensive list de python (lista comprensiva)

        current_players = [x for x in self.players if x.lives > 0]

        # ¿Hay más de un ?

        if len(current_players) < 2:
            print(Fore.RED + 'No hay suficientes jugadores' + Fore.WHITE)
            return
        
        fighters = random.sample(current_players, k=2)
        player1 = fighters[0]
        player2 = fighters[1]
        damage = random.randint(1,6)
        player2.power -= damage
        print(Fore.CYAN + '==> {} le ha zurrado a {}'.format(player1, player2) + Fore.WHITE)

        if player2.power <= 0: # ha perdido una vida
            player2.lives -=1
            player2.power = self.default_power if player2.lives > 0 else 0

            player1.gems += 1
            print(Fore.MAGENTA + '{} ha ganado una gema (tiene{})'.format(player1, player1.gems))

            if player1.gems == 2:
                print(Fore.GREEN + '{} ha ganado una vida (tiene{})'.format(player1, player1.lives))
                player1.gems = 0
                player1.lives += 1

            if player2.lives > 0:
                print(Fore.YELLOW + '{} ha perdido una vida (le quedan {}).'.format(player2, player2.lives)+Fore.WHITE)
            else: # ha muerto
                print(Fore.RED + '{} ha muerto por desgracia.'.format(player2) + Fore.WHITE)

                if len(current_players) <3:
                    print(Fore.LIGHTBLUE_EX + '{} ha ganado el torneo.'.format(player1) + Fore.WHITE)
                    return

            

    def __get_players(self):
        print('Obteniendo jugadores desde la api de Star Wars...')
        response = requests.get('https://swapi.co/api/people')
        people = response.json()['results']
        for person in people:
            self.last_player_id += 1
            player = Player(
                self.last_player_id,
                person['name'],
                person['gender'],
                self.default_power,
                self.default_lives)

            self.players.append(player)
        print('Lista de jugadores preparada')

    def __add_player(self):
        name = ''
        while len(name) < 4:
            name = input('\n Escribe nombre del jugador: ')

        gender = ''
        while len(gender) <3:
            gender = input('\n Escribe género (male/female):')

        self.last_player_id += 1
        player = Player(
                self.last_player_id,
                name,
                gender,
                self.default_power,
                self.default_lives)

        self.players.append(player)
        print(Fore.YELLOW + '{} se ha añadido a la lista de jugadores.'.format(player)+Fore.WHITE)
        



# game = FightGame()
# game.run()
# es igual que lo de abajo

FightGame('Beatriz', 3, 10).run()