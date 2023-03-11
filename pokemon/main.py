import sys
sys.path.append('./typesPokemon')
sys.path.append('./settings')
sys.path.append('./GUI')

import time
import pygame
from pygame.locals import *

from typesPokemon.normalClass import * 
from typesPokemon.feuClass import * 
from typesPokemon.eauClass import * 
from typesPokemon.planteClass import * 
from typesPokemon.volClass import *
from typesPokemon.insecteClass import *
from combat import *

from settings.boutons import *
from settings.variables import *
from settings.fonctions import * 


class Pokedex:
    # Création d'un objet Pokedex

    def __init__(self) -> None:
        
        # ficher json
        pokedex_file="./pokedex/pokédex.json"

        # ouvrir le fichier en question
        with open(pokedex_file, 'r') as file:
            pokedex_data = json.load(file)

        # liste de pokemon
        pdex = pokedex_data["Pokemon"]

        font = pygame.font.SysFont(None, 60)

        for pokemon in pdex:
            text = "Consulter le terminal"
            print(pokemon)

        textSurface = font.render(text, False, WHITE)
        rect_textSurface = textSurface.get_rect()
        rect_textSurface.topleft = (50, 50)

        self.running = True

        background = RED

        # Lancer la boucle principale de la fenêtre de combat
        while self.running:
            # condition de sortie de boucle
            for event in pygame.event.get():
                # si la croix (fermer Menu) est cliquée
                if event.type == QUIT:
                    # variable d'état actif passe à l'état inactif
                    self.running = False
                    quit()

                # check si la souris est cliquée
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if back_btn.isOver(mouse):
                        Menu().run()

            
            # éléments à afficher à l'écran du menu Ajouter
            screen.fill(background)
            screen.blit(textSurface, rect_textSurface)
            back_btn.draw(screen, 5)
        
            # stock les coor (x,y) dans une variable sous forme de tuple
            mouse = pygame.mouse.get_pos()
            
            # MAJ affichage de l'écran
            pygame.display.update()

class Game(Combat):
    # Création d'un objet Game (fille de Combat)

    def __init__(self, monPokemon, pokemonAdversaire) -> None:
        super().__init__(monPokemon, pokemonAdversaire)
        
        # affichage de la fenêtre 
        self.screen = pygame.display.set_mode((860, 600))

        monPokemon_text = f"{monPokemon.getName()} / LvL:{monPokemon.getLvl()}"
        pokemonAdversaire_text = f"{pokemonAdversaire.getName()} / LvL:{pokemonAdversaire.getLvl()}"
        combat_text = "VS"
        detailCombat = ""

        # police du texte 
        font = pygame.font.SysFont(None, 60)
        
        # nom de mon pokemon affiché
        monPokemon_img = font.render(monPokemon_text, True, BLACK)
        rect_monPokemon_text = monPokemon_img.get_rect()
        rect_monPokemon_text.topleft = (50, 400)
        #
        # nom du pokemon adverse affiché
        pokemonAdversaire_img = font.render(pokemonAdversaire_text, True, BLACK)
        rect_pokemonAdversaire_text = pokemonAdversaire_img.get_rect()
        rect_pokemonAdversaire_text.topleft = (375, 50)
        #
        # image combat
        combat_img = font.render(combat_text, True, RED)
        rect_combat_text = combat_img.get_rect()
        rect_combat_text.topleft = (350, 200)

        self.running = True

        background = WHITE

        # Lancer la boucle principale de la fenêtre de combat
        while self.running:
            # condition de sortie de boucle
            for event in pygame.event.get():
                # si la croix (fermer Menu) est cliquée
                if event.type == QUIT:
                    # variable d'état actif passe à l'état inactif
                    self.running = False
                    quit()
                # check si la souris est cliquée
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # si le bouton Commencer est cliqué
                    if start_btn.isOver(mouse):
                        # Affichage du message "Fighting" 
                        detailCombat = "Fighting"
                        combat_img = font.render(detailCombat, True, RED)
                        rect_combat_text.topleft = (300, 250)
                        screen.blit(combat_img, rect_combat_text)
                        pygame.display.flip()
                        # Lancement du combat
                        Game.run(self)
                        # Affichage du vainqueur ainsi que du perdant à l'écran
                        combat_text = Game.run(self)
                        combat_img = font.render(combat_text, True, RED)
                        rect_combat_text.topleft = (60, 250)
                        pygame.display.flip()

                    # si le bouton Retour est cliqué, retour au menu précedent
                    if back_btn.isOver(mouse):
                        Start()

            # éléments à afficher à l'écran du menu Ajouter
            screen.fill(background)
            screen.blit(monPokemon_img, rect_monPokemon_text)
            screen.blit(combat_img, rect_combat_text)
            screen.blit(pokemonAdversaire_img, rect_pokemonAdversaire_text)
            start_btn.draw(screen, 5)
            back_btn.draw(screen, 5)
            
            # stock les coor (x,y) dans une variable sous forme de tuple
            mouse = pygame.mouse.get_pos()
            
            # MAJ affichage de l'écran
            pygame.display.update()

