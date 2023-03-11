import pygame

from settings.boutons import *

# pygame.font.init()

# définition d'une variable pour la fênetre d'affichage
screen = pygame.display.set_mode((860,600))

# variable couleurs
BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255,255,255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# variable arrière plan
background = pygame.image.load("./img/menuBG.png")

# variables boutons 

play_btn = Button(WHITE, 330, 300, 160, 80, "Jouer")
add_pokemon_btn = Button(WHITE, 180, 400, 480, 80, "Ajouter un Pokemon")
pokedex_btn = Button(WHITE, 315, 500, 200, 80, "Pokédex")

add_btn = Button(WHITE, 200, 500, 190, 80, "Ajouter")
exit_btn = Button(WHITE, 640, 500, 180, 80, "Sortir")
back_btn = Button(WHITE, 640, 500, 180, 80, "Retour")

start_btn = Button(WHITE, 200, 500, 270, 80, "Commencer")
