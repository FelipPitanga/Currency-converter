from tkinter import Tk, ttk
from tkinter import *

#library import 
from PIL import Image, ImageTk, ImageOps, ImageDraw


#window colors
cor0 = "#FFFFFF" #white
cor1 = "#333333" #black 
cor2 = "#1c003b" #dark purple


#window settings
window = Tk()
window.geometry("300x320")
window.title("converter")
window.configure(bg=cor0)
window.resizable(width=FALSE, height=FALSE)

style = ttk.Style(window)
style.theme_create("calm")

#split window
frame1 = Frame(window, width=300, height=60, padx= 0, bg=cor1, relief="flat")
frame1.grid(row=0, column=0, columnspan=2)

frame2 = Frame(window, width=300, height=260, padx= 0, bg=cor0, relief="flat")
frame2.grid(row=1, column=0, sticky=NSEW)

#settings frame1
ico1 = Image.open("imgs/dinheiro.png")
ico1 = ico1.resize((45,45), Image.ANTIALIAS)
ico1 = ImageTk.PhotoImage(ico1)

nmpp = Label(frame1, image=ico1, compound=LEFT, text="Currency-converter", height=30, padx=20, pady=13, relief="raised", anchor=CENTER, font='Arial 16 bold', bg=cor1, fg=cor0)
nmpp.place(x=0, y=0)

#settings frame2
nmresult = Label(frame2, width=16, height=2, relief="solid", anchor=CENTER, font='Ivy 15 bold', bg=cor0, fg=cor1)
nmresult.place(x=50, y=10)

#Cois 
coins =["BRL", "EUR", "INR", "USD"]

#box-in (left)
box1in = Label(frame2, text="In:", width=3, height=2, relief="flat", anchor=NW, font='Ivy 10 bold', bg=cor0, fg=cor1)
box1in.place(x=49, y=90)
ComboIn = ttk.Combobox(frame2, width=5, justify=CENTER, font=('Ivy 13 bold'))
ComboIn.place(x=50, y=115)
ComboIn["values"] = (coins)

#box-for (right)
box2for = Label(frame2, text="For:", width=3, height=2, relief="flat", anchor=NW, font='Ivy 10 bold', bg=cor0, fg=cor1)
box2for.place(x=179, y=90)
box2For = ttk.Combobox(frame2, width=5, justify=CENTER, font=('Ivy 13 bold'))
box2For.place(x=180, y=115)
box2For["values"] = (coins)


#input value
value = Entry(frame2, width=18, justify=CENTER, font=('Ivy 13 bold'), relief=SOLID)
value.place(x=65, y=170)

#button for conversion
button = Button(frame2, text="convert", width=18, padx=5, height=1, bg=cor2, fg=cor0, font=('Ivy 10 bold'), relief="raised", overrelief=RIDGE)
button.place(x=65, y=210)




window.mainloop()