from tkinter import *
from threading import *
import numpy as np
import time
from os import listdir
from os.path import isfile, join


class GameWindow(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Jeu du Sokoban - Félix - Trophées de la NSI")

        self.set_window_dimentions()

        
        self.Interface_canvas = InterfaceCanvas(self, width = self.width, height=self.height, bg="grey")

        self.bind('<Configure>', self.Interface_canvas.update_interface_size)
        self.bind('<Motion>', lambda onlyreload=True:self.Interface_canvas.update_interface_size(onlyreload=onlyreload))

        
    def set_window_dimentions(self):
        self.width = 1200
        self.height = 800

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_width = screen_width/2-self.width/2
        center_height = screen_height/2-self.height/2 - 20

        self.geometry("%dx%d+%d+%d"%(self.width,self.height, center_width, center_height))
        self.minsize(700,600)

        

#######################################################################################################


class InterfaceCanvas(Canvas):
    def __init__(self, Window, width = 600, height=400, bg="grey"):
        Canvas.__init__(self, Window, width=width, height=height, bg=bg)
        
        self.Window = Window
        self.bg = bg
        
        self.Game = SokobanGame(self.Window, Interface=self, width=int(self["width"])*0.6, height=int(self["height"])*0.5, bg="white")

        self.levels_buttons_page_num = 0
        self.last_buttons_config = []

        self.time = 0
        self.time2 = 0
        self.time_before_big_reload = 2000


        self.actual_page = 0
        self.WidgetsList = dict([])
        self.load_page(self.actual_page)


    def update_interface_size(self, event=None, onlyreload=False, now=False):
        # On rafraichit visuellement la page toutes les 0.2s
        if time.time() * 1000 > self.time+200 or now:
            self.load_page(self.actual_page, reload=True, launch_level=self.Game.level_number)
            self.time = time.time() * 1000

        
        # On reload completement la page pour que le design reste responsive toutes les 2s
        if time.time() * 1000 > self.time2+self.time_before_big_reload and not(onlyreload):
            print("big_reload")
            self.time_before_big_reload = 2000
            self.load_page(self.actual_page, launch_level=self.Game.level_number)
            self.time2 = time.time() * 1000


    def reload(self):

        for name,widget in self.WidgetsList.items():
            widget_width = 0
            widget_height = 0
            if type(widget["width"]) == int:
                widget_width = widget["width"]
            else:
                widget_width = eval(widget["width"])

            if type(widget["height"]) == int:
                widget_height = widget["height"]
            else:
                widget_height = eval(widget["height"])

            if widget["page"] == self.actual_page:
                self.create_window(widget_width, widget_height, window=widget["widget"])

        
        self["width"] = self.Window.winfo_width()
        self["height"] = self.Window.winfo_height()
        
        
        self.grid(row=0,column=0)
        

    def load_page(self, page_to, reload=False, launch_level=None, ):

        self["width"] = self.Window.winfo_width()
        self["height"] = self.Window.winfo_height()

        if not(reload):
            self.time_before_big_reload += 5000
        
        self.delete('all')
        

        match page_to:
            case "IndexPage" | 0:
                if not(reload):
                    print("IndexPage")
                self.actual_page = 0

                #Titres
                self.create_text(int(self["width"])/2, 100, fill="darkblue", font="Times 60 italic bold", text="Jeu du SOKOBAN")
                self.create_text(int(self["width"])/2, 250, fill="darkblue", font="Times 20 italic bold", text="Poussez les caisses sur les interrupteurs")
                                    

                if not(reload):
                    # Bouton pour accéder à la page de choix du niveau à jouer
                    PlayButton = Button(self.Window, text="Jouer", command=lambda: self.load_page(2))
                    self.WidgetsList["PlayButton"]={"widget":PlayButton, "page":0, "width":'int(self["width"])/2+50', "height":'int(self["height"])/2'}


                    # Bouton pour accéder à la page de création de niveaux
                    AddLevelButton = Button(self.Window, text="Créer des niveaux", command=lambda: self.load_page(1))
                    self.WidgetsList["AddLevelButton"]={"widget":AddLevelButton, "page":0, "width":'int(self["width"])/2-50', "height":'int(self["height"])/2'}

                    # Bouton pour accéder aux crédits
                    CreditButton = Button(self.Window, text="Consulter les crédits", command=lambda: self.load_page(-1))
                    self.WidgetsList["CreditButton"]={"widget":CreditButton, "page":0, "width":'int(self["width"])-100', "height":50}


            case "ChooseLevelPage" | 2:
                if not(reload):
                    print('ChooseLevelPage')
                self.actual_page = 2
                self.create_text(int(self["width"])/2, 100, fill="darkblue", font="Times 60 italic bold", text="Choissisez le niveau")

                if not(reload):
                    
                    # Les emplacements de boutons possibles pour chaque niveau chaque niveau
                    LevelsButtonsPositionsList = []

                    lign_num = round(int(self["height"])/200)
                    buttons_num = round(int(self["width"])/200)
                    #Pour chaque ligne de boutons
                    for i in range(1,round(int(self["height"])/200)):
                        #Pour chaque bouton dans cette ligne
                        for j in range(1,round(int(self["width"])/200)):
                            LevelsButtonsPositionsList.append( ('round(int(self["width"])/'+str(buttons_num)+')*'+str(j),  'round(int(self["height"])/'+str(lign_num)+')*'+str(i)) )
                    
                    # Bouton retour
                    ReturnButtonImage = assets["ReturnButtonImage"] 
                    ReturnButton= Button(self.Window, bg=self.bg, image=ReturnButtonImage, command=lambda:self.buttons_actions("ReturnButton", args={"PreviousPage":0}))
                    self.WidgetsList["ReturnButton"]={"widget":ReturnButton, "page":2, "width":50, "height":50}



                    # les < et > pour montrer les niveaux suivants/précédents
                    SeePreviousImage = assets["SeePreviousImage"]
                    SeePrevious= Button(self.Window, bg=self.bg ,image=SeePreviousImage, command=lambda:self.buttons_actions("SeePrevious"))
                    self.WidgetsList["SeePreviousButton"]={"widget":SeePrevious, "page":2, "width":100, "height":'round(int(self["height"])/2)'}

                    SeeNextImage = assets["SeeNextImage"] 
                    SeeNext= Button(self.Window, bg=self.bg, image=SeeNextImage, command=lambda:self.buttons_actions("SeeNext"))
                    self.WidgetsList["SeeNextButton"]={"widget":SeeNext, "page":2, "width":'round(int(self["width"])-100)', "height":'round(int(self["height"])/2)'}



                    #On crée un bouton pour chaque niveau
                    Buttons_list = []
                    for k in range(len(self.Game.get_available_levels(mode="base_levels"))):
                        Buttons_list.append(Button(self.Window, width=4, height=4, bg='#BFCEFF', text=str(k+1), command=lambda k=k: self.load_page(3, launch_level=k+1)))
                    
                    # Si tous les boutons tiennent dans une page
                    if len(self.Game.get_available_levels(mode="base_levels")) <= len(LevelsButtonsPositionsList):
                        # On cache les < > devenus inutiles
                        keys_to_delete = []
                        for widget_key in self.WidgetsList:
                            if "See" in widget_key and "Button" in widget_key:
                                keys_to_delete.append(widget_key)
                        for key in keys_to_delete:
                            del self.WidgetsList[key]
                        k=0
                        for button in Buttons_list:
                            self.WidgetsList["LevelButton"+str(k)]={"widget":button, "page":2, "width":LevelsButtonsPositionsList[k][0], "height":LevelsButtonsPositionsList[k][1]}
                            k+=1

                    # Si il faut afficher les boutons sur plusieurs pages
                    else:
                        print("Too many buttons("+str(len(Buttons_list))+") to print them all ("+str(len(LevelsButtonsPositionsList))+" positions)")
                        

                        pages_num = len(self.Game.get_available_levels(mode="base_levels")) // len(LevelsButtonsPositionsList)

                        # On clear les boutons qui vont peut être devoir disparaitre
                        keys_to_delete = []
                        for widget_key in self.WidgetsList:
                            if "LevelButton" in widget_key:
                                keys_to_delete.append(widget_key)

                        if self.levels_buttons_page_num == 0:
                            for widget_key in self.WidgetsList:
                                if "SeePreviousButton" in widget_key:
                                    keys_to_delete.append(widget_key)
                        if self.levels_buttons_page_num == pages_num:
                            for widget_key in self.WidgetsList:
                                if "SeeNextButton" in widget_key:
                                    keys_to_delete.append(widget_key)

                        
                        for key in keys_to_delete:
                            del self.WidgetsList[key]
                        

                        if self.levels_buttons_page_num == None:
                            self.levels_buttons_page_num = 0
                        if self.levels_buttons_page_num <= 0:
                            self.levels_buttons_page_num = 0
                        if self.levels_buttons_page_num > pages_num:
                            self.levels_buttons_page_num = pages_num

                        
                        k=0
                        for button in Buttons_list:
                            if k>=len(LevelsButtonsPositionsList)*self.levels_buttons_page_num and k<len(LevelsButtonsPositionsList)*self.levels_buttons_page_num+len(LevelsButtonsPositionsList):
                                pos_index=k-len(LevelsButtonsPositionsList)*self.levels_buttons_page_num
                                self.WidgetsList["LevelButton"+str(k)]={"widget":button, "page":2, "width":LevelsButtonsPositionsList[pos_index][0], "height":LevelsButtonsPositionsList[pos_index][1]}
                            k+=1

                    

                
                
            case "PlayPage" | 3:
                if not(reload):
                    print("PlayPage")
                self.actual_page = 3

                self.create_text(int(self["width"])/2, 80, fill="darkblue", font="Times 60 italic bold", text="Niveau "+str(self.Game.level_number))
                
                if not(reload):
                    # Bouton retour
                    ReturnButtonImage = assets["ReturnButtonImage"] 
                    ReturnButton= Button(self.Window, bg=self.bg, image=ReturnButtonImage, command=lambda:self.buttons_actions("ReturnButton", args={"PreviousPage":2}))
                    self.WidgetsList["ReturnButton"]={"widget":ReturnButton, "page":3, "width":50, "height":50}

                    self.Game.load_level(launch_level)
                    self.Game.launch()



            case "AddLevelPage" | 1:
                if not(reload):
                    print("AddLevelPage")
                self.actual_page = 1
                self.create_text(int(self["width"])/2, 100, fill="darkblue", font="Times 60 italic bold", text="Ajoutez un niveau")
                pass
        
            case "CreditsPage" | -1:
                if not(reload):
                    print("CreditsPage")
                self.actual_page = -1
                self.create_text(int(self["width"])/2, 100, fill="darkblue", font="Times 60 italic bold", text="Crédits")
                pass

        self.reload()


    def buttons_actions(self, action, args={}):
        """Fonction à passer en paramètre des boutons """
        match action:
            case "ReturnButton":
                print(args["PreviousPage"])
                self.load_page(args["PreviousPage"])
                self.Game.grid_forget()

            case "SeePrevious":
                self.levels_buttons_page_num-=1
                self.load_page(2)
                
            case "SeeNext":
                self.levels_buttons_page_num+=1
                self.load_page(2)

            

        


#######################################################################################################
        


class SokobanGame(Canvas):

    def __init__(self, Window, Interface, width = 600, height=400, bg="grey", ):
        Canvas.__init__(self, Window, width = width, height=height, bg=bg)

        self.Interface = Interface
        self.width = width
        self.height = height
        self.current_level = np.array([[]])
        self.end = False
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
        if self.end == False: #quand le jeu est terminé, on ne peut plus se déplacer
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
            

            #Si le niveau est terminé, on change de niveau 
            if (self.test_victory()):
                self.level_number = self.level_number + 1
                
                

                if self.level_number<=len(self.get_available_levels(mode="base_levels")):
                    self.load_level(self.level_number)
                    self.Interface.load_page(3, self.level_number)
                else:
                    print("Game Finished")
                    self.Interface.load_page(2)
                    self.grid_forget()

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

    
    assets = {
        "SeePreviousImage":PhotoImage(file = r"system/images/show_previous_levels.png"),
        "SeeNextImage":PhotoImage(file = r"system/images/show_next_levels.png"),
        "ReturnButtonImage":PhotoImage(file = r"system/images/return.png"),
    }

    #boucle principale
    Window.mainloop()