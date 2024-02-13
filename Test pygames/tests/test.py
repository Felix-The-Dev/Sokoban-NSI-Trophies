#Import the tkinter library
from tkinter import *

class GameWindow(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Jeu du Sokoban - Félix - Trophées de la NSI")
        
        self.width = 1200
        self.height = 800

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_width = screen_width/2-self.width/2
        center_height = screen_height/2-self.height/2-40

        self.geometry("%dx%d+%d+%d"%(self.width,self.height, center_width, center_height))

#Create an instance of tkinter frame
win = GameWindow()


Play_canvas = Canvas(win, width = win.width*0.5, height=win.height*0.5, bg="white")
Play_canvas.grid(row=0,column=0)

#Titres
Play_canvas.create_text(300, 100, fill="darkblue", font="Times 60 italic bold", text="Jeu du SOKOBAN")
Play_canvas.create_text(500, 250, fill="darkblue", font="Times 20 italic bold", text="Poussez les caisses sur les interrupteurs")
Play_canvas.delete("all")           

win.mainloop()