class Start:
    # Création d'un objet Start
    
    def __init__(self):
 
        # récupére le pokemon depuis le pokedex 
        pokedex = open("pokedex/pokemon.json", "r")
        pokedexContent = pokedex.read()
        pokemonList = json.loads(pokedexContent)

        # variable texte, invitation à ajouter un nouveau mot
        choose_invite = "Choisi ton Pokemon:"
        # variable pour stocker le Pokemon choisi
        global text
        text = ""

        # police du texte 
        font = pygame.font.SysFont(None, 60)

        # image du mot à ajouter 
        img = font.render(text, True, BLACK)
        rect_text = img.get_rect()
        rect_text.topleft = (20, 100)
        #
        # image du texte d'invitation
        img_invite = font.render(choose_invite, True, BLACK)
        rect_invite = img_invite.get_rect()
        rect_invite.topleft = (20, 20)

        # curseur
        cursor = Rect(rect_text.topright, (3, rect_text.height))

        # variable de vérification d'état (actif/inactif)
        running = True

        # variable arrière plan
        background = WHITE

        # boucle princiale de l'affichage du menu/objet Ajouter
        while running:

            for event in pygame.event.get():
                # si fermeture demandée (bouton croix, alt+f4, ..) 
                if event.type == QUIT:
                    # variable running n'est plus active, retour au menu
                    running = False
                    # pygame.quit()

                # pour tout event du clavier
                if event.type == KEYDOWN:

                    # si la touche "effacer"/"retour en arrière" 
                    if event.key == K_BACKSPACE:

                        # si longueur du mot > à 0
                        if len(text)>0:

                            # effacer le dernier caractère
                            text = text[:-1]
                    # sinon
                    else:
                        # incrémenté au mot tout nouvel event du clavier
                        text += event.unicode

                    # MAJ affichage à l'écran
                    img = font.render(text, True, BLACK)
                    rect_text.size=img.get_size()

                    # curseur
                    cursor.topleft = rect_text.topright

                # check si la souris est cliquée
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # si le bouton ajouter est cliqué
                    if start_btn.isOver(mouse):
                        # pour tout poke dans la liste de Pokemon
                        for poke in pokemonList["Pokemon"]:
                            # Si le pokemon choisi existe dans la liste 
                            if poke["Name"] == text:
                                # Instancier mon pokemon et le pokemon adverse
                                start_game(text)
                                chooseEnemy()
    
                                # Acces à la fenêtre suivante et pourvsuivre vers le combat
                                Game(start_game(text), chooseEnemy())
                        
                        # Sinon
                        else:
                            # Retour au menu précedent
                            Menu().run()
        
                    # si le bouton menu est cliqué
                    if exit_btn.isOver(mouse):
                        # Retour au menu précedent
                        Menu().run()

            # éléments à afficher à l'écran du menu Ajouter
            screen.fill(background)
            screen.blit(img, rect_text)
            # screen.blit(msg_img, rect_msg)
            screen.blit(img_invite, rect_invite)
            start_btn.draw(screen, 5)
            exit_btn.draw(screen, 5)
            # condition de timing pour le curseur
            if time.time() % 1 > 0.5:
                pygame.draw.rect(screen, RED, cursor)
            
            # stock les coor (x,y) dans une variable sous forme de tuple
            mouse = pygame.mouse.get_pos()
            
            # MAJ affichage de l'écran
            pygame.display.update()

