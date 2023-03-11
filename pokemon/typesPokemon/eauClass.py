from pokemonClass import *

class Eau(Pokemon):

    def __init__(self, name, lvl) -> None:
        super().__init__(name, lvl)
        self.increasePV((15+lvl))
        self.PA += (3+lvl)
        self.déf += (4)
        self.Type = "Eau"