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
Play_canvas.create_rectangle(50*j, 50*i, 50*j+50, 50*i+50, fill="blue")

win.mainloop()