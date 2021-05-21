# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.font as TkFont
from src import snake as snake
import os

class Welcome(Frame):

    def __init__(self, welcomeWindow=None, myTitle=None, myGeometry=None, backgroundColor=None):

        #model
        Frame.__init__(self, welcomeWindow)
        self._me = welcomeWindow
        self._me.title(myTitle)
        self._me.geometry(myGeometry)
        #self._drawing = Canvas(width=800,height=500)
        self._me.config(background=backgroundColor)

        
        self._slugLevel = Button(text = "Slug")
        self._CoralLevel = Button(text = "Coral")
        self._pythonLevel = Button(text = "Python")
        self._exit = Button(text = "Exit")
        self._menubar = Menu(self)
        
        #view
        self.view_interface()
    
    def view_interface(self):

        #widgets
        #------#

        #self.grid(column=0, row=0, sticky=(N, W, E, S)) #appel au gestionnaire de géometrie
        #self._me.grid_rowconfigure(0, weight=1)
        #self._me.grid_columnconfigure(0, weight=1)

        titleFont = TkFont.Font(family="Lucida Calligraphy", size=20, weight="bold")
        levelLabelFont = TkFont.Font(family="Great Vibes", size=15, weight="bold")
        levelFont = TkFont.Font(family="Showcard Gothic", size=20, weight="bold")

        

        #slug level button
        self._slugLevel['font'] = levelFont
        self._slugLevel['activebackground'] = "#ffff00"
        #self._slugLevel.grid(row=2, sticky=N, padx=20, pady=20)
        self._slugLevel.place(relx=0.35, rely=0.52, anchor=CENTER)
        
       
        #coral level button
        self._CoralLevel['font'] = levelFont
        self._CoralLevel['activebackground'] = "#ffff00"
        self._CoralLevel.place(relx=0.5, rely=0.52, anchor=CENTER)

        #python level button
        self._pythonLevel['font'] = levelFont
        self._pythonLevel['activebackground'] = "#ffff00"
        self._pythonLevel.place(relx=0.65, rely=0.52, anchor=CENTER)

        #exit button
        self._exit['font'] = "Helvetica 20 bold"
        self._exit['activebackground'] = "#ff0000"
        self._exit.place(relx=0.95, rely=0.95, anchor=CENTER)

        #menu
        menu = Menu(self._menubar, tearoff=0)
        self._menubar.add_cascade(label="Menu", menu=menu)
        menu.add_command(label="Game history", command=self.showHistory)
        helpmenu=Menu(menu, tearoff=0)
        
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="user manual", command=self.showHelp)
        helpmenu.add_command(label="license", command=self.showLicence)
        menu.add_separator()
        menu.add_command(label="Quitter", command=self.exit)
        

        def mouseOver(e):
            e.widget['background'] = "#80d4ff"

        def mouseLeave(e):
            e.widget['background'] = 'SystemButtonFace'

        #events manage
        self._exit['command'] = self.exit
        self._slugLevel['command'] = self.slug
        self._slugLevel.bind("<Enter>", mouseOver)
        self._slugLevel.bind("<Leave>", mouseLeave)

        self._CoralLevel['command'] = self.coral
        self._CoralLevel.bind("<Enter>", mouseOver)
        self._CoralLevel.bind("<Leave>", mouseLeave)

        self._pythonLevel['command'] = self.python
        self._pythonLevel.bind("<Enter>", mouseOver)
        self._pythonLevel.bind("<Leave>", mouseLeave)

        self._me.config(menu = self._menubar)

    # CONTROLEUR
    def slug(e):
        snake.startGame("slug")

    def coral(e):
        snake.startGame("coral")

    def python(e):
        snake.startGame("python")

    def showHistory(self):
        pass

    def showHelp(self):
        usermanual=Toplevel()
        usermanual.title("User Manual")
        usermanual.geometry("636x900+400+200")
        canvas = Canvas(usermanual, width = 636, height = 900)      
        canvas.pack()      
        mypath=os.path.join("ressources", "images", "manuel.png")
        img=PhotoImage(file=mypath)      
        canvas.create_image(0,0, anchor=NW, image=img)      
        usermanual.resizable(width=False, height=False)
        usermanual.mainloop()

    def showLicence(self):
        license=Tk()
        license.title("License")
        license.geometry("345x400+500+200")
        label1=Label(license, text="Snake DCS", font=("Courier New", 25, "bold", "underline"))
        label1.place(x=100, y=15)
        label2=Label(license, text="Copyright (C) <2021> <Aurélien, Marc, Manuel> \n This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or(at your option) any later version.\n \n This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.\n \n You should have received a copy of the GNU General Public License along with this program.If not, see <http://www.gnu.org/licenses/>.", wraplength=300, justify="left", font=("Courier New", 12))
        label2.place(x=15, y=75)
        license.resizable(width=False, height=False)
        license.mainloop()

    def exit(self):
        self._me.destroy()

def start():
    root = Tk()
    root.iconbitmap(r'ressources\images\blackSnakeIcon.ico')
    #iconphoto(True, PhotoImage(file="./ressources/blackSnakeIcon.ico"))
    bgpath=os.path.join("ressources", "images", "pageA.png")
    bg=PhotoImage(file=bgpath)
    bglabel=Label(root, image=bg)
    bglabel.place(x=0, y=0, relwidth=1, relheight=1)
    program = Welcome(root, "Snake DCS", "900x594+250+50")
    root.resizable(width=False, height=False)
    program.mainloop()