from tkinter import *
import numpy as np
import time
from os import listdir
from os.path import isfile, join


class GameWindow(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Jeu du Sokoban - Félix - Trophées de la NSI")

        self.set_window_dimentions()

        
        self.Interface_canvas = Canvas(self, width = self.width, height=self.height, bg="grey")
        self.bind('<Configure>', self.update_interface_size)
        self.time = 0
        self.Interface_canvas.grid(row=0,column=0)
        
        self.Game = SokobanGame(self, width = self.width*0.6, height=self.height*0.5, bg="white")

        self.actual_page = 0
        
        self.load_page(self.actual_page)
        
    
    def set_window_dimentions(self):
        self.width = 1200
        self.height = 800

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_width = screen_width/2-self.width/2
        center_height = screen_height/2-self.height/2 - 20

        self.geometry("%dx%d+%d+%d"%(self.width,self.height, center_width, center_height))

    def update_interface_size(self, event):
        if time.time() * 1000 > self.time+2000:
            self.load_page(self.actual_page)
            self.time = time.time() * 1000

        

        



    
    def load_page(self, page_to, launch_level=False):
        self.Interface_canvas["width"] = self.winfo_width()
        self.Interface_canvas["height"] = self.winfo_height()
        self.Interface_canvas.delete('all')

        self.Game.grid_forget()


        match page_to:
                case "IndexPage" | 0:
                    print("IndexPage")
                    self.actual_page = 0

                    #Titres
                    self.Interface_canvas.create_text(int(self.Interface_canvas["width"])/2, 100, fill="darkblue", font="Times 60 italic bold", text="Jeu du SOKOBAN")
                    self.Interface_canvas.create_text(int(self.Interface_canvas["width"])/2, 250, fill="darkblue", font="Times 20 italic bold", text="Poussez les caisses sur les interrupteurs")
                                      

                    # Bouton pour accéder à la page de choix du niveau à jouer
                    PlayButton = Button(self, text="Jouer", command=lambda: self.load_page(2))
                    self.Interface_canvas.create_window(int(self.Interface_canvas["width"])/2+50, int(self.Interface_canvas["height"])/2, window=PlayButton)


                    # Bouton pour accéder à la page de création de niveaux
                    AddLevelButton = Button(self, text="Créer des niveaux", command=lambda: self.load_page(1))
                    self.Interface_canvas.create_window(int(self.Interface_canvas["width"])/2-50, int(self.Interface_canvas["height"])/2, window=AddLevelButton)

                    # Bouton pour accéder aux crédits
                    CreditButton = Button(self, text="Consulter les crédits", command=lambda: self.load_page(-1))
                    self.Interface_canvas.create_window(int(self.Interface_canvas["width"])-100, 50, window=CreditButton)


                case "ChooseLevelPage" | 2:
                    self.actual_page = 2
                    self.Interface_canvas.create_text(int(self.Interface_canvas["width"])/2, 100, fill="darkblue", font="Times 60 italic bold", text="Choissisez le niveau")

                    
                    LevelsButtonsPositionsList = []

                    lign_num = round(int(self.Interface_canvas["height"])/200)
                    buttons_num = round(int(self.Interface_canvas["width"])/200)
                    #Pour chaque ligne de boutons
                    for i in range(1,round(int(self.Interface_canvas["height"])/200)):
                        #Pour chaque bouton dans cette ligne
                        for j in range(1,round(int(self.Interface_canvas["width"])/200)):
                            LevelsButtonsPositionsList.append( (round(int(self.Interface_canvas["width"])/buttons_num)*j,  round(int(self.Interface_canvas["height"])/lign_num)*i) )
                    
                    #On crée un bouton pour chaque niveau
                    Buttons_list = []
                    for k in range(len(self.Game.get_available_levels(mode="base_levels"))):
                        Buttons_list.append(Button(self, width=4, height=4, text=str(k+1), command=lambda k=k: self.load_page(3, launch_level=k+1)))
                    
                    if len(self.Game.get_available_levels(mode="base_levels")) <= len(LevelsButtonsPositionsList):
                        k=0
                        for button in Buttons_list:
                            self.Interface_canvas.create_window(LevelsButtonsPositionsList[k][0], LevelsButtonsPositionsList[k][1], window=button)
                            k+=1
                    
                    
                    
                case "PlayPage" | 3:
                    print("PlayPage")
                    self.actual_page = 3

                    #on grid le canvas
                    self.Game.grid(row=0, column=0)

                    if launch_level == False:
                        self.Interface_canvas.create_text(int(self.Interface_canvas["width"])/2, 80, fill="darkblue", font="Times 60 italic bold", text="Niveau "+str(launch_level))
                        self.Game.launch()
                    else:
                        self.Interface_canvas.create_text(int(self.Interface_canvas["width"])/2, 80, fill="darkblue", font="Times 60 italic bold", text="Niveau "+str(launch_level))
                        self.Game.launch()
                        self.Game.load_level(launch_level)

                    pass
                case "AddLevelPage" | 1:
                    print("AddLevelPage")
                    self.actual_page = 1
                    self.Interface_canvas.create_text(self.width/2, 100, fill="darkblue", font="Times 60 italic bold", text="Ajoutez un niveau")
                    pass
            
                case "CreditsPage" | -1:
                    print("CreditsPage")
                    self.actual_page = -1
                    self.Interface_canvas.create_text(self.width/2, 100, fill="darkblue", font="Times 60 italic bold", text="Crédits")
                    pass
        



class SokobanGame(Canvas):

    def __init__(self, Window, width = 600, height=400, bg="grey"):
        Canvas.__init__(self, Window, width = width, height=height, bg=bg)

        self.Window = Window
        self.width = width
        self.height = height
        self.current_level = np.array([[]])
        self.level_number = 1
    

    
    # Fonction en lançant le jeu
    def launch(self, modify=False):
        if not(modify):
            #On active les commandes
            self.focus_set()
            self.bind("<Key>", self.move)

        else:
            #On lance le processus de gestion des évenements
            self.bind("<Button-1>", self.add_level_page_events)
            self.bind("<Button-2>", self.add_level_page_events)
            self.bind("<Motion>", self.add_level_page_events)
            pass


    def get_available_levels(self, mode="all"):
        base_levels = [f for f in listdir("system/base_levels") if isfile(join("system/base_levels/", f))]
        custom_levels = [f for f in listdir("system/custom_levels") if isfile(join("system/custom_levels/", f))]
        custom_levels.sort()
        if mode == "all":
            return base_levels+custom_levels
        elif mode == "base_levels":
            return base_levels
        elif mode == "custom_levels":
            return custom_levels


    def create_level(self, level_path):

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
    

    
    def update(self):
        self.delete("all")
        
        # On calcule la taille de la grille voulue en fonction de la talle du niveau
        grid_size = self.height/self.current_level.shape[0]

        # On on recalcule la largeur du canvas en fonction de la largeur du niveau
        self.config(width=self.current_level.shape[1]*grid_size)

        # On crée les lignes de chaque ligne et de chaque colonne
        # /!\ current_level.shape[0] = num of colums ; current_level.shape[1] = num of ligns
        #ligns
        for i in range(self.current_level.shape[1]):
            self.create_line(grid_size*i, 0, grid_size*i, grid_size*self.current_level.shape[0], width=0.75)

        #columns
        for j in range(self.current_level.shape[0]):
            self.create_line(0, grid_size*j, grid_size*self.current_level.shape[1], grid_size*j, width=0.75)


        for i in range(self.current_level.shape[0]):
            for j in range(self.current_level.shape[1]):
                if (self.current_level[i][j] == "1"):
                    #affichage mur
                    self.create_rectangle(grid_size*j, grid_size*i, grid_size*j+grid_size, grid_size*i+grid_size, fill="blue")

                elif (self.current_level[i][j] == "p"):
                    #affichage joueur
                    self.create_oval(grid_size*j, grid_size*i, grid_size*j+grid_size, grid_size*i+grid_size, fill="yellow")

                elif (self.current_level[i][j] == "X"):
                    #affichage caisse
                    self.create_rectangle(grid_size*j, grid_size*i, grid_size*j+grid_size, grid_size*i+grid_size, fill="red")

                elif (self.current_level[i][j] == "I"):
                    #affichage interrupteur
                    self.create_oval(grid_size*j+10, grid_size*i+grid_size/5, grid_size*j+grid_size*4/5, grid_size*i+grid_size*4/5, fill="red")
        

    
    def load_level(self, level_num:int=None, level:np.array=None):
        if level_num==None:
            print("External level launched")
            self.current_level = level
        else:
            self.level_number = level_num
            self.current_level = self.create_level("system/base_levels/level"+str(level_num)+".txt")
            print("Level "+str(level_num)+" loaded")

        self.update()
        self.grid(row=0,column=0)

    

    def move(self, event):
        self.grid(row=0,column=0)
        """ Gestion de l'évenement : Appui sur une touche du clavier"""
        if end == False: #quand le jeu est terminé, on ne peut plus se déplacer
            #on efface le canevas
            mvt_poss = True
            key = event.keysym
            for i in range(self.current_level.shape[0]):
                for j in range(self.current_level.shape[1]):
                    if self.current_level[i][j] == "p" and mvt_poss:
                        #déplacement possible si pas de mur dans la case destination ni de caisse suivie d'une caisse ou d'un mur
                        #haut
                        if (key == "Up" or key == "z") and (self.current_level[i-1][j] == "0" or (self.current_level[i-1][j] == "X" and (self.current_level[i-2][j] == "0" or self.current_level[i-2][j] == "I"))):
                            if self.current_level[i-1][j] == "X":
                                self.current_level[i-2][j] = "X"
                            self.current_level[i-1][j] = "p"
                            self.current_level[i][j] = "0"
                
                        elif (key == "Left" or key == "q") and (self.current_level[i][j-1] == "0" or (self.current_level[i][j-1] =="X" and (self.current_level[i][j-2] == "0" or self.current_level[i][j-2] == "I"))):
                            if self.current_level[i][j-1] == "X":
                                self.current_level[i][j-2] = "X"
                            self.current_level[i][j-1] = "p"
                            self.current_level[i][j] = "0"

                        elif (key == "Right" or key == "d") and (self.current_level[i][j+1] == "0" or (self.current_level[i][j+1] =="X" and (self.current_level[i][j+2] == "0" or self.current_level[i][j+2] == "I"))):
                            if self.current_level[i][j+1] == "X":
                                self.current_level[i][j+2] = "X"
                            self.current_level[i][j+1] = "p"
                            self.current_level[i][j] = "0"

                        if (key == "Down" or key == "s") and (self.current_level[i+1][j] == "0" or (self.current_level[i+1][j] =="X" and (self.current_level[i+2][j] == "0" or self.current_level[i+2][j] == "I"))):
                            if self.current_level[i+1][j] == "X":
                                self.current_level[i+2][j] = "X"
                            self.current_level[i+1][j] = "p"
                            self.current_level[i][j] = "0"
            
                        mvt_poss = False # pour ne pas se déplacer de plusieurs cases à la fois
            

            #le cas échéant on change de niveau 
            if (self.test_victory()):
                self.level_number = self.level_number + 1

                

                if self.level_number<=len(self.get_available_levels(mode="base_levels")):
                    self.Window.load_page(3, self.level_number)
                else:
                    print("Game Finished")
                    self.Window.load_page(2)

            #on update le canevas
            self.update()

    def add_level_page_events(self, event):
        print("IN MODIFY EVENTS : " + str(event.num))
        match event:
            case "Button-1":
                print("Right click pressed !!")
                pass
            case "Button-2":
                print("Left click pressed !!")
                pass
            case "Motion":
                print("Mouse moved !!")
                pass


        #On charge le premier niveau
        self.load_level(1)


    # Fonction testant si un niveau est fini
    def test_victory(self):
        for i in range(self.current_level.shape[0]):
            for j in range(self.current_level.shape[1]):
                if self.current_level[i][j] == "I":
                    return False
                    #si il y au moins un interrupteur sans caisse, on n'a pas fini
        return True



if __name__ == "__main__":
    
    # Création de la fenetre principale
    Window = GameWindow()

    #Variables globales
    level_number = 0
    end = False


    #boucle principale
    Window.mainloop()