# Dans ce fichier python sont stoqués tous les sons necessaires au jeu


import pygame


class Sound:                # on crée un classe son qui gèrera les sons et musiques du son
    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound("assets/click.ogg"),            # le son de click
            "music1": pygame.mixer.Sound("assets/music 1.mp3"),         # le son de la musique 1
            "music2": pygame.mixer.Sound("assets/music 2.mp3"),         # le son de la musique 2
            "music3": pygame.mixer.Sound("assets/music 3.mp3")          # le son de la musique 3
        }

    def play(self, name):       # on crée une méthode play pour jouer le son
        self.sounds[name].play()

    def stop(self, name):       # on crée une méthode stop pour stopper le son
        self.sounds[name].stop()
