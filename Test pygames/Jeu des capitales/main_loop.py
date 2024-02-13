# Dans ce fichier, j'ai programmé la boucle principale du jeu et les variables qu'elle utilise ce n'est pas le fichier
# via lequel on lance le jeu (expliqué dans functions)

# Problème: on ne peux pas écrire deux lettres d'affilées



from pygame.locals import *  # on importe pygame, pour l'interface grafique GUI
import random                # on importe un module pour créer des nombres aléatoires
from time import *
from functions import *      # on importe le fichier/module functions, pour les fonctions du jeu
from images import *         # on importe le fichier/module images, pour les images du jeu
from sounds import *         # on importe le fichier/module sounds, pour les sons du jeu


pygame.init()                # on lance pygame



class Game:                     # la classe game qui permet d'agir sur le jeu
    def __init__(self):
        self.statue = 0         # le statut du jeu
        self.sound = Sound()    # gérer les sons




countries_list = ["France", "Espagne", "Allemagne"]
                                                          # on crée deux listes qui stoquent les noms de pays et de capitales
capital_list = ["Paris", "Madrid", "Berlin"]

countries_gender_list = ["f", "n", "n"]                          # on crée une liste qui stoquera le genre des pays (ex : DE LA france = f, DU portugal )

can_question = [True, True, False]      # question de double lettres

# Ces listes sont reliées entres elles, ex:La france a pour capitale paris, genre féminin et on peux poser des questions dessus



##############################
add("Portugal", "Lisbonne", "m", False)
add("Angleterre", "Londres", "n", False)                         # ajouter des pays et des capitales via la fonction add (voir fichier functions)
add("Italie", "Rome", "n")
add("Russie", "Moscou", "f", False)
add("Autriche", "Vienne", "n", False)
add("Belgique", "Bruxelles", "f", False)
add("Biélorussie", "Minsk", "f", False)
add("Birmanie", "Naypyidaw", "f")
add("Bolivie", "Sucre", "f")
add("Brésil", "Brasilia", "m")
add("Bulgarie", "Sofia", "f")
add("Canada", "Ottawa", "m", False)
add("Chili", "Santiago", "m")
add("Chine", "Pékin", "f")
add("Colombie", "Bogota", "f")
add("Coree du Nord", "Pyongyang", "f")
add("Coree du Sud", "Seoul", "f")
add("Costa Rica", "San Jose", "m")
add("Croatie", "Zagreb", "f")
add("Danemark", "Copenhague", "m")
add("Egypte", "Le Caire", "n")
add("Estonie", "Tallinn", "n", False)
add("Etats Unis", "Washington", "n")
add("Ethiopie", "Addis Abeba", "n", False)
add("Finlande", "Helsinki", "f")
add("Grece", "Athènes", "f")
add("Guatemala", "Guatemala", "n")
add("Hongrie", "Budapest", "f")
add("Inde", "New Delhi", "n")
add("Indonésie", "Jakarta", "n")
add("Irak", "Bagdad", "n")
add("Iran", "Téhéran", "n")
add("Irlande", "Dublin", "n")
add("Islande", "Reykjavik", "n")
add("Japon", "Tokyo", "m")
add("Jordanie", "Amman", "f", False)
add("Kazakhstan", "Noursoultan", "m")
add("Lettonie", "Riga", "f", False)
add("Lituanie", "Vilnius", "f")
add("Maroc", "Rabat", "m")
add("Mexique", "Mexico", "m")
add("Moldavie", "Chișinau", "f")
add("Mongolie", "Oulan-Bator", "f")
add("Népal", "Katmandou", "m")
add("Norvège", "Oslo", "f")
add("Pérou", "Lima", "m")
add("Pologne", "Varsovie", "f")
add("Roumanie", "Bucarest", "f")
add("Slovaquie", "Bratislava", "f")
add("Slovenie", "Ljubljana", "f")
add("Suède", "Stockholm", "f")
add("Suisse", "Berne", "f")
##############################

print(countries_list)


# variables pour la barre de saisie
text = [""]
cursor = 0
answer = ""
zone = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
can_error = False
click = ctrl = False
color_bar = color_bar2 = 0



pygame.display.set_caption("Capital mania")         # on crée la fenêtre avec son titre : "Capital mania "
screen = pygame.display.set_mode((1080, 720))       # on la redimensionne



