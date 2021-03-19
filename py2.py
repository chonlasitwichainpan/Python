from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
from PIL import ImageTk,Image

def set_message(event=None):
    text = text_input.get()
    
    if text == 'admin' :
        com1()
    elif text == 'costumer' :
        com2()
    #title_label.configure(text=text)

def com1():
    title_label2.pack_forget()
    title_label3 = tk.Label(master=window, text="com1work")
    title_label3.pack()
    window2()
    

def com2():
    title_label4 = tk.Label(master=window, text="com2work")
    title_label4.pack()

#def screen_clear():
    #clearscreen = os.system('cls')

def window2():
    window2 = tk.Tk()
    window2.title("This is window2")
    window2.minsize(width=500, height=500)



    window2.mainloop()

window = Tk()
window.title("Application")
#window.minsize(width=200, height=200)
window.bind('<Return>',set_message)

window.geometry("800x450") #You want the size of the app to be 500x500
window.resizable(0, 0) #Don't allow resizing in the x or y direction

'''C = Canvas(window, bg="blue", height=250, width=300)
bg = PhotoImage(file = "E:\\streaming\\Webcam Overlay2.png")
background_label = Label(window, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()'''

headtop = Canvas(window, bg="red", height=200, width=0)
head = PhotoImage(file = "D:\WorkKKU\\1_2\\ED251007\\Project\\Untitled-1.png")
head_label = Label(window, anchor=N, image=head)
head_label.place(x=0, y=0, relwidth=1, relheight=1)
headtop.pack()


title_label = tk.Label(master=window, text="Enter Your Situation")
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()


test_button = Button(window, text="Enter", command=set_message)
test_button2 = Button(window, text="Enter", command=set_message)

#test_button.grid(column = 10, row = 0)
#test_button2.grid(column = 1, row = 1)

test_button.pack(pady = 10, padx = 50, anchor = 'w')
test_button2.pack()


title_label2 = tk.Label(master=window, text="1234567890")
title_label2.pack()

window.mainloop()