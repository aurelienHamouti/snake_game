# -*- coding: utf-8 -*-
from Tkinter import *
import tkFont
from random import randrange
from winsound import *
import time

class Snake(Frame):

    def __init__(self, snakeWindow=None, myTitle=None, myGeometry=None, backgroundColor=None, level="slug", canvasColor="black"):

        #model
        Frame.__init__(self, snakeWindow)
        self._me = snakeWindow
        self._me.title(myTitle)
        self._me.geometry(myGeometry)
        self._me.config(background=backgroundColor)
        self._x = 245
        self._y = 24       
        self._dx = 10
        self._dy = 10
        self._pX = randrange(5, 595)#random start x position
        self._pY = randrange(5, 495)#random start y position
        self._flag = 0
        self._cible = 0
        self._direction = 'top'
        self._serpent = [[self._x,self._y],[self._x+2.5,self._y+2.5],[self._x+5,self._y+5],[0,0]]
        self._canvas = Canvas(self._me , width=600, height=500, bg=canvasColor)
        self._canvas.pack(side=TOP, padx=5, pady=5)
        self._exitButton = Button(self._me, text='Exit', command=self._me.destroy, bg='black' , fg='green')

        if(level=="slug"):
            self._speed = 200
        elif(level=="coral"):
            self._speed = 60
        elif(level=="python"):
            self._speed = 10
        else:
            self._speed = 60
        
        #view
        self.view_interface()

        #Controler
        self.newGame()
        self.play_ambiance_music()

    def view_interface(self):

        oval1 = self._canvas.create_oval(self._serpent[1][0], self._serpent[1][1], self._serpent[1][0] +10, self._serpent[1][1]+10, outline='green', fill='red')
        oval = self._canvas.create_oval(self._serpent[0][0], self._serpent[0][1], self._serpent[0][0]+10, self._serpent[0][1]+10, outline='green', fill='green')
        self._cible = self._canvas.create_rectangle(self._pX, self._pY, self._pX+5, self._pY+5, outline='green', fill='black')
        self._exitButton['highlightcolor'] = "red"
        self._exitButton['activebackground'] = "#ffff00"
        self._exitButton.pack(side=TOP, padx=5, pady =5)

        #events manage
        self._me.bind('<d>', self.turnRight)
        self._me.bind('<a>', self.turnLeft)
        self._me.bind('<w>' , self.turnTop)
        self._me.bind('<s>', self.turnBottom)

    def move(self):
        self._canvas.delete('all')
        i=len(self._serpent)-1
        j=0
        while i > 0:
            self._serpent[i][0]=self._serpent[i-1][0]
            self._serpent[i][1]=self._serpent[i-1][1]
            self._canvas.create_oval(self._serpent[i][0], self._serpent[i][1], self._serpent[i][0] +10, self._serpent[i][1]+10,outline='green', fill='black')
            i=i-1
        self._canvas.create_rectangle(self._pX, self._pY, self._pX+5, self._pY+5, outline='green', fill='black')

        if self._direction  == 'left':
            self._serpent[0][0]  = self._serpent[0][0] - self._dx
        if self._serpent[0][0] < 0:
            self._serpent[0][0] = 593
        elif self._direction  == 'right':
            self._serpent[0][0]  = self._serpent[0][0] + self._dx
            if self._serpent[0][0] > 593:
                self._serpent[0][0] = 0
        elif self._direction  == 'top':
            self._serpent[0][1]  = self._serpent[0][1] - self._dy
            if self._serpent[0][1] < 0:
                self._serpent[0][1] = 493
        elif self._direction  == 'down':
            self._serpent[0][1]  = self._serpent[0][1] + self._dy
            if self._serpent[0][1] > 493:
                self._serpent[0][1] = 0
        self._canvas.create_oval(self._serpent[0][0], self._serpent[0][1], self._serpent[0][0]+10, self._serpent[0][1]+10,outline='green', fill='blue')
        self.test()
        self.test()
        if self._flag != 0:
            self._me.after(self._speed, self.move)

    def turnRight(self, e):
        self._direction = 'right'

    def turnLeft(self, e):
        self._direction = 'left'

    def turnTop(self, e):
        self._direction = 'top'

    def turnBottom(self, e):
        self._direction = 'down'

    def test(self):
        if self._serpent[1][0]>self._pX-7 and  self._serpent[1][0]<self._pX+7:        
            if self._serpent[1][1]>self._pY-7 and self._serpent[1][1]<self._pY+7:
                self.win()#the snake catch the cible !
    def newGame(self):
        if self._flag == 0:
            self._flag = 1
        self.move()

    def play_win_music(self):
        PlaySound(r"..\ressources\win.wav", SND_ASYNC)
        #winsound.Beep(500, 100)
        time.sleep(1)
        self.play_ambiance_music()

    def play_ambiance_music(self):
        PlaySound(r"..\ressources\ambiance.wav", SND_ASYNC)

    def win(self):
        self._pX = randrange(5, 495)#new random cible
        self._pY = randrange(5, 495)
        self._canvas.coords(self._cible,self._pX, self._pY, self._pX+5, self._pY+5)
        self._serpent.append([0,0])#lengthen the snake
        self.play_win_music()#noise catch

    def lose(self):
        pass

    def exit(self):
        pass

def startGame(level):
    root = Tk()
    root.iconbitmap(r'..\ressources\blackSnakeIcon.ico')
    program = Snake(root, "Snake DCS", "700x550+300+20", "#00cc00", level, "#00001a")
    program.mainloop()