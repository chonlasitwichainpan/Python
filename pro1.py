from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import os
from PIL import ImageTk,Image

'''packagewindow = Tk()
packagewindow.title("Add Package")
packagewindow.bind('<return>')

packagewindow.geometry("500x200")
packagewindow.resizable(0, 0)

def getmessage():
    send = sendernameinput.get()
    recip = recipnameinput.get()
    address = addressinput.get()
    typ = typepick.get()
    sendto = sendtopick.get()
    weight = weightinput.get()

    sendernametitle.destroy()
    sendernameinput.destroy()
    recipnametitle.destroy()
    recipnameinput.destroy()
    addresstitle.destroy()
    addressinput.destroy()
    typetitle.destroy()
    typepick.destroy()
    sendtotitle.destroy()
    sendtopick.destroy()
    weighttitle.destroy()
    weightinput.destroy()
    enterbutton.destroy()

    infomationdone = tk.Label(master = packagewindow, text="Information has entered the system")
    infomationdone.config(font=("Courier", 18))
    infomationdone.pack(anchor='center')

    donebutton = Button(packagewindow, text="Done", command = packagewindow.destroy)
    donebutton.pack(anchor='center')

sendernametitle = tk.Label(master = packagewindow, text="Sender name")
sendernametitle.place(x = 10, y = 10)
sendernameinput = tk.Entry(master = packagewindow)
sendernameinput.place(x = 90, y = 10)
recipnametitle = tk.Label(master = packagewindow, text="Recipient name",anchor=E)
recipnametitle.place(x = 250, y = 10)
recipnameinput = tk.Entry(master = packagewindow)
recipnameinput.place(x = 345, y = 10)

addresstitle = tk.Label(master = packagewindow, text="Address")
addresstitle.place(x = 10, y = 45)
addressinput = tk.Entry(master = packagewindow)
addressinput.place(x = 90, y = 45, width = 380)

typetitle = tk.Label(master = packagewindow, text="Type")
typetitle.place(x = 10, y = 80)
typepick = ttk.Combobox(packagewindow, values = ["Quick","Norm"])
typepick.place(x = 90, y = 80)

sendtotitle = tk.Label(master = packagewindow, text="Send to")
sendtotitle.place(x = 10, y = 115)
sendtopick = ttk.Combobox(packagewindow, values = ["Bangkok","Loei","Surin"])
sendtopick.place(x = 90, y = 115)

weighttitle = tk.Label(master = packagewindow, text="Weight")
weighttitle.place(x = 10, y = 150)
weightinput = tk.Entry(master = packagewindow)
weightinput.place(x = 90, y = 150)

enterbutton = Button(packagewindow, text = "Confirm", height = 5, width = 10, command = getmessage)
enterbutton.place(x = 350, y = 80)

packagewindow.mainloop()'''

'''checkwindow = Tk()           ###เช็คพัสดุ ยังไม่เสร็จ
checkwindow.title("Check Package")

checkwindow.geometry("300x500")
checkwindow.resizable(0,0)

def packagecheck():
    inputnumtitle.destroy()
    inputnum.destroy()
    search.destroy()

    packagenumbertitle = tk.Label(checkwindow, text="Package Number\n")
    packagenumbertitle.config(font=("", 12))
    packagenumbertitle.pack(anchor='center')
    packagenumber = tk.Label(checkwindow, text="NOR1234567890TH")
    packagenumber.config(font=("", 12))
    packagenumber.pack(anchor='center')





inputnumtitle = tk.Label(checkwindow, text="\n\n\n\n\n\n\n\n\nPlease enter package number")
inputnumtitle.config(font=("", 14))
inputnumtitle.pack(anchor='center')
inputnum = tk.Entry(checkwindow)
inputnum.pack(anchor='center')
search = Button(checkwindow, text="Search", command = packagecheck)
search.pack(anchor='center')

checkwindow.mainloop()'''


'''receipt = Tk()
receipt.title("Quix Express Receipt")
receipt.geometry("300x500")
receipt.resizable(0,0)

receipttitle = tk.Label(receipt, text="Quix Express Receipt\n")
receipttitle.config(font=("", 14))
receipttitle.pack(anchor='center')

sendname = tk.Label(receipt, text="Sender Name")
sendname.config(font=("", 10))
sendname.pack(anchor='w')

recipname = tk.Label(receipt, text="Recipient Name")
recipname.config(font=("", 10))
recipname.pack(anchor='w')

weightname = tk.Label(receipt, text="Weight")
weightname.config(font=("", 10))
weightname.pack(anchor='w')

pricename = tk.Label(receipt, text="Price")
pricename.config(font=("", 10))
pricename.pack(anchor='w')

kkto = tk.Label(receipt, text="KhonKaen to")
kkto.config(font=("", 10))
kkto.pack(anchor='w')

number = tk.Label(receipt, text="Packagenumber")
number.config(font=("", 14))
number.pack(anchor='center')

packagenumber = tk.Label(receipt, text="NOR1234567890TH")
packagenumber.config(font=("", 14))
packagenumber.pack(anchor='center')

closebutton = Button(receipt, text="Close", command = receipt.destroy)
closebutton.pack(anchor='center')
receipt.mainloop()'''

'''def numinput():
    global numintitle,numinput,search
    numintitle = tk.Label(updatewindow, text="Please input your package number\n")
    numintitle.config(font=("", 12))
    numintitle.pack(anchor='center')
    numinput = tk.Entry(updatewindow)
    numinput.pack(anchor='center')
    search = Button(updatewindow, text="Search", command = update)
    search.pack(anchor='center')

def update():
    numintitle.destroy()
    numinput.destroy()
    search.destroy()
    packagenumtitle = tk.Label(updatewindow, text="Package Number")
    packagenumtitle.pack(anchor='center')
    packagenum = tk.Label(updatewindow, text="ABC1234567890TH")
    packagenum.pack(anchor='center')



updatewindow = Tk()
updatewindow.title("Update Status")
updatewindow.geometry("300x500")
updatewindow.resizable(0,0)

numinput()

updatewindow.mainloop()'''

import sys
import os
from tkinter import Tk, Label, Button

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

root = Tk()

Label(root, text="Hello World!").pack()
Button(root, text="Restart", command=restart_program).pack()

root.mainloop()