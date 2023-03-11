class Pokemon:
    def __init__(self, name, lvl) -> None:
        self.type = self.__class__
        self.__name = name
        self.__PV = 100
        self.lvl = lvl
        self.PA = 10
        self.déf = 0
    
    def getName(self):
        return self.__name

    def getLvl(self):
        return self.lvl

    def getPV(self):
        return self.__PV
    
    def increasePV(self, PvtoAdd):
        self.__PV += PvtoAdd
    
    def decreasePV(self, PvtoRemove):
        self.__PV -= PvtoRemove
    
    def gT(self):
        return self.Type

    def displayInfo(self):
        print(f"Pokemon: {self.__name}")
        print(f"lvl: {self.lvl}")
        print(f"{self.__PV} PV")
        print(f"{self.PA} PA")
        print(f"{self.déf} déf.")