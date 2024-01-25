# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 08:17:47 2023

@author: adurandlag
"""

import tkinter as tk
from Classes import *


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.defwidgets()
        self.change_page((), self.MenuPageWidgets)
        
    
    
    def change_page(self, page_from, page_to, side=None):        
        for widget in page_from:
            widget.pack_forget()
        
        for widget in page_to:
            if side != None:
                widget.pack(side=side)
            else:
                widget.pack()

    def defwidgets(self):
        # définition des pages
        self.MenuPageWidgets = ()
        self.ChooseGMPageWidgets = ()
        
        # Main page
        self.MainTitle = tk.Label(self, 
                             text="Trouble in the meadow", 
                             font=("Arial", 60) 
                             )
        
        self.SubTitle = tk.Label(self, 
                            text="Un jeu random réalisé par Félix en Python",
                            font=("Arial", 40) 
                            )
        
        self.PlayButton = tk.Button(self,
                               text="Jouer",
                               font=("Arial", 40), 
                               bg="Orange",
                               command=lambda: self.change_page(self.MenuPageWidgets, self.ChooseGMPageWidgets, side="left")
                               )
            
        self.MenuPageWidgets = (self.MainTitle, self.SubTitle, self.PlayButton)
        
        
        
        
        #Choose gamemodes
        
        self.PlayNormalModeButton = tk.Button(self,
                               text="Jeu normal",
                               font=("Arial", 40), 
                               bg="Green",
                               width="20",
                               height="5",
                               command=lambda: self.launchGame(mode="normal")
                               )
        
        self.ChooseGMPageWidgets = (self.PlayNormalModeButton, )
        
        
    
    def launchGame(self, mode="normal"):
       if mode == "normal":
           
           
           self.GameCanvas = tk.Canvas(self, 
                               width=1100, 
                               height=700, 
                               bg="ivory"
                               )
           self.GameCanvas.create_rectangle(10,10,10+30,10+40, fill="orange")
           
           self.player = Player(self.GameCanvas, "assets/player.png")
           self.tower1 = Tower(self.GameCanvas, "assets/carotte.png")
           self.tower2 = Tower(self.GameCanvas, "assets/carotte.png")
           self.tower3 = Tower(self.GameCanvas, "assets/carotte.png")
           self.tower4 = Tower(self.GameCanvas, "assets/carotte.png")
           print(self.player, self.tower1, self.tower2, self.tower3, self.tower4)
           
           
           
           
           
           self.GamePageWidgets = (self.GameCanvas, )
           
           
           self.change_page(self.ChooseGMPageWidgets,self.GamePageWidgets)
       
       
       
   
            
            
            


if __name__ == "__main__":
    app = Window()
    app.title("Trouble in the Meadow (simple TkGame)")
    app.iconbitmap("assets/logo.ico")
    
    width_distance_center = str(int(app.winfo_screenwidth()   /2 -700))
    height_distance_center = str(int(app.winfo_screenheight() /2 -400))
                                 
    app.geometry("1400x800+"+width_distance_center+"+"+height_distance_center)
    app.minsize(950, 600)
    app.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    