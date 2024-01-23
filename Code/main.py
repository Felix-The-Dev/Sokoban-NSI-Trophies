from tkinter import *
import numpy as np


class GameWindow(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Jeu du Sokoban - Félix - Trophées de la NSI")


class SokobanGame(Canvas):

    def __init__(self, Window, width = 600, height=400, bg="grey"):
        Canvas.__init__(self,Window, width = width, height=height, bg=bg)

        self.current_level = np.array([[]])

        self.level1 = self.create_level("level2.txt")
        self.load_level(self.level1)

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

    def load_level(self, level:np.array, level_num=None):
        if level_num==None:
            self.current_level = level
            print_on_canvas(level)
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
            level = self.create_level(path+file_name)
            self.current_level = level
            print_on_canvas(level)
        
    def print_on_canvas(self, level):

        # On crée les lignes de chaque ligne et de chaque colonne
        for i in range(level.shape[0]):
            self.create_line(0,50*i, 800, 50*i, width=0.5)

        for j in range(level.shape[1]):
            self.create_line(0, 50*j, 0.5*j, 600, width=0.5)


        for i in range(level.shape[0]):
            for j in range(level.shape[1]):
                if (level[i][j] == "1"):
                    #affichage mur
                    self.create_rectangle(50*j, 50*i, 50*j+50, 50*i+50, fill="blue")

                elif (level[i][j] == "p"):
                    #affichage joueur
                    self.create_oval(50*j, 50*i, 50*j+50, 50*i+50, fill="yellow")

                elif (level[i][j] == "X"):
                    #affichage caisse
                    self.create_rectangle(50*j, 50*i, 50*j+50, 50*i+50, fill="red")

                elif (level[i][j] == "I"):
                    #affichage interrupteur
                    self.create_oval(50*j+10, 50*i+10, 50*j+40, 50*i+40, fill="red")




    # Fonction testant si un niveau est fini
    def test_victory(self):
        for i in range(self.current_level.shape[0]):
            for j in range(self.current_level.shape[1]):
                if self.current_level[i][j][3] == 1 and self.current_level[i][j][2] == 0:
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
    width = 1400
    height = 900
    Interface_canvas = Canvas(Window, width = width, height=height, bg="grey")
    Play_canvas = SokobanGame(Window, width = width*1.5, height=height*1.5, bg="white")

    # Titre
    Interface_canvas.create_text(width/2, 100, fill="darkblue", font="Times 60 italic bold", text="Jeu du SOKOBAN")
    Interface_canvas.create_text(width/2, 250, fill="darkblue", font="Times 20 italic bold", text="Poussez les caisses sur les interrupteurs")
    Interface_canvas.create_text(width/2, 300, fill="darkblue", font="Times 20 italic bold", text="Appuyez sur une touche pour commencer")

   
    def Keyboard(event):
        global level_number
        global end
        """ Gestion de l'évenement : Appui sur une touche du clavier"""
        if end == False: #quand le jeu est terminé, on ne peut plus se déplacer
            #on efface le canevas
            Play_canvas.delete("all")
            mvt_poss = True
            key = event.keysym
            for i in range(12):
                for j in range(16):
                    if Play_canvas.current_level[i][j][1] == 1 and mvt_poss:
                        #déplacement possible si pas de mur dans la case destination ni de caisse suivie d'une caisse ou d'un mur
                        #haut
                        if key == "Up" and Play_canvas.current_level[i-1][j][0] != 1 and not(Play_canvas.current_level[i-1][j][2]==1) and (Play_canvas.current_level[i-2][j][2]==1 or Play_canvas.current_level[i-2][j][0]==1):
                            if Play_canvas.current_level[i-1][j][2] == 1:
                                Play_canvas.current_level[i-2][j][2] = 1
                                Play_canvas.current_level[i-1][j][2] = 0
                            Play_canvas.current_level[i][j][1] = 0
                            Play_canvas.current_level[i-1][j][1] = 1
                
                        elif key == "Left" and Play_canvas.current_level[i][j-1][0] != 1 and not(Play_canvas.current_level[i][j-1][2]==1) and (Play_canvas.current_level[i][j-2][2]==1 or Play_canvas.current_level[i][j-2][0]==1):
                            if Play_canvas.current_level[i][j-1][2]==1:
                                Play_canvas.current_level[i][j-2][2] = 1
                                Play_canvas.current_level[i][j-1][2] = 0
                            Play_canvas.current_level[i][j][1] = 0
                            Play_canvas.current_level[i][j-1][1] = 1

                        elif key == "Right" and Play_canvas.current_level[i][j+1][0] != 1 and not(Play_canvas.current_level[i][j+1][2]==1) and (Play_canvas.current_level[i][j+2][2]==1 or Play_canvas.current_level[i][j+2][0]==1):
                            if Play_canvas.current_level[i][j+1][2]==1:
                                Play_canvas.current_level[i][j+2][2] = 1
                                Play_canvas.current_level[i][j+1][2] = 0
                            Play_canvas.current_level[i][j][1] = 0
                            Play_canvas.current_level[i][j+1][1] = 1

                        if key == "Down" and Play_canvas.current_level[i+1][j][0] != 1 and not(Play_canvas.current_level[i+1][j][2]==1) and (Play_canvas.current_level[i+2][j][2]==1 or Play_canvas.current_level[i+2][j][0]==1):
                            if Play_canvas.current_level[i+1][j][2] == 1:
                                Play_canvas.current_level[i+2][j][2] = 1
                                Play_canvas.current_level[i+1][j][2] = 0
                            Play_canvas.current_level[i][j][1] = 0
                            Play_canvas.current_level[i+1][j][1] = 1
                        mvt_poss = False # pour ne pas se déplacer de plusieurs cases à la fois
            
            #le cas échéant on change de niveau 
            if (Play_canvas.test_victoire()==True):
                level_number = level_number+1

                if level_number==1:
                    Play_canvas.load_level()

                if level_number==2:
                    genere_level3()
                    Canevas.create_text(400,300, fill="darkblue", font="Times 60 italic bold", text="BRAVO !!!")
                    end = True #on bloque les commandes
            #on raffiche le canevas
            print_canvas_Play_canvas.current_level


    Interface_canvas.focus_set()
    Interface_canvas.bind("<Key>", Keyboard)
    Interface_canvas.Play_canvas.current_level(row=0,column=0)

    # Création d'un widget Button (bouton Quitter)
    ExitButton = Button(Window, text="Quitter", command=Window.destroy)
    ExitButton.Play_canvas.current_level(row=1, column=0)

    #boucle principale
    Window.mainloop()
            
                        
