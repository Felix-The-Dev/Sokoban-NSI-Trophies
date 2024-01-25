from tkinter import *
import numpy as np


class GameWindow(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Jeu du Sokoban - Félix - Trophées de la NSI")

        self.window_dimentions()
        self.load_page(0)
        
    
    def window_dimentions(self):
        self.width = 1200
        self.height = 800

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_width = screen_width/2-self.width/2
        center_height = screen_height/2-self.height/2 - 20

        self.geometry("%dx%d+%d+%d"%(self.width,self.height, center_width, center_height))

    def load_page(self, page):

        pass



class SokobanGame(Canvas):

    def __init__(self, Window, width = 600, height=400, bg="grey"):
        Canvas.__init__(self,Window, width = width, height=height, bg=bg)

        self.Window = Window
        self.width = width
        self.height = height
        self.current_level = np.array([[]])
        self.level_number = 1
        

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
        self.grid(row=0,column=0)

    
    def load_level(self, level_num:int=None, level:np.array=None):
        self.delete("all")
        if level_num==None:
            self.current_level = level
        else:
            path="system/base_levels/"
            match level_num:
                case 1:
                    file_name = 'level1.txt'
                case 2:
                    file_name = 'level2.txt'
                case 3:
                    file_name = 'level3.txt'
                case 4:
                    file_name = 'level4.txt'
                case 5:
                    file_name = 'level5.txt'
                case 6:
                    file_name = 'level6.txt'
                case 7:
                    file_name = 'level7.txt'
                case 8:
                    file_name = 'level8.txt'
                case 9:
                    file_name = 'level9.txt'
                case 10:
                    file_name = 'level10.txt'
            self.current_level = self.create_level(path+file_name)

        self.update()
    

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

                if self.level_number==2:
                    self.load_level(3)

                if self.level_number==3:
                    self.load_level(3)
                    self.create_text(400,300, fill="darkblue", font="Times 60 italic bold", text="BRAVO !!!")
                    self.grid_remove()
    
            #on update le canevas
            self.update()

    def modify_events(self, event):
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

    # Fonction en lançant le jeu
    def launch(self, modify=False):
        # On enlève le bouton jouer
        LaunchButton.grid_remove()
        #on grid le canvas
        self.grid(row=0, column=0)

        if not(modify):
            #On active les commandes
            self.focus_set()
            self.bind("<Key>", self.move)
        else:
            print("IN LAUNCH")
            #On lance le processus de modification
            self.bind("<Button-1>", self.modify_events)
            self.bind("<Button-2>", self.modify_events)
            self.bind("<Motion>", self.modify_events)
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


    

    # Création d'un widget Canvas (zone graphique)
    Interface_canvas = Canvas(Window, width = Window.width, height=Window.height, bg="grey")
    Play_canvas = SokobanGame(Window, width = Window.width*0.5, height=Window.height*0.5, bg="white")

    # Titre
    Interface_canvas.create_text(Window.width/2, 100, fill="darkblue", font="Times 60 italic bold", text="Jeu du SOKOBAN")
    Interface_canvas.create_text(Window.width/2, 250, fill="darkblue", font="Times 20 italic bold", text="Poussez les caisses sur les interrupteurs")
    Interface_canvas.create_text(Window.width/2, 300, fill="darkblue", font="Times 20 italic bold", text="Appuyez sur une touche pour commencer")

    Interface_canvas.grid(row=0,column=0)

    # Création d'un bouton jouer (in levels)
    LaunchButton = Button(Window, text="Lancer le jeu", command=Play_canvas.launch)
    LaunchButton.grid(row=1, column=0)
    

    # Création d'un bouton créer des niveaux
    ModifyButton = Button(Window, text="Créer des niveaux", command=Play_canvas.launch(modify=True))
    ModifyButton.grid(row=0, column=0)

    # Création d'un bouton jouer
    PlayButton = Button(Window, text="Jouer", command=Play_canvas.launch(modify=True))
    PlayButton.grid(row=0, column=0)


    # Création d'un widget Button (bouton Quitter)
    ExitButton = Button(Window, text="Quitter", command=Window.destroy)
    ExitButton.grid(row=1, column=0)

    


    #boucle principale
    Window.mainloop()