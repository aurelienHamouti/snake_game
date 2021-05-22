# -*- coding: utf-8 -*-
from os import times
from tkinter import *
from random import randrange
import pygame
import time
from datetime import datetime
import os

class Snake(Frame):

    def __init__(self, snakeWindow=None, myTitle=None, myGeometry=None, backgroundColor=None, level="slug", canvasColor="black"):

        #model
        Frame.__init__(self, snakeWindow)
        self._level = level
        self._me = snakeWindow
        self._me.title(myTitle)
        self._me.geometry(myGeometry)
        self._me.config(background=backgroundColor)
        self._x = 250
        self._y = 300       
        self._dx = 10
        self._dy = 10
        self._pX = randrange(5, 595)#random start x position
        self._pY = randrange(5, 495)#random start y position
        self._flag = 0
        self._cible = 0
        self._direction = 'top'
        self._move = False
        self._snake = 0
        self._widthCanvas = 600
        self._heightCanvas = 500
        self._canvas = Canvas(self._me , width= self._widthCanvas, height=self._heightCanvas, bg=canvasColor)
        self._exitButton = Button(self._me, text='Exit', command=self.exit, bg='black' , fg='green')
        self._scoreFilePath = os.path.join('data', 'scores.txt')
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.mixer.init()

        if(level=="slug"):
            self._speed = 200
        elif(level=="coral"):
            self._speed = 90
        elif(level=="python"):
            self._speed = 30
        else:
            self._speed = 60
        
        #view
        self.view_interface()

        #Controler
        self.newGame()

    def view_interface(self):
        
        self._snake = [[self._x,self._y],[self._x+2.5,self._y+2.5],[self._x+5,self._y+5],[0,0]]
        self._cible = self._canvas.create_rectangle(self._pX, self._pY, self._pX+5, self._pY+5, outline='green', fill='black')
        self._canvas.pack(side=TOP, padx=5, pady=5)
        self._exitButton['highlightcolor'] = "red"
        self._exitButton['activebackground'] = "#ffff00"
        self._exitButton.pack(side=TOP, padx=5, pady =5)

        #events manage
        self._me.bind('<d>', self.turnRight)
        self._me.bind('<Right>', self.turnRight)
        self._me.bind('<a>', self.turnLeft)
        self._me.bind('<Left>', self.turnLeft)
        self._me.bind('<w>' , self.turnTop)
        self._me.bind('<Up>' , self.turnTop)
        self._me.bind('<s>', self.turnBottom)
        self._me.bind('<Down>', self.turnBottom)

    def move(self):
        self._canvas.delete('all')
        if self._move:
            
            j=0
            i=len(self._snake)-1
            while i > 0:
                self._snake[i][0]=self._snake[i-1][0]
                self._snake[i][1]=self._snake[i-1][1]
                self._canvas.create_oval(self._snake[i][0], self._snake[i][1], self._snake[i][0] +10, self._snake[i][1]+10,outline='green', fill='black')
                i=i-1
            self._canvas.create_rectangle(self._pX, self._pY, self._pX+7, self._pY+7, outline='green', fill='black')

            if self._direction  == 'right':
                self._snake[0][0]  = self._snake[0][0] + self._dx
                if self._snake[0][0] > self._widthCanvas:
                    #self._snake[0][0] = 0
                    self.lose()
                    return 0
            elif self._direction  == 'left':
                self._snake[0][0]  = self._snake[0][0] - self._dx
                if self._snake[0][0] < 0:
                    #self._snake[0][0] = self._widthCanvas
                    self.lose()
                    return 0
            elif self._direction  == 'top':
                self._snake[0][1]  = self._snake[0][1] - self._dy
                if self._snake[0][1] < 0:
                    #self._snake[0][1] = self._heightCanvas
                    self.lose()
                    return 0
            elif self._direction  == 'down':
                self._snake[0][1]  = self._snake[0][1] + self._dy
                if self._snake[0][1] > self._heightCanvas:
                    #self._snake[0][1] = 0
                    self.lose()
                    return 0
            self._canvas.create_oval(self._snake[0][0], self._snake[0][1], self._snake[0][0]+10, self._snake[0][1]+10,outline='green', fill='blue')
            self.test()
        else:
            #Appuyer sur une touche directionelle pour commencer à jouer !
            self._canvas.create_text(300, 200, text='Appuyer sur une touche directionnelle pour commencer à jouer !', fill='white', justify='center', font='Helvetica 12 bold')
        if self._flag != 0:
            self._me.after(self._speed, self.move)

    def turnRight(self, e):
        self._direction = 'right'
        self._move = True

    def turnLeft(self, e):
        self._direction = 'left'
        self._move = True

    def turnTop(self, e):
        self._direction = 'top'
        self._move = True

    def turnBottom(self, e):
        self._direction = 'down'
        self._move = True

    def test(self):
        if self._snake[1][0]>self._pX-7 and  self._snake[1][0]<self._pX+7:        
            if self._snake[1][1]>self._pY-7 and self._snake[1][1]<self._pY+7:
                self.win()#the snake catch the cible !

    def newGame(self):
        self.play_ambiance_music()
        try:
            f = open(self._scoreFilePath, "a")
            f.write(datetime.now().strftime("%d/%m/%Y : %H:%M:%S") + " new game party has begun on level : " + str(self._level) + "\n")
            f.close()
        except:
            print("error when the file scores.txt is write")
        if self._flag == 0:
            self._flag = 1
        self.move()

    def play_win_music(self):
        try:
            winSound = pygame.mixer.music.load(os.path.join('ressources', 'sounds', 'eat.wav'))
            winSound = pygame.mixer.music.play(0)
            pygame.mixer.music.play(0)
        except:
            print("error when pygame mixer music is used")
        time.sleep(0.4)
        self.play_ambiance_music()

    def play_ambiance_music(self):
        try:
            ambianceSound = pygame.mixer.music.load(os.path.join('ressources', 'sounds', 'ambiance.wav'))
            ambianceSound = pygame.mixer.music.play(-1)
        except:
            print("error when pygame mixer music is used")

    def win(self):
        self._pX = randrange(20, self._widthCanvas-20)#new random cible
        self._pY = randrange(20, self._heightCanvas-20)
        self._canvas.coords(self._cible,self._pX, self._pY, self._pX+5, self._pY+5)
        self._snake.append([0,0])#lengthen the snake
        self.play_win_music()#noise catch
        #write score
        try:
            f = open(self._scoreFilePath, "a")
            f.write(datetime.now().strftime("%d/%m/%Y : %H:%M:%S") + " snake eat an apple ! -> new snake lenght is " + str(len(self._snake)) + "\n")
            f.close()
        except:
            print("error when the file scores.txt is write")

    def lose(self):
        try:
            loseSound = pygame.mixer.music.load(os.path.join('ressources', 'sounds', 'lose.wav'))
            loseSound = pygame.mixer.music.play(0)
        except:
            print("error when pygame mixer music is used")
        time.sleep(0.8)
        self._snake = [[self._x,self._y],[self._x+2.5,self._y+2.5],[self._x+5,self._y+5],[0,0]]
        self._snake[0][0] = self._x
        self._snake[0][1] = self._y
        self._pX = randrange(20, self._widthCanvas-20)#new random cible
        self._pY = randrange(20, self._heightCanvas-20)
        self._canvas.coords(self._cible,self._pX, self._pY, self._pX+5, self._pY+5)
        self._move = False
        self.move()
        self.play_ambiance_music()
        try:
            f = open(self._scoreFilePath, "a")
            f.write(datetime.now().strftime("%d/%m/%Y : %H:%M:%S") + " snake is died, game over \n")
            f.close()
        except:
            print("error when the file scores.txt is write")

    def exit(self):
        pygame.mixer.music.stop()
        self._me.destroy()

def startGame(level):
    root = Tk()
    root.iconbitmap(os.path.join('ressources', 'images', 'blackSnakeIcon.ico'))
    root.resizable(width=False, height=False)
    root.attributes('-topmost',True)
    program = Snake(root, "Snake DCS", "700x550+300+20", "#00cc00", level, "#00001a")
    program.mainloop()