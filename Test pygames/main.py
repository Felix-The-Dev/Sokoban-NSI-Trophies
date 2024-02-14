import pygame
import numpy as np
import time
import math
from os import listdir
from os.path import isfile, join


pygame.init() 

class Button():
    def __init__(self, name:str, position:tuple, size:tuple, text=None, image=None, color=None, backgroundcolor=None):

        self.button_conponents = {}

        if text != None and color != None:
            font = pygame.font.SysFont("monospace" ,15)
            self.text_image = font.render ( text, 1 , color)
            self.button_conponents[name+"Text"] = {
                "widget": self.text_image, 
                "position": (eval(position[0]), eval(position[1])), 
                "litteral_pos": position
            }

        # Si le bouton n'a pas d'image
        if backgroundcolor != None:
            self.surface = pygame.Surface(size)                                # on crée le bouton Jouer
            self.surface.fill(backgroundcolor)                                                
            self.surface = pygame.transform.scale(self.play_button, (100, 100))
            self.surface_position = ("math.ceil(self.screen.get_width()/2)","math.ceil(self.screen.get_height()/2)")
            self.surface_rect = self.play_button.get_rect()                               # on crée son rect
            self.surface_rect.x = eval(self.surface_position[0])
            self.surface_rect.y = eval(self.surface_position[1])

            self.button_conponents[name+"Surface"] = {
                "widget": self.surface, 
                "position": self.surface_rect, 
                "litteral_pos": self.surface_position
            }

        # Si le bouton a une image
        elif image != None:
            
            
            self.image = pygame.image.load(image)          
            self.image_size = size
            self.image = pygame.transform.scale(self.image, (eval(self.image_size[0]),eval(self.image_size[1])))

            self.button_conponents[name+"Image"] = {
                "widget": self.image, 
                "position": (eval(position[0]), eval(position[1])), 
                "litteral_pos": position
            }
            



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


class Window():
    def __init__(self):
        pygame.display.set_caption("Jeu du Sokoban - Félix.dev")
        self.size = (1200,800)
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)

        self.set_widgets()
        self.actual_page = {}

        self.load_page(0)
        self.running = True


    def set_widgets(self):
        
        self.background = pygame.image.load('system/assets/background.jpg')           # on crée l'arrière plan
        self.background_size = ("self.screen.get_width()", "self.screen.get_height()")
        self.background = pygame.transform.scale(self.background, (eval(self.background_size[0]),eval(self.background_size[1])))


        self.return_button = pygame.image.load('system/assets/return.png')           # on crée le bouton retour
        self.return_button = pygame.transform.scale(self.return_button, (75, 75))
        self.return_button_rect = self.return_button.get_rect()                           # on crée son rect
        self.return_button_rect.x = 10
        self.return_button_rect.y = 10

 
        self.play_button = pygame.Surface((10, 10))                                # on crée le bouton Jouer
        pygame.draw.rect(self.play_button, (0,255,0), ((40,10),(50,30)), 3)
        self.play_button.fill((255,0,0))                                                
        self.play_button = pygame.transform.scale(self.play_button, (100, 100))
        self.play_button_position = ("math.ceil(self.screen.get_width()/2)","math.ceil(self.screen.get_height()/2)")
        self.play_button_rect = self.play_button.get_rect()                               # on crée son rect
        self.play_button_rect.x = eval(self.play_button_position[0])
        self.play_button_rect.y = eval(self.play_button_position[1])



    def run(self,):
        
        for keys,element in self.actual_page.items():
            self.screen.blit(element["widget"], element["position"])   # on affiche tous les boutons de la page actuelle

        self.update_responsive_design()
        pygame.display.flip()

        
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                

                if self.play_button_rect.collidepoint(event.pos):
                    self.load_page(2)

            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size
                if width < 500:
                    width = 500
                if height < 400:
                    height = 400
                self.screen = pygame.display.set_mode((width,height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)

            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()



    def update_responsive_design(self):
        for keys,element in self.actual_page.items():
            if "litteral_pos" in element:
                element["position"].x = eval(element["litteral_pos"][0])
                element["position"].y = eval(element["litteral_pos"][1])

            if "litteral_size" in element:
                element["widget"] = pygame.transform.scale(element["widget"], (eval(element["litteral_size"][0]), eval(element["litteral_size"][1])))
        
        
    def load_page(self, page_to=0):
        self.actual_page = {}
        match page_to:
            case "IndexPage" | 0:
                print("IndexPage")
                self.actual_page = {
                    "Background":{"widget":self.background, "position":(0,0), "litteral_size":self.background_size},
                    "ReturnButton":{"widget":self.return_button, "position":self.return_button_rect},
                    "PlayButton":{"widget":self.play_button, "position":self.play_button_rect, "litteral_pos":self.play_button_position},
                }
            case "ChangeLevelPage" | 2:
                print("ChangeLevelPage")
                self.actual_page = {
                    "Background":{"widget":self.background, "position":(0,0), "litteral_size":self.background_size},
                    "ReturnButton":{"widget":self.return_button, "position":self.return_button_rect},
                }
            case "PlayPage" | 3:
                print("PlayPage")
                pass
            case "CreditPage" | -1:
                print("CreditPage")
                pass
            case "AddLevelPage" | 1:
                print("AddLevelPage")
                pass



if __name__ == '__main__':
    app = Window()

    while app.running:
            app.run()
