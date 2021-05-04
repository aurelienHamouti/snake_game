# -*- coding: utf-8 -*-

from Tkinter import *
import tkFont
from random import randrange

class Snake(Frame):

    def __init__(self, snakeWindow=None, myTitle=None, myGeometry=None, backgroundColor=None, level="slug", canvasColor="black"):

        #model
        Frame.__init__(self, snakeWindow)
        self._me = snakeWindow
        self._me.title(myTitle)
        self._me.geometry(myGeometry)
        self._me.config(background=backgroundColor)

        self.x = 245
        self.y = 24       
        self.dx = 10
        self.dy = 10
        self.pX = randrange(5, 495)#random start x position
        self.pY = randrange(5, 495)#random start y position
        self.flag = 0
        self.pomme = 0
        self.direction = 'top'
        self.serpent=[[self.x,self.y],[self.x+2.5,self.y+2.5],[self.x+5,self.y+5],[0,0]]
        self.canvas = Canvas(self._me , width=500, height=500, bg=canvasColor)
        self.canvas.pack(side=TOP, padx=5, pady=5)

        #view
        self.view_interface()

        #Controler
        self.newGame()

    def view_interface(self):

        oval1=self.canvas.create_oval(self.serpent[1][0], self.serpent[1][1], self.serpent[1][0] +10, self.serpent[1][1]+10, outline='green', fill='red')
        oval = self.canvas.create_oval(self.serpent[0][0], self.serpent[0][1], self.serpent[0][0]+10, self.serpent[0][1]+10, outline='green', fill='green')
        self.pomme = self.canvas.create_rectangle(self.pX, self.pY, self.pX+5, self.pY+5, outline='green', fill='black')

        b1 = Button(self._me, text='Lancer', command=self.newGame, bg='black' , fg='green')
        b1.pack(side=LEFT, padx=5, pady=5)

        b2 = Button(self._me, text='Quitter', command=self._me.destroy, bg='black' , fg='green')
        b2.pack(side=RIGHT, padx=5, pady =5)

        tex1 = Label(self._me, text="Cliquez sur 'New Game' pour commencer le jeu.", bg='black' , fg='green')
        tex1.pack(padx=0, pady=11)

        #events manage
        self._me.bind('<d>', self.turnRight)
        self._me.bind('<a>', self.turnLeft)
        self._me.bind('<w>' , self.turnTop)
        self._me.bind('<s>', self.turnBottom)

    def move(self):
        #global x
        #global y,pX,pY
        #global Serpent
        self.canvas.delete('all')
        i=len(self.serpent)-1
        j=0
        while i > 0:
            self.serpent[i][0]=self.serpent[i-1][0]
            self.serpent[i][1]=self.serpent[i-1][1]
            self.canvas.create_oval(self.serpent[i][0], self.serpent[i][1], self.serpent[i][0] +10, self.serpent[i][1]+10,outline='green', fill='black')
            i=i-1
        self.canvas.create_rectangle(self.pX, self.pY, self.pX+5, self.pY+5, outline='green', fill='black')

        if self.direction  == 'left':
            self.serpent[0][0]  = self.serpent[0][0] - self.dx
        if self.serpent[0][0] < 0:
            self.serpent[0][0] = 493
        elif self.direction  == 'right':
            self.serpent[0][0]  = self.serpent[0][0] + self.dx
            if self.serpent[0][0] > 493:
                self.serpent[0][0] = 0
        elif self.direction  == 'top':
            self.serpent[0][1]  = self.serpent[0][1] - self.dy
            if self.serpent[0][1] < 0:
                self.serpent[0][1] = 493
        elif self.direction  == 'down':
            self.serpent[0][1]  = self.serpent[0][1] + self.dy
            if self.serpent[0][1] > 493:
                self.serpent[0][1] = 0
        self.canvas.create_oval(self.serpent[0][0], self.serpent[0][1], self.serpent[0][0]+10, self.serpent[0][1]+10,outline='green', fill='blue')
        self.test()
        self.test()
    
        if self.flag != 0:
            self._me.after(60, self.move)

    def turnRight(self, e):
        #global direction
        self.direction = 'right'

    def turnLeft(self, e):
        #global direction
        self.direction = 'left'

    def turnTop(self, e):
         #global direction
        self.direction = 'top'

    def turnBottom(self, e):
        #global direction
        self.direction = 'down'

    def test(self):

        if self.serpent[1][0]>self.pX-7 and  self.serpent[1][0]<self.pX+7:        
            if self.serpent[1][1]>self.pY-7 and self.serpent[1][1]<self.pY+7:
                #On remet une pomme au hasard
                self.pX = randrange(5, 495)
                self.pY = randrange(5, 495)
                self.canvas.coords(self.pomme,self.pX, self.pY, self.pX+5, self.pY+5)
                #On joute un nouveau point au self.serpent
                self.serpent.append([0,0])
                #print(Serpent)
    def newGame(self):
        #global pX,pY
        #global flag
        if self.flag == 0:
            self.flag = 1
        self.move()


    def win(self):
        pass

    def lose(self):
        pass

    def exit(self):
        pass

def startGame(level):
    root = Tk()
    program = Snake(root, "Snake DCS", "800x500+100+100", "#00cc00", level, "#00001a")
    program.mainloop()