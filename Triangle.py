#! python3

import tkinter as tk
from tkinter import *
import math


def calc():
    a = float(entryA.get())
    b = float(entryB.get())
    c = float(entryC.get())
    h = float(entryH.get())



main = Tk()
main.geometry("650x400")
main.resizable(0,0)
photo = PhotoImage(file = "triangle.png")
frame = Frame()
label1 = Label(image= photo)
label2 = Label(master = frame, text= "Enter in as much information about in the\n triangle shown and I will calculate the area")
button = Button(master = frame, text = "Calculate", command = calc)
entryA = Entry(width = 5)
entryB = Entry(width = 5)
entryC = Entry(width = 5)
entryH = Entry(width = 5)


label1.pack()
frame.pack()
label2.pack(side = LEFT)
button.pack(side = LEFT)
entryA.place(x= 240, y = 110)
entryB.place(x=470, y= 150)
entryH.place(x= 375, y = 120)
entryC.place(x=340, y= 240)
main.mainloop()