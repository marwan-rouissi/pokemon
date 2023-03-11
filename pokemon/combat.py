import sys
sys.path.append('./typesPokemon')
sys.path.append('./pokedex')
import random
import time
import json
from os.path import exists

# Importer tout les fichiers de types pokemon nécessaire au combat
from typesPokemon.normalClass import * 
from typesPokemon.feuClass import * 
from typesPokemon.eauClass import * 
from typesPokemon.planteClass import * 
from typesPokemon.volClass import * 
from typesPokemon.insecteClass import * 

class Combat():
    # création d'un objet combat

    def __init__(self, monPokemon, pokemonAdversaire) -> None:
        self.monPokemon = monPokemon
        self.pokemonAdversaire = pokemonAdversaire
        self.finDuCombat = False
        self.turn = 1

    # verifier is l'un des 2 pokemon est battu
    def checkEndFight(self):
        if self.monPokemon.getPV() <= 0 or self.pokemonAdversaire.getPV() <= 0:
            return True

    # retourner le nom du pokemon vainqueur
    def getWinner(self):
        # if self.checkEndFight():
            if self.monPokemon.getPV() <= 0:
                return self.pokemonAdversaire.getName()
            if self.pokemonAdversaire.getPV() <= 0:
                return self.monPokemon.getName()
    
    # chance de toucher l'adversaire
    def hit(self):
        chance = random.choice(range(2))
        if chance == 1:
            return True
        else:
            return False
    
    # récupérer le type du pokemon adverse
    def getType(self):
        return self.pokemonAdversaire.type
    
    # determiner la puissance des attaques face au pokemon adverse en fonction du type
    def getStrength(self):
        if self.monPokemon.type == Feu:
            if self.getType() == Eau:
                self.monPokemon.PA *= 0.5
            elif self.getType() == Plante:
                self.monPokemon.PA *= 2
            else:
                self.monPokemon.PA *= 1
        elif self.monPokemon.type == Eau:
            if self.getType() == Plante:
                self.monPokemon.PA *= 0.5
            elif self.getType() == Feu:
                self.monPokemon.PA *= 2
            else:
                self.monPokemon.PA *= 1
        elif self.monPokemon.type == Plante:
            if self.getType() == Feu:
                self.monPokemon.PA *= 0.5
            elif self.getType() == Eau:
                self.monPokemon.PA *= 2
            else:
                self.monPokemon.PA *= 1
        elif self.monPokemon.type == Normal:
            if self.getType() == Feu:
                self.monPokemon.PA *= 0.75
            elif self.getType() == Eau:
                self.monPokemon.PA *= 0.75
            elif self.getType() == Plante:
                self.monPokemon.PA *= 0.75
            else:
                self.monPokemon.PA *= 1
        
        return self.monPokemon.PA

    # soustraire les PV après coups (si l'attaque est un succès)
    def removePV(self):
        if self.hit():
            if self.turn == 1:
                # si tour de mon pokemon
                damage =  self.monPokemon.PA - self.pokemonAdversaire.déf
                # self.pokemonAdversaire.decreasePV(self.monPokemon.PA)
                self.pokemonAdversaire.decreasePV(damage)
                print(f"{self.monPokemon.getName()} attaque")
                self.turn = 2
            if self.turn == 2:
                damage = self.pokemonAdversaire.PA - self.monPokemon.déf
                # self.monPokemon.decreasePV(self.pokemonAdversaire.PA)
                self.monPokemon.decreasePV(damage)
                print(f"{self.pokemonAdversaire.getName()} attaque")
                self.turn = 1
        else:
            print("L'attaque a échoué")
    
    # récupérer le nom du perdant
    def getLoser(self):
        # if self.checkEndFight():
            if self.monPokemon.getPV() <= 0:
                return self.monPokemon.getName()
            if self.pokemonAdversaire.getPV() <= 0:
                return self.pokemonAdversaire.getName()
    
     # fonction pour enregistrer les mdp vadilés en format .json
    def registerPokedex(self):
        # ficher json
        pokedex_file="./pokedex/pokédex.json"
        # variable de verification si le fichier existe déjà ou non
        file_exist = exists(pokedex_file)
        # variable dans laquelle stocker les mdp
        pokemonList = {}
        # le pokemon à enregistrer

        data = {
                "Name": self.pokemonAdversaire.getName(),
                "Type": self.pokemonAdversaire.Type,
                "Atq.": self.pokemonAdversaire.PA,
                "Def.": self.pokemonAdversaire.déf,
                "LvL": self.pokemonAdversaire.getLvl()
                }
        
        # si le fichier .json existe déjà
        if file_exist:
            # ouvrir le fichier en question
            with open(pokedex_file, 'r') as file:
                pokedex_data = json.load(file)
                # print(pokedex_data["Pokemon"])

                # pour pour les éléments récupérés depuis le fichier
                for element in pokedex_data["Pokemon"]:
            
                    # si l'élément en question est identique à l'élement que l'on souhaite ajouter
                    if element["Name"] == data["Name"]:
                        
                        # arrêter là
                        break

                # # sinon ajouter le pokemon à la liste d'éléments récupérés depuis le fichier .json    
                else:
                    pokemonList["Pokemon"] = [data]
                    pokedex_data["Pokemon"] += pokemonList["Pokemon"]

                # réécrire par dessus le fichier .json en le remplacant par la nouvelle variable incluants les éléments récupérés + le pokemon à ajouter    
                with open(pokedex_file, "w") as file:
                    json.dump(pokedex_data, file, indent=4)
                
        # si le fichier .json n'existe pas                
        else:
            # le créer avec pour object le 1er pokemon à ajouter
            with open(pokedex_file, 'w') as file:
                pokemonList["Pokemon"] = [data]
                json.dump(pokemonList, file, indent=4)

    # méthode qui lance et fait tourner le combat
    def run(self):
        self.getStrength()
        while self.finDuCombat == False and self.checkEndFight() != True:
            
            self.hit()
            self.removePV()
            
            print(f"Mon Pokemon: {self.monPokemon.getName()} / {self.monPokemon.getPV()} PV")
            print(f"Pokemon adverse: {self.pokemonAdversaire.getName()} / {self.pokemonAdversaire.getPV()} PV")
            time.sleep(1)

        print(f"{self.getLoser()} K.O")
        print(f"{self.getWinner()} a gagné !")
        self.registerPokedex()
        return f"{self.getLoser()} K.O - {self.getWinner()} a gagné "
    
# Les lignes commentées suivantes étaient pertinantes et utiles pour le jeu via termial, elle sont obsolètes avec et pour l'interface graphique

# # lancer une partie
# start_game()

# # determiner le pokemon adverse
# chooseEnemy()

# Instancier mon pokemon et afficher ses info
# monPokemon = t(name, monPokemonlvl)
# monPokemon = Feu("Salameche", 5)
# monPokemon.displayInfo()

# Instancier le pokemon adverse et afficher ses info
# pokemonAdversaire = enemyType(enemyName, enemylvl)
# pokemonAdversaire.displayInfo()


# Instancier un combat
# combat = Combat(monPokemon, pokemonAdversaire)

# # Lancer le combat
# combat.run()