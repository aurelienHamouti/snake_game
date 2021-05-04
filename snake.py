# -*- coding: utf-8 -*-

from Tkinter import *
import tkFont
from random import randrange

class Snake(Frame):

    def __init__(self, snakeWindow=None, myTitle=None, myGeometry=None, backgroundColor=None, level="slug"):

        #model
        Frame.__init__(self, snakeWindow)
        self._me = snakeWindow
        self._me.title(myTitle)
        self._me.geometry(myGeometry)
        self._me.config(background=backgroundColor)

        x = 245
        y = 24        
        dx, dy = 10, 10
        flag = 0
        direction = 'haut'
        Serpent=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]

        pX = randrange(5, 495)
        pY = randrange(5, 495)

        can = Canvas(self._me , width=500, height=500, bg='black')
        can.pack(side=TOP, padx=5, pady=5)

        #view
        self.view_interface()

    def view_interface(self):

        oval1=can.create_oval(Serpent[1][0], Serpent[1][1], Serpent[1][0] +10, Serpent[1][1]+10, outline='green', fill='red')
        oval = can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10, outline='green', fill='green')
        pomme = can.create_rectangle(pX, pY, pX+5, pY+5, outline='green', fill='black')

        #events manage
        fen.bind('<d>', turnRight)
        fen.bind('<q>', turnLeft)
        fen.bind('<z>' , turnTop)
        fen.bind('<s>', turnBottom)

    def move():
        global x
        global y,pX,pY
        global Serpent
        can.delete('all')
        i=len(Serpent)-1
        j=0
        while i > 0:
            Serpent[i][0]=Serpent[i-1][0]
            Serpent[i][1]=Serpent[i-1][1]
            can.create_oval(Serpent[i][0], Serpent[i][1], Serpent[i][0] +10, Serpent[i][1]+10,outline='green', fill='black')
            i=i-1
        can.create_rectangle(pX, pY, pX+5, pY+5, outline='green', fill='black')

        if direction  == 'gauche':
            Serpent[0][0]  = Serpent[0][0] - dx
        if Serpent[0][0] < 0:
            Serpent[0][0] = 493
        elif direction  == 'droite':
            Serpent[0][0]  = Serpent[0][0] + dx
            if Serpent[0][0] > 493:
                Serpent[0][0] = 0
        elif direction  == 'haut':
            Serpent[0][1]  = Serpent[0][1] - dy
            if Serpent[0][1] < 0:
                Serpent[0][1] = 493
        elif direction  == 'bas':
            Serpent[0][1]  = Serpent[0][1] + dy
            if Serpent[0][1] > 493:
                Serpent[0][1] = 0
        can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10,outline='green', fill='blue')
        test()
        test()
    
        if flag != 0:
            fen.after(60, move)

    def turnRight():
        global direction
        direction = 'droite'

    def turnLeft():
        global direction
        direction = 'gauche'

    def turnTop():
        global direction
        direction = 'haut'

    def turnBottom():
        global direction
        direction = 'bas'

    def test():
        global pomme
        global x,y,pX,pY
        global Serpent
        if Serpent[1][0]>pX-7 and  Serpent[1][0]<pX+7:        
            if Serpent[1][1]>pY-7 and Serpent[1][1]<pY+7:
                #On remet une pomme au hasard
                pX = randrange(5, 495)
                pY = randrange(5, 495)
                can.coords(pomme,pX, pY, pX+5, pY+5)
                #On joute un nouveau point au serpent
                Serpent.append([0,0])
                #print(Serpent)

    def win():
        pass

    def lose():
        pass

    def exit():
        pass

def start(level):
    root = Tk()
    program = Snake(root, "Snake DCS", "800x500+100+100", "#00cc00", level)
    program.mainloop()