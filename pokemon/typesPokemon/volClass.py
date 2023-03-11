from pokemonClass import *

class Vol(Pokemon):

    def __init__(self, name, lvl) -> None:
        super().__init__(name, lvl)
        self.increasePV((35+lvl))
        self.PA += (20+lvl)
        self.déf += (5)
        self.Type = "Vol"