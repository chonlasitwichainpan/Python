'''from tkinter import *
import tkinter
from tkinter import messagebox
def proces():
    number1=Entry.get(E1)
    number2=Entry.get(E2)
    operator=Entry.get(E3)
    number1=int(number1)
    number2=int(number2)
    if operator =="+":
        answer=number1+number2
    if operator =="-":
        answer=number1-number2
    if operator=="*":
        answer=number1*number2
    if operator=="/":
        answer=number1/number2
    Entry.insert(E4,0,answer)
    print(answer)

top = tkinter.Tk()
L1 = Label(top, text="My calculator",).grid(row=0,column=1)
L2 = Label(top, text="Number 1",).grid(row=1,column=0)
L3 = Label(top, text="Number 2",).grid(row=2,column=0)
L4 = Label(top, text="Operator",).grid(row=3,column=0)
L4 = Label(top, text="Answer",).grid(row=4,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
B=Button(top, text ="Submit",command = proces).grid(row=5,column=1,)

top.mainloop()'''

# This will import all the widgets 
# and modules which are available in 
# tkinter and ttk module 
'''from tkinter import * #หน้าต่างใหม่
from tkinter.ttk import *
  
# creates a Tk() object 
master = Tk() 
  
# sets the geometry of main  
# root window 
master.geometry("200x200") 
  
  
# function to open a new window  
# on a button click 
def openNewWindow(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(master) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("New Window") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    Label(newWindow,  
          text ="This is a new window").pack() 
  
  
label = Label(master,  
              text ="This is the main window") 
  
label.pack(pady = 10) 
  
# a button widget which will open a  
# new window on button click 
btn = Button(master,  
             text ="Click to open a new window",  
             command = openNewWindow) 
btn.pack(pady = 10) 
  
# mainloop, runs infinitely 
mainloop()'''

'''from tkinter import *

window=Tk()

def power_number():
    answer=float(e1_value.get())**2
    t1.insert(END,float(answer))

l1=Label(window,text="Number:")
l1.grid(row=0, column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text="Calculate",command=power_number)
b1.grid(row=0,column=2)

t1=Text(window,height=1,width=15)
t1.grid(row=0,column=3)'''

'''import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

def func(event):
    print("You hit return.")

def onclick(event=None):
    print("You clicked the button")

root.bind('<Return>', onclick)

button = tk.Button(root, text="click me", command=onclick)
button.pack()

root.mainloop()'''

'''import tkinter as tk

class Application(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")

        tk.Frame.__init__(self, self.root)
        self.create_widgets()

    def create_widgets(self):
        self.root.bind('<Return>', self.parse)
        self.grid()

        self.submit = tk.Button(self, text="Submit")
        self.submit.bind('<Button-1>', self.parse)
        self.submit.grid()

    def parse(self, event):
        print("You clicked?")

    def start(self):
        self.root.mainloop()


Application().start()'''


'''from tkinter import *

root = Tk()

buttonA0 = Button(root, width = 50, text = 'Hi')
buttonB0 = Button(root, text = 'Bye')
buttonC0 = Button(root, text = 'Option 0')
buttonC1 = Button(root, text = 'Option 1')
buttonC2 = Button(root, text = 'Option 2')
buttonC3 = Button(root, text = 'Option 3')
buttonC4 = Button(root, text = 'Option 4')

buttonA0.grid(column = 0, row = 0, rowspan = 5, sticky = NE+SW)
buttonB0.grid(column = 0, row = 5, columnspan = 2, sticky = E+W)
buttonC0.grid(column = 1, row = 0)
buttonC1.grid(column = 1, row = 1)
buttonC2.grid(column = 1, row = 2)
buttonC3.grid(column = 1, row = 3)
buttonC4.grid(column = 1, row = 4)

root.mainloop()'''

'''from tkinter import *

window = Tk()

button1 = Button(window, text = 'button1')
button2 = Button(window, text = 'button2')

button1.grid(column = 0, row = 0)
button2.grid(column = 0, row = 1)

window.mainloop()'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import os
from PIL import ImageTk,Image
import sqlite3 as db
import sqlite3
conn = sqlite3.connect(r"D:\WorkKKU\1_2\ED251007\Chonlasit_Python\shipping.db")
c = conn.cursor()
global shipto
ntrack = []
global send,recip,address,sendto,typ,weight

def change_label(*args):
    label.config(text='') # clear label
    label.config(text='T' + var.get()) # set new label text

root = Tk()

var = StringVar() # make the StringVar()

label = Label(root)
entry = Entry(root, textvariable=var) # set the textvariable to var

var.trace('w', change_label) # trace var to monitor for changes, calling function on change

label.pack()
entry.pack()

root.mainloop()