from tkinter import * 
import random

#print("POKER RNG!")

langas = Tk()
langas.geometry("300x150")

def paspausti():
    ivesta = generuoti.get()
    rezultatas["text"] = ivesta
    generuoti.delete(0, len(ivesta))


pavadinimas = Label(langas, text="RANDOM NUMBER GENERATOR")
skaicius = Label(langas, text="Skaicius")
generuoti = Entry(langas)
mygtukas = Button(langas, text="Generuoti", command=paspausti)
langas.bind("<Return>", lambda event: paspausti())
rezultatas = Label(langas, text="", bd=1, relief=SUNKEN, anchor=E)


skaicius.grid(row=0, column=0)
generuoti.grid(row=0, column=1)
mygtukas.grid(row=2, column=1)
rezultatas.grid(row=1, columnspan=3, sticky=W+E)


langas.mainloop()
