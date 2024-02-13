# Dans ce fichier python sont stoqués toutes les images necessaires au jeu


import pygame

import main_loop
import main_loop


background = pygame.image.load('assets/background.png')         # on crée une variable qui stoque l'arrière plan

icon = pygame.image.load('assets/Logo-du-jeu.png')              # on crée le logo du jeu et on l'applique
icon = pygame.transform.scale(icon, (20, 20))
pygame.display.set_icon(icon)

game_banner = pygame.image.load('assets/game banner.png')
game_banner = pygame.transform.scale(game_banner, (700, 350))       # on crée la bannière du jeu et on la redimensionne

credit = pygame.image.load('assets/credits.png')
credit = pygame.transform.scale(credit, (200, 100))                 # on crée le petit credit du jeu et on le redimensionne

date = pygame.image.load('assets/date.png')                         # on crée la date du jeu
date = pygame.transform.scale(date, (100, 25))

Munsch = pygame.image.load('assets/Munsch.png')                     # on crée le petit message pour Madame Munsch
Munsch = pygame.transform.scale(Munsch, (200, 100))


play_button = pygame.image.load('assets/play button.png')           # on crée le bouton de jeu
play_button = pygame.transform.scale(play_button, (440, 165))
play_button_rect = play_button.get_rect()                           # on crée son rect, une zone où l'on pourra cliquer
play_button_rect.x = 350
play_button_rect.y = 400



settings_button = pygame.image.load('assets/settings button.png')           # on crée le bouton des paramètres
settings_button = pygame.transform.scale(settings_button, (90, 50))
settings_button_rect = settings_button.get_rect()                           # on crée son rect
settings_button_rect.x = 990
settings_button_rect.y = 10

smiley = pygame.image.load('assets/emoji.png')         # on crée le petit émojii
smiley = pygame.transform.scale(smiley, (50, 50))

active_music = pygame.image.load('assets/active music.jpg')         # on crée le bouton d'activation de la musique
active_music = pygame.transform.scale(active_music, (60, 60))       # on crée son rect
active_music_rect = active_music.get_rect()
active_music_rect.x = 930
active_music_rect.y = 7

stop_music = pygame.image.load('assets/stop music.jpg')         # # on crée le bouton stop musique
stop_music = pygame.transform.scale(stop_music, (60, 60))       # on crée son rect
stop_music_rect = stop_music.get_rect()
stop_music_rect.x = 930
stop_music_rect.y = 7

return_button = pygame.image.load('assets/return button.png')         # on crée le bouton de retour1 du jeu
return_button = pygame.transform.scale(return_button, (550, 353))     # on crée son rect
return_button_rect = return_button.get_rect()
return_button_rect.x = 690
return_button_rect.y = 600

Music_1_button = pygame.image.load('assets/Music 1 button.png')         # on crée le bouton de la musique 1 du jeu version non activé
Music_1_button = pygame.transform.scale(Music_1_button, (500, 75))      # on crée son rect
Music_1_button_rect = Music_1_button.get_rect()
Music_1_button_rect.x = 450
Music_1_button_rect.y = 205

Music_2_button = pygame.image.load('assets/Music 2 button.png')         # on crée le bouton de la musique 2 du jeu version non activé
Music_2_button = pygame.transform.scale(Music_2_button, (500, 75))      # on crée son rect
Music_2_button_rect = Music_2_button.get_rect()
Music_2_button_rect.x = 450
Music_2_button_rect.y = 275

Music_3_button = pygame.image.load('assets/Music 3 button.png')         # on crée le bouton de la musique 3 du jeu version non activé
Music_3_button = pygame.transform.scale(Music_3_button, (500, 75))      # on crée son rect
Music_3_button_rect = Music_3_button.get_rect()
Music_3_button_rect.x = 450
Music_3_button_rect.y = 345


Music_1_button_red = pygame.image.load('assets/Music 1 button red.png')         # on crée le bouton de la musique 1 du jeu version activé
Music_1_button_red = pygame.transform.scale(Music_1_button_red, (500, 75))      # on crée son rect
Music_1_button_red_rect = Music_1_button_red.get_rect()
Music_1_button_red_rect.x = 450
Music_1_button_red_rect.y = 205

Music_2_button_red = pygame.image.load('assets/Music 2 button red.png')         # # on crée le bouton de la musique 2 du jeu version non activé
Music_2_button_red = pygame.transform.scale(Music_2_button_red, (500, 75))      # on crée son rect
Music_2_button_red_rect = Music_2_button_red.get_rect()
Music_2_button_red_rect.x = 450
Music_2_button_red_rect.y = 275

Music_3_button_red = pygame.image.load('assets/Music 3 button red.png')         # # on crée le bouton de la musique 3 du jeu version non activé
Music_3_button_red = pygame.transform.scale(Music_3_button_red, (500, 75))      # on crée son rect
Music_3_button_red_rect = Music_3_button_red.get_rect()
Music_3_button_red_rect.x = 450
Music_3_button_red_rect.y = 345



