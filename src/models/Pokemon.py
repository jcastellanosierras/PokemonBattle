class Pokemon:

    def __init__(self, name, types, moves, stats):
        self.name = name
        self.types = types
        self.moves = moves
        self.stats = stats
        # self.nature = nature
        # self.ivs = ivs
        # self.evs = evs
        self.currentHP = stats['hp']
        self.state = None

    def is_defeated(self):
        return self.currentHP == 0

