# -*- coding: utf-8 -*-

from Tkinter import *
import tkFont
import snake

class Welcome(Frame):

    def __init__(self, welcomeWindow=None, myTitle=None, myGeometry=None, backgroundColor=None):

        #model
        Frame.__init__(self, welcomeWindow)
        self._me = welcomeWindow
        self._me.title(myTitle)
        self._me.geometry(myGeometry)
        #self._drawing = Canvas(width=800,height=500)
        self._me.config(background=backgroundColor)

        self._welcome = Label(text = "Welcome on the DCS snake game ssssss !")
        self._levelChoice = Label(text = "Choice your level :")
        self._slugLevel = Button(text = "Slug")
        self._MedusaLevel = Button(text = "Medusa")
        self._pythonLevel = Button(text = "Python")
        self._exit = Button(text = "Exit")
        
        #view
        self.view_interface()
    
    def view_interface(self):

        #widgets
        #------#

        #self.grid(column=0, row=0, sticky=(N, W, E, S)) #appel au gestionnaire de géometrie
        #self._me.grid_rowconfigure(0, weight=1)
        #self._me.grid_columnconfigure(0, weight=1)

        titleFont = tkFont.Font(family="Lucida Calligraphy", size=20, weight="bold")
        levelLabelFont = tkFont.Font(family="Great Vibes", size=15, weight="bold")
        levelFont = tkFont.Font(family="Showcard Gothic", size=20, weight="bold")

        #welcome message label
        self._welcome['font'] = titleFont
        self._welcome['bg'] = "#00cc00"
        self._levelChoice['fg'] = "white"
        #self._welcome.grid(row=0, column=0, columnspan=1)
        self._welcome.pack()

        #level message label
        self._levelChoice['font'] = levelLabelFont
        self._levelChoice['bg'] = "#00cc00"
        self._levelChoice['fg'] = "white"
        self._levelChoice.pack()
        self._levelChoice.place(relx=0.5, rely=0.20, anchor=CENTER)

        #slug level button
        self._slugLevel['font'] = levelFont
        self._slugLevel['activebackground'] = "#ffff00"
        #self._slugLevel.grid(row=2, sticky=N, padx=20, pady=20)
        self._slugLevel.pack()
        self._slugLevel.place(relx=0.325, rely=0.40, anchor=CENTER)
       
        #medusa level button
        self._MedusaLevel['font'] = levelFont
        self._MedusaLevel['activebackground'] = "#ffff00"
        self._MedusaLevel.pack()
        self._MedusaLevel.place(relx=0.5, rely=0.40, anchor=CENTER)

        #python level button
        self._pythonLevel['font'] = levelFont
        self._pythonLevel['activebackground'] = "#ffff00"
        self._pythonLevel.pack()
        self._pythonLevel.place(relx=0.7, rely=0.40, anchor=CENTER)

        #exit button
        self._exit['font'] = "Helvetica 20 bold"
        self._exit['activebackground'] = "#ff0000"
        self._exit.pack()
        self._exit.place(relx=0.5, rely=0.90, anchor=CENTER)

        def mouseOver(e):
            e.widget['background'] = "#80d4ff"

        def mouseLeave(e):
            e.widget['background'] = 'SystemButtonFace'

        #events manage
        self._exit['command'] = self.exit
        self._slugLevel['command'] = self.slug
        self._slugLevel.bind("<Enter>", mouseOver)
        self._slugLevel.bind("<Leave>", mouseLeave)

        self._MedusaLevel['command'] = self.medusa
        self._MedusaLevel.bind("<Enter>", mouseOver)
        self._MedusaLevel.bind("<Leave>", mouseLeave)

        self._pythonLevel['command'] = self.python
        self._pythonLevel.bind("<Enter>", mouseOver)
        self._pythonLevel.bind("<Leave>", mouseLeave)

    # CONTROLEUR
    def slug(e):
        snake.start("slug")

    def medusa(e):
        pass

    def python(e):
        pass

    def exit(self):
        self._me.destroy()

def start():
    root = Tk()
    program = Welcome(root, "Snake DCS", "800x500+100+100", "#00cc00")
    program.mainloop()