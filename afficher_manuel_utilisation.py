from tkinter import *

fenetre=Tk()
fenetre.title("snake")
fenetre.geometry("600x600+2500+150")



def manuelutilisation():
    fenetremanuel=Toplevel()
    fenetremanuel.title("Manuel d'utilisation")
    fenetremanuel.geometry("707x1000+400+200")
    canvas = Canvas(fenetremanuel, width = 707, height = 1000)      
    canvas.pack()      
    img = PhotoImage(file="petit.png")      
    canvas.create_image(0,0, anchor=NW, image=img)      
    fenetremanuel.resizable(width=False, height=False)
    fenetremanuel.mainloop()



helpbut=Button(fenetre, text="Manuel d'utilisation", command=manuelutilisation)
helpbut.place(relx=0.5, rely=0.75, anchor=CENTER)

fenetre.mainloop()
