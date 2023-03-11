from pokemonClass import *

class Plante(Pokemon):

    def __init__(self, name, lvl) -> None:
        super().__init__(name, lvl)
        self.increasePV((30+lvl))
        self.PA += (4+lvl)
        self.déf += (3)
        self.Type = "Plante"