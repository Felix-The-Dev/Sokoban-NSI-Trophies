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
            self.surface = pygame.Surface(size)                                # on crée la surface où insérer le texte
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
        
        self.font = pygame.font.SysFont("Arial" ,100)

        self.set_widgets()
        self.actual_page = {}

        self.actual_page_num = 0
        self.load_page(0)
        self.running = True


    def set_widgets(self):
        
        self.background = pygame.image.load('system/assets/fake_background.png')           # on crée l'arrière plan
        self.background_size = ("self.screen.get_width()", "self.screen.get_height()")
        self.background = pygame.transform.scale(self.background, (eval(self.background_size[0]),eval(self.background_size[1])))


        self.return_button = pygame.image.load('system/assets/return.png')               # on crée le bouton retour
        self.return_button = pygame.transform.scale(self.return_button, (75, 75))
        self.return_button_rect = self.return_button.get_rect()                           # on crée son rect
        self.return_button_rect.x = 10
        self.return_button_rect.y = 10

        # Bouton Jouer
        self.play_buttonText = self.font.render("Jouer", 1 , (0,0,0))

        self.play_button_position = ("math.ceil(self.screen.get_width()/2)-self.play_buttonText.get_rect().width/2","math.ceil(self.screen.get_height()/2)-self.play_buttonText.get_rect().height/2")

        self.play_buttonSurface = pygame.Surface((self.play_buttonText.get_rect().width, self.play_buttonText.get_rect().height))                                # on crée le bouton Jouer
        pygame.draw.rect(self.play_buttonSurface, (0,255,0), ((0,0),(20,40)))
        self.play_buttonSurface.fill((125, 125, 125))                                                
        
        self.play_button_rect = self.play_buttonSurface.get_rect()                               # on crée son rect
        self.play_button_rect.x = eval(self.play_button_position[0])
        self.play_button_rect.y = eval(self.play_button_position[1])

        # Boutons de niveau
        self.LevelsButtonsList = {}
        for level_num in range(1, len(get_available_levels(mode="base_levels"))+1):
            print("Created button : "+str(level_num))
            level_buttonText = self.font.render(str(level_num), 1 , (0,0,0))


            level_buttonSurface = pygame.Surface((125,150))                                # on crée le bouton Jouer
            pygame.draw.rect(level_buttonSurface, (0,255,0), ((0,0),(0,0)))
            level_buttonSurface.fill((125, 125, 255))
            
            level_buttonText_rect = level_buttonText.get_rect()
            level_buttonSurface_rect = level_buttonSurface.get_rect()


            # level_buttonText_rect.center = level_buttonSurface_rect.center


            self.LevelsButtonsList["LevelButton"+str(level_num)] = {
                "ButtonText":level_buttonText,
                "ButtonSurface":level_buttonSurface,
                "ButtonTextRect":level_buttonText_rect,
                "ButtonSurfaceRect":level_buttonSurface_rect,
            }




    def run(self,):
        
        for key,element in self.actual_page.items():
            self.screen.blit(element["widget"], element["position"])   # on affiche tous les boutons de la page actuelle

        self.update_responsive_design()
        pygame.display.flip()

        
        for event in pygame.event.get():

            # Clic gauche
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if self.play_button_rect.collidepoint(event.pos):
                    self.load_page(2)

                if self.return_button_rect.collidepoint(event.pos):
                    match self.actual_page_num:
                        case 1:
                            self.load_page(0)
                        case 2:
                            self.load_page(0)
                        case -1:
                            self.load_page(0)
                        case 3:
                            self.load_page(2)

            # Changement des dimentions de la fenêtre
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size
                if width < 500:
                    width = 500
                if height < 400:
                    height = 400
                self.screen = pygame.display.set_mode((width,height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)

            # Appui du bouton quitter
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()



    def update_responsive_design(self):
        for keys,element in self.actual_page.items():
            if "litteral_pos" in element:
                element["position"][0] = eval(element["litteral_pos"][0])
                element["position"][1] = eval(element["litteral_pos"][1])

            if "litteral_size" in element:
                element["widget"] = pygame.transform.scale(element["widget"], (eval(element["litteral_size"][0]), eval(element["litteral_size"][1])))
        
        
    def load_page(self, page_to=0):
        self.actual_page = {}
        match page_to:
            case "IndexPage" | 0:
                self.actual_page_num = 0
                print("IndexPage")
                self.actual_page = {
                    "Background":{"widget":self.background, "position":(0,0), "litteral_size":self.background_size},
                    "PlayButtonSurface":{"widget":self.play_buttonSurface, "position":self.play_button_rect, "litteral_pos":self.play_button_position},
                    "PlayButtonText":{"widget":self.play_buttonText, "position":self.play_button_rect, "litteral_pos":self.play_button_position},
                }
            case "ChangeLevelPage" | 2:
                print("ChangeLevelPage")
                self.actual_page_num = 2
                self.actual_page = {
                    "Background":{"widget":self.background, "position":(0,0), "litteral_size":self.background_size},
                    "ReturnButton":{"widget":self.return_button, "position":self.return_button_rect},
                }

                # Les emplacements de boutons possibles pour chaque niveau chaque niveau
                LevelsButtonsPositionsList = []

                lign_num = self.screen.get_height()//150
                column_num = self.screen.get_width()//150
                print("Nombre de lignes : "+str(lign_num)+" ("+str(self.screen.get_height())+"//200)")
                print("Nombre de colonnes : "+str(column_num)+" ("+str(self.screen.get_width())+"//200)")
                #Pour chaque ligne de boutons
                for i in range(1,lign_num-1):
                    #Pour chaque bouton dans cette ligne
                    for j in range(1,column_num-1):
                        LevelsButtonsPositionsList.append( ('round(self.screen.get_width()/'+str(column_num)+')*'+str(j),  'round(self.screen.get_height()/'+str(lign_num)+')*'+str(i)) )

                for element in LevelsButtonsPositionsList:
                    print("("+str(eval(element[0]))+", "+str(eval(element[1]))+")")
                # Si tous les boutons tiennent dans une page
                if len(get_available_levels(mode="base_levels")) <= len(LevelsButtonsPositionsList):
                    k = 0
                    for key,level_button in self.LevelsButtonsList.items():
                        self.actual_page[key+"Surface"] = {
                            "widget":level_button["ButtonSurface"], 
                            "position":level_button["ButtonSurfaceRect"],
                            "litteral_pos":(LevelsButtonsPositionsList[k][0],LevelsButtonsPositionsList[k][1])
                        }
                        self.actual_page[key+"Text"] = {
                            "widget":level_button["ButtonText"], 
                            "position":level_button["ButtonTextRect"],
                            "litteral_pos":(LevelsButtonsPositionsList[k][0]+"+25",LevelsButtonsPositionsList[k][1]+"+25",),
                        }
                        k+=1
                else:
                    print("Too many buttons("+str(len(get_available_levels(mode="base_levels")))+") to print them all ("+str(len(LevelsButtonsPositionsList))+" positions)")
                    pass
                

            case "PlayPage" | 3:
                self.actual_page_num = 3
                print("PlayPage")
                pass
            case "CreditPage" | -1:
                self.actual_page_num = -1
                print("CreditPage")
                pass
            case "AddLevelPage" | 1:
                self.actual_page_num = 1
                print("AddLevelPage")
                pass



if __name__ == '__main__':
    app = Window()

    while app.running:
            app.run()