class Ajouter_Pokemon:
    # création d'un objet pour le menu Ajouter un Pokemon

    def __init__(self):

        # variable texte, invitation à ajouter un nouveau Pokemon
        add_invite = "Ajouter un Pokemon: (Nom, Type)"
        # variable pour stocker le nouveau Pokemon et son type à ajouter
        text = ""

        # police du texte 
        font = pygame.font.SysFont(None, 60)

        # image du mot à ajouter 
        img = font.render(text, True, WHITE)
        rect_text = img.get_rect()
        rect_text.topleft = (20, 100)

        # image du texte d'invitation
        img_invite = font.render(add_invite, True, WHITE)
        rect_invite = img_invite.get_rect()
        rect_invite.topleft = (20, 20)

        # curseur
        cursor = Rect(rect_text.topright, (3, rect_text.height))

        # variable de vérification d'état (actif/inactif)
        running = True

        # variable arrière plan
        background = GRAY

        # boucle princiale de l'affichage du menu/objet Ajouter
        while running:

            for event in pygame.event.get():
                # si fermeture demandée (bouton croix, alt+f4, ..) 
                if event.type == QUIT:
                    # variable running n'est plus active, retour au menu
                    running = False
                    quit()

                # pour tout event du clavier
                if event.type == KEYDOWN:

                    # si la touche "effacer"/"retour en arrière" 
                    if event.key == K_BACKSPACE:

                        # si longueur du mot > à 0
                        if len(text)>0:

                            # effacer le dernier caractère
                            text = text[:-1]
                    # sinon
                    else:
                        # incrémenté au mot tout nouvel event du clavier
                        text += event.unicode

                    # MAJ affichage à l'écran
                    img = font.render(text, True, WHITE)
                    rect_text.size=img.get_size()

                    # curseur
                    cursor.topleft = rect_text.topright

                # check si la souris est cliquée
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # si le bouton ajouter est cliqué
                    if add_btn.isOver(mouse):
                        # si le mot à ajouter est supérieur à une lettre
                        if len(text)>1:
                            # # le mot à l'écran est ajouté à la liste de pokemon
                            addPokemon(text)
                            # # retour au menu une fois le pokemon ajouté
                            Menu().run()

                    # si le bouton menu est cliqué
                    if exit_btn.isOver(mouse):
                        # retour au menu
                        Menu().run()

            # éléments à afficher à l'écran du menu Ajouter
            screen.fill(background)
            screen.blit(img, rect_text)
            screen.blit(img_invite, rect_invite)
            add_btn.draw(screen, 5)
            exit_btn.draw(screen, 5)
            # condition de timing pour le curseur
            if time.time() % 1 > 0.5:
                pygame.draw.rect(screen, RED, cursor)
            
        # stock les coor (x,y) dans une variable sous forme de tuple
            mouse = pygame.mouse.get_pos()
            
            # MAJ affichage de l'écran
            pygame.display.update()

class Menu:
    # création d'un objet Menu

    def __init__(self) -> None:
        pygame.init()

        # affichage de la fenêtre 
        self.screen = pygame.display.set_mode((860, 600))

        # variable d'état pour derterminer quand le Menu est actif
        self.running = True
    
    def run(self):

        # Lancer la boucle principale du menu
        while self.running:
            # condition de sortie de boucle
            for event in pygame.event.get():
                # si la croix (fermer Menu) est cliquée
                if event.type == QUIT:
                    # variable d'état actif passe à l'état inactif
                    self.running = False
                    quit()

                # check si la souris est cliquée
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # si bouton Jouer est cliqué
                    if play_btn.isOver(mouse):
                        # Accès au menu Start
                        Start()
                    
                    # si bouton Ajouter Pokemon est cliqué
                    if add_pokemon_btn.isOver(mouse):
                        # appel de l'objet Ajouter un pokemon 
                        Ajouter_Pokemon()
                    
                    # si bouton Pokedex
                    if pokedex_btn.isOver(mouse):
                        print("Pokédex : ")
                        # appel de l'objet Pokedex
                        Pokedex()

            # éléments à afficher sur l'écran
            ## fond d'écran
            self.screen.blit(background, (-50, -100))
            # boutons
            play_btn.draw(self.screen, 5)
            add_pokemon_btn.draw(self.screen, 5)
            pokedex_btn.draw(self.screen, 5)

            # stock les coor (x,y) dans une variable sous forme de tuple
            mouse = pygame.mouse.get_pos()

            # MAJ de l'affichage
            pygame.display.update()

        # quitter proprement le programme 
        pygame.quit()

# si le programme est executé directement (et non importé comme module)
if __name__ == "__main__":
    # Lancer le Menu
    Menu().run()