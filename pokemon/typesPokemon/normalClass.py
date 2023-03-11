from pokemonClass import *

class Normal(Pokemon):

    def __init__(self, name, lvl) -> None:
        super().__init__(name, lvl)
        self.increasePV((10+lvl))
        self.PA += (3+lvl)
        self.déf += (3)
        self.Type = "Normal"