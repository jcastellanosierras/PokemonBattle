import random


class Battle:

    def __init__(self, pokemon_one, pokemon_two):
        self.turn = 1
        self.modify = None
        self.pokemon_one = pokemon_one
        self.pokemon_two = pokemon_two
        self.winner = None

    def is_finished(self):
        finished = False
        if self.pokemon_one.is_defeated():
            self.winner = 'two'
            finished = True

        if self.pokemon_two.is_defeated():
            self.winner = 'one'
            finished = True

        return finished

    def choose_move(self):
        cont = 1
        for move in self.pokemon_one.moves:
            print(cont, '. ', move["name"])
            cont += 1

        print("Elige un movimiento: ")
        move = int(input())
        while move < 1 or move > len(self.pokemon_one.moves):
            print("Elige un movimiento: ")
            move = int(input())

        return self.pokemon_one.moves[move - 1]

    def start(self):
        print('Estamos en el turno', self.turn)
        while not self.is_finished():
            move = self.choose_move()
            print('Has usado el movimiento', move["name"])
            move_pkm_two = random.randint(0, len(self.pokemon_two.moves))
            print('El rival ha usado el movimiento', self.pokemon_two.moves[move_pkm_two]["name"])
            self.turn += 1

        if self.winner == 'one':
            print('El ganador es', self.pokemon_one.name)
        else:
            print('El ganador es', self.pokemon_two.name)

        return 0
