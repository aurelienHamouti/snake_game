# -*- coding: utf-8 -*-
from Tkinter import *

#paramètres fenêtre
fenetre=Tk()
fenetre.title("Snake DCS")
fenetre.geometry("600x600+2500+150")
fenetre.config(background="#cfdb18")


#paramètres boutton start
startbut=Button(fenetre, text= "Start Game", font="Helvetica 30 bold")
startbut.place(relx=0.5, rely=0.40, anchor=CENTER)


#paramètres optionMenu difficulté
options=["vers de terre", "couleuvre", "python"]
clicked=StringVar()
clicked.set("difficulty")

drop=OptionMenu(fenetre, clicked, *options)
drop.place(relx=0.5, rely=0.55, anchor=CENTER)


#paramètres boutton high score
highbut=Button(fenetre, text= "High score", bg="green", font="Helvetica 20 bold")
highbut.place(relx=0.5, rely=0.65, anchor=CENTER)


#paramètres boutton sound
soundbut=Button(fenetre, text= "sound", bg="green", font="Helvetica 20 bold")
soundbut.place(relx=0.5, rely=0.75, anchor=CENTER)


#paramètres boutton help
helpbut=Button(fenetre, text= "help", bg="green", font="Helvetica 20 bold")
helpbut.place(relx=0.5, rely=0.85, anchor=CENTER)


#paramètres boutton quitter
quitbut=Button(fenetre, text= "quit the game", bg="green", font="Helvetica 12 italic")
quitbut.place(relx=0.97, rely=0.97, anchor=SE)


#paramètre étiquette titre
titre=Label(fenetre, text="Snake DCS", bg="#cfdb18", font="Helvetica 45 bold")
titre.place(relx=0.5, rely=0.1, anchor=CENTER)





fenetre.mainloop()