import pygame
import numpy as np
import time
from os import listdir
from os.path import isfile, join


pygame.init() 

# Système d'import de niveaux via des fichiers .txt
def get_available_levels(mode="all"):
    base_levels = [f for f in listdir("system/base_levels") if isfile(join("system/base_levels/", f))]
    custom_levels = [f for f in listdir("system/custom_levels") if isfile(join("system/custom_levels/", f))]
    custom_levels.sort()
    if mode == "all":
        return base_levels+custom_levels
    elif mode == "base_levels":
        return base_levels
    elif mode == "custom_levels":
        return custom_levels


def create_level(level_path):

    level_in_list = []
    with open(level_path, "r") as level_file:
        i=0
        for lign in level_file:
            lign = lign.replace("\n", "") # on supprimer les \n à la fin

            level_in_list.append([])
            for element in lign.split(" "):
                level_in_list[i].append(element)
            i += 1
    
    level = np.array(level_in_list)
    return level


pygame.display.set_caption("Jeu du Sokoban - Félix.dev")
screen = pygame.display.set_mode((1200,800))

background = pygame.image.load('system/images/background.png')           # on crée l'arrière plan
background = pygame.transform.scale(background, (1300, 800))

return_button = pygame.image.load('system/images/return.png')           # on crée le bouton retour
return_button = pygame.transform.scale(return_button, (100, 100))
return_button_rect = return_button.get_rect()                           # on crée son rect
return_button_rect.x = 990
return_button_rect.y = 10

play_button = pygame.image.load('system/images/return.png')                                     # on crée le bouton Jouer
play_button = pygame.transform.scale(play_button, (100, 100))
play_button_rect = play_button.get_rect()                               # on crée son rect
play_button_rect.x = 990
play_button_rect.y = 10

running = True
while running:
    screen.blit(background, (0, 0))     # on affiche le boutton des paramètres
    screen.blit(play_button, (0, 0))     # on affiche le boutton des paramètres
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()