from tkinter import *

# Création de la fenetre principale
Window = Tk()
Window.title("Sokoban")

#Variables globales
level_number = 0
end = False

# Création du plateau 

# plateau vide au départ
grid=[] 
for i in range(12):
    grid.append([])
    for j in range(16):
        grid[i].append([])

        for k in range(4):
            (grid[i][j].append(0))


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
Canevas.create_text(400, 100, fill="darkblue", font="Times 60 italic bold" text="SOKOBAN")
Canevas.create_text(400, 250, fill="darkblue", font="Times 20 italic bold" text="Poussez les caisses sur les interrupteurs")
Canevas.create_text(400, 300, fill="darkblue", font="Times 20 italic bold" text="Appuyez sur une touche pour commencer")

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
                Canvas.create_oval(50*j, 50*i, 50*j+50, 50*i+50, fill="yellow")