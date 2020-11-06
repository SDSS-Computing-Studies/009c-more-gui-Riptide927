#! python3

import tkinter as tk
from tkinter import *
import math


def calc():
    labelans["text"]=""
    a = (entryA.get())
    b = (entryB.get())
    c = (entryC.get())
    h = (entryH.get())

    if h == "":
        if b == "" or a =="" or c == "":
            pass
        else:
            x=1
            a=float(a)
            b=float(b)
            c=float(c)
            s = (a+b+c)/2
            labelans["text"] = math.sqrt(s*(s-a)*(s-b)*(s-c))
    if b!="" and h!="":
        b=float(b)
        h=float(h)
        labelans["text"] = (h*b)/2
    else:
        if x==1:
            pass
        else:
            labelans["text"] = "Could not Calculate try again"



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
labelans = Label(master = frame)

label1.pack()
frame.pack()
label2.pack(side = LEFT)
button.pack(side = LEFT)
entryA.place(x= 240, y = 110)
entryC.place(x=470, y= 150)
entryH.place(x= 375, y = 120)
entryB.place(x=340, y= 240)
labelans.pack(side= LEFT)
main.mainloop()