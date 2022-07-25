from models import Pokemon, Battle
from utils import constants

ascuas = {
    'name': 'Ascuas',
    'type': constants.fire,
    'power': 40,
    'precision': 100
}

arañazo = {
    'name': 'Arañazo',
    'type': constants.normal,
    'power': 40,
    'precision': 100
}

latigo_cepa = {
    'name': 'Látigo Cepa',
    'type': constants.plant,
    'power': 45,
    'precision': 100
}
if __name__ == '__main__':

    pokemon_one = Pokemon.Pokemon(
        'Charmander',
        'Fire',
        [ascuas, arañazo],
        {'hp': 20}
    )

    pokemon_two = Pokemon.Pokemon(
        'Bulbasaur',
        'Plant',
        [latigo_cepa, arañazo],
        {'hp': 25}
    )

    battle = Battle.Battle(pokemon_one, pokemon_two)
    battle.start()