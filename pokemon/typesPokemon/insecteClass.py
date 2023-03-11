from pokemonClass import *

class Insecte(Pokemon):

    def __init__(self, name, lvl) -> None:
        super().__init__(name, lvl)
        self.increasePV((5+lvl))
        self.PA += (12+lvl)
        self.déf += (8)
        self.Type = "Insecte"