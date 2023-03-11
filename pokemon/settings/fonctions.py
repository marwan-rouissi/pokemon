import json
import random
# Importer tout les fichiers de types pokemon nécessaire au combat
from typesPokemon.normalClass import * 
from typesPokemon.feuClass import * 
from typesPokemon.eauClass import * 
from typesPokemon.planteClass import * 
from typesPokemon.volClass import * 
from typesPokemon.insecteClass import * 



# fonction ajouter un pokemon
def addPokemon(text):

    # ficher json
    pokedex_file="./pokedex/pokemon.json"

    # variable dans laquelle stocker les pokemon
    pokemonList = {}

    # nom = la substring de la string (text) avant la virgule
    nom = text.partition(", ")[0]
    # Type = la substring de la string (text) après la virgule
    Type = text.partition(", ")[2]

    # le pokemon à enregistrer
    data = {
            "Name": nom,
            "Type": Type,
            }
    

    # ouvrir le fichier en question
    with open(pokedex_file, 'r') as file:
        pokedex_data = json.load(file)

    # ajouter le pokemon à la liste d'éléments récupérés depuis le fichier .json    
    
    pokemonList["Pokemon"] = [data]
    pokedex_data["Pokemon"] += pokemonList["Pokemon"]

    # réécrire par dessus le fichier .json en le remplacant par la nouvelle variable incluants les éléments récupérés + le pokemon à ajouter    
    with open(pokedex_file, "w") as file:
        json.dump(pokedex_data, file, indent=4)

# fonction pour choisir son pokemon
def start_game(text):

    # Les lignes commentées suivantes étaient pertinantes et utiles pour le jeu via termial, elle sont obsolètes avec et pour l'interface graphique

    # Invite l'utilisateur à choisir son pokemon et son lvl
    # print("Choisi ton pokemon:")
    # pokemon = input()
    # print("Choisir son lvl")
    # global lvl
    # lvl = int(input())
    pokemon = text

    # récupére le pokemon depuis le pokedex 
    pokedex = open("pokedex/pokemon.json", "r")
    pokedexContent = pokedex.read()
    pokemonList = json.loads(pokedexContent)
    
    global monPokemonlvl
    monPokemonlvl = random.choice(range(100))

    # Invite l'utilisateur à choisir un nouveau pokemon si le choix précedent n'est pas valide
    while pokemon not in pokedexContent:
        print("Pokemon non valide. Choisir un pokemon valide.")
        pokemon = input()
        # print("Choisir son lvl")
        # lvl = int(input())

    # sinon, récupère les éléments necessaires pour instancier un pokemon (son nom et son type) et les stocke dans une variable 
    else:   
        for p in pokemonList["Pokemon"]:

            if  pokemon == p["Name"]:
                global name 
                name = p["Name"]
                print(p)
                global t
                t = p["Type"] 
                if t == "Normal":
                    t = Normal
                if t == "Feu":
                    t = Feu
                if t == "Eau":
                    t = Eau
                if t == "Plante":
                    t = Plante
                if t == "Vol":
                    t = Vol
                if t == "Insecte":
                    t = Insecte
    
    # Instancier mon pokemon et afficher ses info
    
    monPokemon = t(name, monPokemonlvl)
    return monPokemon

# fonction pour choisir un pokemon adversaire random depuis le pokedex
def chooseEnemy():
    pokedex = open("pokedex/pokemon.json", "r")
    pokedexContent = pokedex.read()
    pokemonList = json.loads(pokedexContent)

    global enemylvl
    enemylvl = random.choice(range(100))

    enemyPoke = random.choice(pokemonList["Pokemon"])
    global enemyName
    enemyName = enemyPoke["Name"]
    global enemyType
    enemyType = enemyPoke["Type"]


    if enemyType == "Normal":
        enemyType = Normal
    if enemyType == "Feu":
        enemyType = Feu
    if enemyType == "Eau":
        enemyType = Eau
    if enemyType == "Plante":
        enemyType = Plante
    if enemyType == "Vol":
        enemyType = Vol
    if enemyType == "Insecte":
        enemyType = Insecte
    
    # Instancier le pokemon adverse et afficher ses info
    pokemonAdversaire = enemyType(enemyName, enemylvl)
    return pokemonAdversaire