# autres variables
question = 0                                        # on crée une variable qui stoque le type de question à poser
country_number_to_generate = 0                        # on crée une variable qui stoque le numéro pour les questions
determinant = ""                                    # on crée une variable qui stoque le déterminant à appliquer pour les pays
has_answer = False
music = 0
choosed_music = 1


running = True                                      # on crée une variable booléene qui indiquera si le jeu est en cour

game = Game()                                       # on crée une variable qui représentera la classe Game et qui sera utilisé pour les actions du jeu

print("Ouverture du jeu")
while running:

    # on met à jour l'écran
    pygame.display.flip()

    # on affiche l'arrière plan du jeu
    screen.blit(background, (0, 0))

    if music == 0:                                  # gestion des musiques
        screen.blit(stop_music, stop_music_rect)
        game.sound.stop("music1")
        game.sound.stop("music2")
        game.sound.stop("music3")


    else:
        screen.blit(active_music, active_music_rect)
        music = choosed_music

    if music == 1:
        game.sound.stop("music2")
        game.sound.stop("music3")
        game.sound.play("music1")

    elif music == 2:
        game.sound.stop("music1")
        game.sound.stop("music3")
        game.sound.play("music2")

    elif music == 3:
        game.sound.stop("music1")
        game.sound.stop("music2")
        game.sound.play("music3")

    screen.blit(settings_button, (990, 10))     # on affiche le boutton des paramètres


    if game.statue == 0:        # si le jeu affiche l'écran d'accueil

        # on affiche le bouton du jeu, la bannière, le crédit, la date et le msg pour Mme Musch
        screen.blit(play_button, (350, 400))
        screen.blit(game_banner, (200, 50))
        screen.blit(credit, (12, 635))
        screen.blit(date, (12, 10))
        screen.blit(Munsch, (875, 630))


    elif game.statue == -1:     # si le jeu affiche l'écran des paramètres
        print_text("Musiques :", (145, 190), size=75) #on affiche le texte musique  grâce à notre variable print_text

        if music == 0:  # affichage des boutons musique
            screen.blit(Music_1_button, Music_1_button_rect)
            screen.blit(Music_2_button, Music_2_button_rect)
            screen.blit(Music_3_button, Music_3_button_rect)

        if music == 1:
            screen.blit(Music_1_button_red, Music_1_button_red_rect)
            screen.blit(Music_2_button, Music_2_button_rect)
            screen.blit(Music_3_button, Music_3_button_rect)

        elif music == 2:
            screen.blit(Music_1_button, Music_1_button_rect)
            screen.blit(Music_2_button_red, Music_2_button_red_rect)
            screen.blit(Music_3_button, Music_3_button_rect)

        elif music == 3:
            screen.blit(Music_1_button, Music_1_button_rect)
            screen.blit(Music_2_button, Music_2_button_rect)
            screen.blit(Music_3_button_red, Music_3_button_red_rect)

        screen.blit(smiley, (955, 355))
        screen.blit(return_button, return_button_rect)


    elif game.statue == 1:      # si le jeu affiche l'écran de changements des modes de jeu
        # on affiche le bouton exercice, le bouton recherche, la bannière et le bouton retour
        screen.blit(exercices_button, exercices_button_rect)
        screen.blit(research_button, research_button_rect)
        screen.blit(gamemode_choice, (300, -80))
        screen.blit(return_button1, return_button1_rect)


    elif game.statue == 2:   # si le jeu affiche l'écran du mode recherche
        # on affiche la bannière de recherche, le bouton retour et la règle
        screen.blit(research_banner, (350, 50))
        screen.blit(return_button2, return_button2_rect)
        screen.blit(rule, (-30, -30))

        if color_bar == 0:
            screen.blit(research_bar, (350, 370))

        elif color_bar == 1:
            screen.blit(research_bar_blue, (350, 370))          # changement de couleur de la barre de saisie

        elif color_bar == 2:
            screen.blit(research_bar_purple, (350, 370))




        if zone[0] == "":
            zone[0] = detect_text()
            cursor = 0

        for i in range(1, 18):                  # on détecte quelle zone à atribuer pour la lettre
            if zone[i] == "":
                zone[i] = detect_text()
                cursor = i
                if zone[i] == zone[i-1] or zone[i-1] == "":
                    zone[i] = ""



        for a in range(0, 18):                      # on affiche chaque zones
            print_text(zone[a], (370+a*20, 375))




        if answer in capital_list:              # on détecte si la réponse est dans la liste des capitales ou des pays et on affiche la réponse
            a = capital_list.index(answer)

            if countries_gender_list[a] == "m":
                determinant = "du "

            elif countries_gender_list[a] == "n":
                determinant = "de l'"

            elif countries_gender_list[a] == "f":
                determinant = "de la "

            print_text(f"{answer} est la capitale {determinant + countries_list[a]}", (350, 420))


        elif answer in countries_list:
            b = countries_list.index(answer)

            if countries_gender_list[b] == "m":
                determinant = "du "

            elif countries_gender_list[b] == "n":
                determinant = "de l'"

            elif countries_gender_list[b] == "f":
                determinant = "de la "

            print_text(f"La capitale {determinant + answer } est {capital_list[b]}", (350, 420))

        else:
            if can_error:
                print_text("Erreur, pays ou capitale absent dans la base de donnée ", (200, 430))


    elif game.statue == 3:
        # on affiche la bannière de recherche, le bouton retour et la règle
        screen.blit(return_button3, return_button3_rect)
        screen.blit(exercices_banner, (350, -150))
        screen.blit(rule, (-30, -30))

        if color_bar2 == 0:
            screen.blit(exercices_bar, (350, 370))

        elif color_bar2 == 1:
            screen.blit(exercices_bar_blue, (350, 370))     # changement de couleur de la barre de saisie

        elif color_bar2 == 2:
            screen.blit(exercices_bar_purple, (350, 370))


        if zone[0] == "":
            zone[0] = detect_text()
            cursor = 0
        # on détecte quelle zone a atribuer pour la lettre
        for i in range(0, 18):
            if zone[i] == "":
                zone[i] = detect_text()
                cursor = i
                if zone[i] == zone[i-1] or zone[i-1] == "":
                    zone[i] = ""



        print_text("".join(zone), (370, 375))


        if question != 1:  # on affiche la question

            print_text(f"Quelle est la capitale {determinant + countries_list[country_number_to_generate]} ?", (280, 280))

        else:
            print_text(f"De quel pays {capital_list[country_number_to_generate]} est-elle la capitale ?", (280, 280))


        if has_answer:
            if question != 1: # on détecte si la réponse est juste et on affiche la réponse

                if answer == capital_list[country_number_to_generate]:
                    print_text("Bonne réponse !", (450, 430), color=(0, 229, 31))
                    screen.blit(new_question, (350, 500))

                else:
                    if can_error:
                        print_text(f"Mauvaise réponse !, la capitale {determinant + countries_list[country_number_to_generate]} est {capital_list[country_number_to_generate]}", (150, 430), color=(255, 4, 4))
                        screen.blit(new_question, (350, 500))
            else:

                if answer == countries_list[country_number_to_generate]:
                    print_text("Bonne réponse !", (450, 430), color=(0, 229, 31))
                    screen.blit(new_question, (350, 500))


                                                                                            # vérification de la véracité de la réponse
                else:
                    if can_error:
                        print_text(f"Mauvaise réponse !, {capital_list[country_number_to_generate]} est la capitale {determinant + countries_list[country_number_to_generate]}", (150, 430), color=(255, 4, 4))
                        screen.blit(new_question, (350, 500))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # on detecte qi l'utilsateur quitte le jeu
            running = False
            pygame.quit()
            print("Fermeture du jeu")


        elif event.type == pygame.MOUSEBUTTONDOWN:  # on détecte un click

            if music != 0:      # pour le bouton stop music
                if active_music_rect.collidepoint(event.pos):
                    music = 0
            else:
                if stop_music_rect.collidepoint(event.pos):
                    music = 1

            if settings_button_rect.collidepoint(event.pos):    # le bouton setting
                game.statue = -1
                game.sound.play("click")



            if game.statue == 0:
                if play_button_rect.collidepoint(event.pos):    # le bouton de jeu
                    game.statue = 1
                    game.sound.play("click")



            elif game.statue == -1:
                if return_button_rect.collidepoint(event.pos):  # bouton retour
                    game.statue = 0
                    game.sound.play("click")

                if Music_1_button_rect.collidepoint(event.pos):  # musique1
                    choosed_music = 1
                    game.sound.play("click")

                if Music_2_button_rect.collidepoint(event.pos): # musique 2
                    choosed_music = 2
                    game.sound.play("click")

                if Music_3_button_rect.collidepoint(event.pos): # musique 3
                    choosed_music = 3
                    game.sound.play("click")



            elif game.statue == 1:
                if research_button_rect.collidepoint(event.pos):  # bouton du mode recherche
                    can_error = False
                    game.statue = 2
                    game.sound.play("click")

                    if countries_gender_list[country_number_to_generate] == "m":
                        determinant = "du "

                    elif countries_gender_list[country_number_to_generate] == "n":      # déterminant du pays
                        determinant = "de l'"

                    elif countries_gender_list[country_number_to_generate] == "f":
                        determinant = "de la "

                    zone[0] = ""
                    zone[1] = ""
                    zone[2] = ""
                    zone[3] = ""
                    zone[4] = ""
                    zone[5] = ""
                    zone[6] = ""
                    zone[7] = ""        # on clear les zones
                    zone[8] = ""
                    zone[9] = ""
                    zone[10] = ""
                    zone[11] = ""
                    zone[12] = ""
                    zone[13] = ""
                    zone[14] = ""
                    zone[15] = ""
                    zone[16] = ""
                    zone[17] = ""

                if exercices_button_rect.collidepoint(event.pos):

                    can_error = False
                    question = random.randint(1, 2)

                    country_number_to_generate = random.randint(0, len(countries_list) - 1)
                    determinant = ""


                    while not can_question[country_number_to_generate]:
                        can_error = False
                        question = random.randint(1, 2)    # on génère le type de question

                        country_number_to_generate = random.randint(0, len(countries_list) - 1)   #on génère le numéro du pays à généré
                        determinant = ""


                    if countries_gender_list[country_number_to_generate] == "m":
                        determinant = "du "

                    elif countries_gender_list[country_number_to_generate] == "n":   # déterminant du pays
                        determinant = "de l'"

                    elif countries_gender_list[country_number_to_generate] == "f":
                        determinant = "de la "

                    zone[0] = ""
                    zone[1] = ""
                    zone[2] = ""
                    zone[3] = ""
                    zone[4] = ""
                    zone[5] = ""
                    zone[6] = ""
                    zone[7] = ""
                    zone[8] = ""
                    zone[9] = ""
                    zone[10] = ""
                    zone[11] = ""   # on clear les zones
                    zone[12] = ""
                    zone[13] = ""
                    zone[14] = ""
                    zone[15] = ""
                    zone[16] = ""
                    zone[17] = ""

                    game.statue = 3
                    game.sound.play("click")

                if return_button1_rect.collidepoint(event.pos):
                    game.statue = 0
                    game.sound.play("click")



            elif game.statue == 2:

                if return_button2_rect.collidepoint(event.pos): # bouton retour
                    game.statue = 1
                    game.sound.play("click")

                if research_bar_rect.collidepoint(event.pos):
                    click = True
                    color_bar = 1       # couleur de la barre de recherche

                elif not ctrl:
                    click = False
                    color_bar = 0

                else:
                    click = False
                    color_bar = 2



            elif game.statue == 3:

                if return_button3_rect.collidepoint(event.pos):     # bouton retour
                    game.statue = 1
                    game.sound.play("click")

                if exercices_bar_rect.collidepoint(event.pos):
                    click = True
                    color_bar2 = 1

                elif not ctrl:
                    click = False
                    color_bar2 = 0      # couleur de la barre de recherche

                else:
                    click = False
                    color_bar2 = 2

                if has_answer:
                    if new_question_rect.collidepoint(event.pos):
                        question = random.randint(1, 2)

                        country_number_to_generate = random.randint(0, len(countries_list) - 1)
                        determinant = ""

                        while not can_question[country_number_to_generate]:
                            can_error = False
                            question = random.randint(1, 2)

                            country_number_to_generate = random.randint(0, len(countries_list) - 1)
                            determinant = ""


                        if countries_gender_list[country_number_to_generate] == "m":
                            determinant = "du "

                        elif countries_gender_list[country_number_to_generate] == "n":
                            determinant = "de l'"

                        elif countries_gender_list[country_number_to_generate] == "f":
                            determinant = "de la "

                        zone[0] = ""
                        zone[1] = ""
                        zone[2] = ""
                        zone[3] = ""
                        zone[4] = ""
                        zone[5] = ""
                        zone[6] = ""
                        zone[7] = ""
                        zone[8] = ""
                        zone[9] = ""        #on clear les zones
                        zone[10] = ""
                        zone[11] = ""
                        zone[12] = ""
                        zone[13] = ""
                        zone[14] = ""
                        zone[15] = ""
                        zone[16] = ""
                        zone[17] = ""
                        has_answer = False