gamemode_choice = pygame.image.load('assets/Gamemode choice.png')       # on crée la bannière de changement de mode de jeu
gamemode_choice = pygame.transform.scale(gamemode_choice, (550, 353))

exercices_button = pygame.image.load('assets/exercices button.png')     # on crée le bouton exercice
exercices_button = pygame.transform.scale(exercices_button, (550, 350)) # on crée son rect
exercices_button_rect = exercices_button.get_rect()
exercices_button_rect.x = 535
exercices_button_rect.y = 170

research_button = pygame.image.load('assets/research button.png')       # on crée le bouton recherche
research_button = pygame.transform.scale(research_button, (550, 353))   # on crée son rect
research_button_rect = research_button.get_rect()
research_button_rect.x = 0
research_button_rect.y = 170

return_button1 = pygame.image.load('assets/return button.png')         # on crée le bouton de retour2 du jeu
return_button1 = pygame.transform.scale(return_button1, (550, 353))    # on crée son rect
return_button1_rect = return_button1.get_rect()
return_button1_rect.x = 690
return_button1_rect.y = 600




research_banner = pygame.image.load('assets/research banner.png')     # on crée la bannière du mode recherche
research_banner = pygame.transform.scale(research_banner, (400, 360))

research_bar = pygame.image.load('assets/Research bar.png')           # on crée la barre de recherche en mode blanc
research_bar = pygame.transform.scale(research_bar, (400, 100))       # on crée son rect
research_bar_rect = research_bar.get_rect()
research_bar_rect.x = 350
research_bar_rect.y = 370

research_bar_blue = pygame.image.load('assets/Research bar blue.png')      # on crée la barre de recherche en mode bleu
research_bar_blue = pygame.transform.scale(research_bar_blue, (400, 100))  # on crée son rect
research_bar_blue_rect = research_bar_blue.get_rect()
research_bar_blue_rect.x = 350
research_bar_blue_rect.y = 370

research_bar_purple = pygame.image.load('assets/Research bar purple.png')      # on crée la barre de recherche en mode violet
research_bar_purple = pygame.transform.scale(research_bar_purple, (400, 100))  # on crée son rect
research_bar_purple_rect = research_bar_purple.get_rect()
research_bar_purple_rect.x = 350
research_bar_purple_rect.y = 370

return_button2 = pygame.image.load('assets/return button.png')          # on crée le bouton de retour2
return_button2 = pygame.transform.scale(return_button2, (550, 353))     # on crée son rect
return_button2_rect = return_button2.get_rect()
return_button2_rect.x = 690
return_button2_rect.y = 600




exercices_banner = pygame.image.load('assets/exercice banner.png')      # on crée la bannière du mode exercice
exercices_banner = pygame.transform.scale(exercices_banner, (400, 350))

return_button3 = pygame.image.load('assets/return button.png')          # on crée le bouton de retour3
return_button3 = pygame.transform.scale(return_button3, (550, 353))     # on crée son rect
return_button3_rect = return_button3.get_rect()
return_button3_rect.x = 690
return_button3_rect.y = 600

exercices_bar = pygame.image.load('assets/Research bar.png')            # on crée la barre de recherche du mode exercice en mode blanc
exercices_bar = pygame.transform.scale(exercices_bar, (400, 100))
exercices_bar_rect = exercices_bar.get_rect()
exercices_bar_rect.x = 350
exercices_bar_rect.y = 370

exercices_bar_blue = pygame.image.load('assets/Research bar blue.png')          # on crée la barre de recherche du mode exercice en mode bleu
exercices_bar_blue = pygame.transform.scale(exercices_bar_blue, (400, 100))     # on crée son rect
exercices_bar_blue_rect = exercices_bar_blue.get_rect()
exercices_bar_blue_rect.x = 350
exercices_bar_blue_rect.y = 370

exercices_bar_purple = pygame.image.load('assets/Research bar purple.png')          # on crée la barre de recherche du mode exercice en mode violet
exercices_bar_purple = pygame.transform.scale(exercices_bar_purple, (400, 100))     # on crée son rect
exercices_bar_purple_rect = exercices_bar_purple.get_rect()
exercices_bar_purple_rect.x = 350
exercices_bar_purple_rect.y = 370

rule = pygame.image.load('assets/Rule.png')         # on crée la régle des majuscules
rule = pygame.transform.scale(rule, (300, 250))

new_question = pygame.image.load('assets/New question.png')     # on crée le bouton nouvelle question
new_question = pygame.transform.scale(new_question, (400, 100))
new_question_rect = new_question.get_rect()
new_question_rect.x = 350
new_question_rect.y = 500

