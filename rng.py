# POKER RANDOM NUMBER GENERATOR

import tkinter as tk 
import random

langas = tk.Tk()
langas.geometry("100x150")
langas.title("Random Number Generator")
langas.resizable(width=False,height=False)
langas.iconbitmap('C:\\Users\\jack-\\Desktop\\Paskaitu medziaga\\ikona2.ico')

def gen_nr():
    sarasas = range(0,100)
    skaicius = ""
    for skaicius in range(2):
        skaicius = skaicius + random.choice(sarasas)
    linija2.config(text = skaicius)

#linija1 = tk.Label(text="RNG",font=("broadway",67),bg="Black",fg="White")
mygtukas = tk.Button(text="<X>",font=("broadway",25),bg="black",fg="white",command=gen_nr)
linija2 = tk.Label (font=("broadway",50),bg="white", fg="black",text="")

#linija1.grid(row=0, column=0)
mygtukas.grid(row=10, column=0)
linija2.grid(row=20, column=0)

langas.mainloop()
