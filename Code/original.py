from tkinter import *


class GameWindow(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Jeu du Sokoban - Félix - Trophées de la NSI")
        self.create_grid()

    def create_grid(self):
        # Création du plateau 
        # plateau vide au départ
        for i in range(12):
            grid.append([])
            for j in range(16):
                grid[i].append([])
                for k in range(4):
                    grid[i][j].append(0)


        # niveau 1
        # murs

        for i in range(12):
            grid[i][0][0] = 1
            grid[i][1][0] = 1
            grid[i][14][0] = 1
            grid[i][15][0] = 1

        for j in range(16):
            grid[0][j][0] = 1
            grid[1][j][0] = 1
            grid[10][j][0] = 1
            grid[11][j][0] = 1

        # joueur
        grid[3][3][1] = 1
        #caisses
        grid[5][4][2]=1
        grid[5][6][2]=1
        #interrupteurs
        grid[3][8][3] = 1
        grid[5][5][3] = 1





if __name__ == "__main__":
    
    grid=[] 
    # Création de la fenetre principale
    Window = GameWindow()

    #Variables globales
    level_number = 0
    end = False




    def clear_grid():
        #on efface le plateau
        for i in range(2,10):
            for j in range(2,14):
                grid[i][j][0] = 0
                grid[i][j][1] = 0
                grid[i][j][2] = 0
                grid[i][j][3] = 0

    # Fonctions, appelées au bon moment pour les niveauc suivants
    def genere_level2():
        clear_grid()

        #on crée un nouveau plateau
        #murs
        grid[8][8][0] = 1
        grid[7][3][0] = 1
        #joueur
        grid[9][9][1] = 1
        #caisses
        grid[5][4][2] = 1
        grid[5][6][2] = 1
        #interrupteurs
        grid[3][8][3] = 1
        grid[5][5][3] = 1

    def genere_level3():
        clear_grid()

    # Fonction testant si un niveau est fini
    def test_victoire():
        for i in range(12):
            for j in range(16):
                if grid[i][j][3] == 1 and grid[i][j][2] == 0:
                    return False
                    #si il y au moins un interrupteur sans caisse, on n'a pas fini
        return True

    # Création d'un widget Canvas (zone graphique)
    width = 600
    height = 800
    Canevas = Canvas(Window, width = width, height=height, bg="grey")

    # Titre
    Canevas.create_text(400, 100, fill="darkblue", font="Times 60 italic bold", text="SOKOBAN")
    Canevas.create_text(400, 250, fill="darkblue", font="Times 20 italic bold", text="Poussez les caisses sur les interrupteurs")
    Canevas.create_text(400, 300, fill="darkblue", font="Times 20 italic bold", text="Appuyez sur une touche pour commencer")

    def print_canvas_grid():
        for i in range(12):
            Canevas.create_line(0,50*i,800,50*i,width=0.5)
        for j in range(16):
            Canevas.create_line(50*j, 0.5*j,600,width=0.5)
        for i in range(12):
            print()
            for j in range(16):
                if (grid[i][j][0] == 1):
                    #affichage mur
                    Canevas.create_rectangle(50*j, 50*i, 50*j+50, 50*i+50, fill="blue")

                elif (grid[i][j][1] == 1):
                    #affichage joueur
                    Canevas.create_oval(50*j, 50*i, 50*j+50, 50*i+50, fill="yellow")

                elif (grid[i][j][2] == 1):
                    #affichage caisse
                    Canevas.create_rectangle(50*j, 50*i, 50*j+50, 50*i+50, fill="red")

                elif (grid[i][j][3] == 1):
                    #affichage interrupteur
                    Canevas.create_oval(50*j+10, 50*i+10, 50*j+40, 50*i+40, fill="red")

    def Keyboard(event):
        global level_number
        global end
        """ Gestion de l'évenement : Appui sur une touche du clavier"""
        if end == False: #quand le jeu est terminé, on ne peut plus se déplacer
            #on efface le canevas
            Canevas.delete("all")
            mvt_poss = True
            key = event.keysym
            for i in range(12):
                for j in range(16):
                    if grid[i][j][1] == 1 and mvt_poss:
                        #déplacement possible si pas de mur dans la case destination ni de caisse suivie d'une caisse ou d'un mur
                        #haut
                        if key == "Up" and grid[i-1][j][0] != 1 and not(grid[i-1][j][2]==1) and (grid[i-2][j][2]==1 or grid[i-2][j][0]==1):
                            if grid[i-1][j][2] == 1:
                                grid[i-2][j][2] = 1
                                grid[i-1][j][2] = 0
                            grid[i][j][1] = 0
                            grid[i-1][j][1] = 1
                
                        elif key == "Left" and grid[i][j-1][0] != 1 and not(grid[i][j-1][2]==1) and (grid[i][j-2][2]==1 or grid[i][j-2][0]==1):
                            if grid[i][j-1][2]==1:
                                grid[i][j-2][2] = 1
                                grid[i][j-1][2] = 0
                            grid[i][j][1] = 0
                            grid[i][j-1][1] = 1

                        elif key == "Right" and grid[i][j+1][0] != 1 and not(grid[i][j+1][2]==1) and (grid[i][j+2][2]==1 or grid[i][j+2][0]==1):
                            if grid[i][j+1][2]==1:
                                grid[i][j+2][2] = 1
                                grid[i][j+1][2] = 0
                            grid[i][j][1] = 0
                            grid[i][j+1][1] = 1

                        if key == "Down" and grid[i+1][j][0] != 1 and not(grid[i+1][j][2]==1) and (grid[i+2][j][2]==1 or grid[i+2][j][0]==1):
                            if grid[i+1][j][2] == 1:
                                grid[i+2][j][2] = 1
                                grid[i+1][j][2] = 0
                            grid[i][j][1] = 0
                            grid[i+1][j][1] = 1
                        mvt_poss = False # pour ne pas se déplacer de plusieurs cases à la fois
            
            #le cas échéant on change de niveau 
            if (test_victoire()==True):
                level_number = level_number+1

                if level_number==1:
                    genere_level2()

                if level_number==2:
                    genere_level3()
                    Canevas.create_text(400,300, fill="darkblue", font="Times 60 italic bold", text="BRAVO !!!")
                    end = True #on bloque les commandes
            #on raffiche le canevas
            print_canvas_grid


    Canevas.focus_set()
    Canevas.bind("<Key>", Keyboard)
    Canevas.grid(row=0,column=0)

    #Création d'un widget Button (bouton Quitter)
    ExitButton = Button(Window, text="Quitter", command=Window.destroy)
    ExitButton.grid(row=1, column=0)

    #boucle principale
    Window.mainloop()
            
                        
