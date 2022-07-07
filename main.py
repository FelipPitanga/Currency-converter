from tkinter import _Compound, _Relief, Tk, font, ttk
from tkinter import *
from turtle import width 

#library import 
from PIL import Image, ImageTk, ImageOps, ImageDraw


#window colors
cor0 = "#FFFFFF" #white
cor1 = "#333333" #black 
cor2 = "#1c003b" #dark purple


#window settings
janela = Tk()
janela.geometry("300x320")
janela.title("converter")
janela.configure(bg=cor0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_create("calm")

#split window
frame1 = Frame(janela, width=300, height=60, padx= 0, bg=cor1, relief="flat")
frame1.grid(row=0, column=0, columnspan=2)

frame2 = Frame(janela, width=300, height=260, padx= 0, bg=cor0, relief="flat")
frame2.grid(row=1, column=0, sticky=NSEW)

#settings frame1
ico1 = Image.open('imgs/img1.jgp')
ico1 = ico1.resize((40, 40), Image.ANTIALIAS)
ico1 = ImageTk.PhotoImage(ico1)

nm = Label(frame1, image=ico1, compound=LEFT, text="Currency-converter", height=30, padx=30, pady=13, relief="raised", anchor=CENTER, bg=cor2, fg=cor0)
nm.Place(x=0, y=0)

#settings frame2
nmresult = Label(frame2, compound=LEFT, width=16, height=2, relief="solid", anchor=CENTER, bg=cor0, fg=cor1)
nmresult.Place(x=50, y=10)


janela.mainloop()