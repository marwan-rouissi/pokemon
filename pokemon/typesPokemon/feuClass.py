from pokemonClass import *

class Feu(Pokemon):

    def __init__(self, name, lvl) -> None:
        super().__init__(name, lvl)
        self.increasePV((15+lvl))
        self.PA += (5+lvl)
        self.déf += (5)
        self.Type = "Feu"