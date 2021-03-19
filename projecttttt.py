from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
from PIL import ImageTk,Image


#def addpackage() :
    

window1 = Tk()
window1.title("Application")
#window.minsize(width=200, height=200)
#window.bind('<Return>',set_message)

window1.geometry("800x450") #You want the size of the app to be 500x500
window1.resizable(0, 0)

headtop = Canvas(window1, bg="red", height=200, width=0)
head = PhotoImage(file = "D:\WorkKKU\\1_2\\ED251007\\Project\\Untitled-1.png")
head_label = Label(window1, anchor=N, image=head)
head_label.place(x=0, y=0, relwidth=1, relheight=1)
headtop.pack()

button1 = tk.Button(window1, text="Add pasadu", height = 5, width = 10)
button2 = tk.Button(window1, text="Update pasadu", height = 5, width = 10)
button3 = tk.Button(window1, text="Check pasadu", height = 5, width = 10)
button4 = tk.Button(window1, text="Exit Program", height = 5, width = 10, command=window1.destroy)

button1.pack(padx = 60, side=tk.LEFT)
button2.pack(padx = 60, side=tk.LEFT)
button3.pack(padx = 60, side=tk.LEFT)
button4.pack(padx = 60, side=tk.LEFT)

window1.mainloop()