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
choix=["vers de terre", "couleuvre", "python"]
clicked=StringVar()
clicked.set("difficulty")

diffmen=OptionMenu(fenetre, clicked, *choix)
diffmen.place(relx=0.5, rely=0.55, anchor=CENTER)




#paramètres boutton high score
highbut=Button(fenetre, text= "High score", font="Helvetica 20 bold")
highbut.place(relx=0.5, rely=0.65, anchor=CENTER)




#paramètres boutton sound
soundbut=Button(fenetre, text= "sound", font="Helvetica 20 bold")
soundbut.place(relx=0.5, rely=0.75, anchor=CENTER)




#paramètres boutton help
helpbut=Button(fenetre, text= "help!", font="Helvetica 20 bold", command=open)
helpbut.place(relx=0.5, rely=0.85, anchor=CENTER)

#action du bouton help (ouvre fenêtre avec aide)
def open():
	fenetrehelp =Toplevel()
	fenetrehelp.title("I'm here to help you!")
	fenetrehelp.geometry("600x600+1700+150")
	fenetrehelp.config(background="#eff2d9")
	
	
	#bouton pour fermer la fenêtre help
	boutfermhelp=Button(fenetrehelp, text="fermer l'aide", command=fenetrehelp.destroy)
	boutfermhelp.place(relx=0.5, rely=0.95, anchor=CENTER)






#paramètres boutton quitter
quitbut=Button(fenetre, text= "quit the game", font="Helvetica 12 italic", command=fenetre.destroy)
quitbut.place(relx=0.97, rely=0.97, anchor=SE)




#paramètre étiquette titre
titre=Label(fenetre, text="Snake DCS", bg="#cfdb18", font="Helvetica 45 bold")
titre.place(relx=0.5, rely=0.1, anchor=CENTER)





fenetre.mainloop()