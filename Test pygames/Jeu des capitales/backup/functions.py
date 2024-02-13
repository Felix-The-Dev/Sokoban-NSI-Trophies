# Dans ce fichier sont stoquées toutes les fonctions necessaires au jeu  (add, print_text, detect_text)

# C'est le fichier via lequel on lance le jeu en effet à cause d'une erreur python pour l'import des fonctions ci dessous
# dans le fichier main_loop, j'ai du lancer le jeu par ici et importer d'ici le code principal, les fonctions étant acceptées
# car elles sont contenue dans le fichier lanceur du jeu.


from time import *
import pygame   # on importe pygame
import main_loop    # on importe le fichier/module main_loop
from main_loop import *

##################################################################################################################################################



def add(pays, capitale, genre, dbl_lettre=True): # expliqué dans le docstring
    """Cette fonction permet d'ajouter un pays et sa capitale au jeu. On entre en première valeur le pays à ajouter, en
                 deuxième valeur la capitale à ajouter et en troisième valeur le genre du pays (m, n, f)
                                        [pour le déterminant des questions]"""

    main_loop.countries_list.append(pays)                # on ajoute le pays à la liste des pays à l'aide de la méthode .append
    main_loop.capital_list.append(capitale)              # on ajoute le capitales à la liste des capitales

    main_loop.countries_gender_list.append(genre)        # le genre des pays détermine si l'on dit "de la France"(f), "du Portugal"(m)
                                                         # ou "de l'Espagne"(n)
    main_loop.can_question.append(dbl_lettre)         # pour les doubles lettres



##################################################################################################################################################



def print_text(letter, area, size=40, color=(0, 0, 0), font="arial"):
    """" Cette fonction permet d'afficher une lettre. On entre en première valeur la lettre à afficher
                et en deuxième valeur la zone dans laquelle afficher cette lettre avec (x, y).
            La fonction prend en valeur optionnelle la taille, la couleur (code RGB) et la police """



    police = pygame.font.SysFont(font, size)                    # on crée une police pour écrire du texte
    image_texte = police.render(letter, False, color)           # on crée une variable qui stoquera l'image du texte
    main_loop.screen.blit(image_texte, area)                    # on affiche le texte



##################################################################################################################################################



def detect_text():
    """Cette fonction permet de détecter si une lettre a été pressée et renvoie cette lettre
                            (les majuscules sont prises en compte)"""


    keys = pygame.key.get_pressed()             # on définit une variable comme l'évent pygame "touche pressée"
    lettre = ""     # la variable lettre sera renvoyée


    if keys[K_LCTRL]:
        main_loop.ctrl = True
        main_loop.color_bar = main_loop.color_bar2 = 2

    elif not main_loop.click:                             # on crée une condition pour afficher la barre en violet si la touche
        main_loop.ctrl = False                            # control est préssée
        main_loop.color_bar = main_loop.color_bar2 = 0

    else:
        main_loop.ctrl = False
        main_loop.color_bar = main_loop.color_bar2 = 1



    if keys[K_LSHIFT]:
        maj = True
                                                # on crée un condition pour déterminer si il faut afficher une majuscule
    else:
        maj = False

    liste_de_clefs = [keys[K_a], keys[K_b], keys[K_c], keys[K_d], keys[K_e], keys[K_f], keys[K_g], keys[K_h], keys[K_i], keys[K_j],
                      keys[K_k], keys[K_l], keys[K_m], keys[K_n], keys[K_o], keys[K_p], keys[K_q], keys[K_r], keys[K_s], keys[K_t],
                      keys[K_u], keys[K_v], keys[K_w], keys[K_x], keys[K_y], keys[K_z], keys[K_AT], keys[K_2]]
    # listes pour la boucle qui suit
    liste_de_lettres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "k", "r",
                        "s", "t", "u", "v", "w", "x", "y", "z", "à", "é"]

    liste_de_MAJUSCULES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                            "S", "T", "U", "V", "W", "X", "Y", "Z"]

    if maj:                                        # on crée une condition pour affecter à la variable lettre la lettre en majuscule
                                                   # ou en minuscule qui est pressée et détectée grâce aux listes de pygame
        for n in range(26):
            # une boucle for avec en varable d'iteration un objet range(26) pour toutes les 26 lettres de l'alphabet
            if liste_de_clefs[n]:
                lettre = liste_de_MAJUSCULES[n]


    else:
        for n in range(28):
            # 28 lettres car le à et le é sont pris en compte
            if liste_de_clefs[n]:
                lettre = liste_de_lettres[n]


    if keys[K_SPACE]:   #espace
        lettre = " "

    if keys[K_RETURN]:  # gestion de la touche entré, pour valider la réponse
        main_loop.can_error = True
        main_loop.text = "".join(main_loop.zone)    # on joint toutes les lettres de toutes les zones en une seule chaîne de caractère
        for n in range(18):                         # on vide les zones
            main_loop.zone[n] = ""

        if main_loop.text == "":
            pass
        else:
            main_loop.answer = main_loop.text
        main_loop.has_answer = True

    if keys[K_BACKSPACE]:       # gestion de la touche suprimer
        main_loop.zone[main_loop.cursor-1] = ""
        sleep(0.007)

    if lettre in liste_de_MAJUSCULES:
        sleep(0.007)

    return lettre                              # on revoie la lettre
