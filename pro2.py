from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk, Label, Button
import tkinter as tk
#import tkinter as Tk
import os
import sys
from PIL import ImageTk,Image
import sqlite3 as db
import sqlite3
conn = sqlite3.connect(r"D:\WorkKKU\1_2\ED251007\Chonlasit_Python\shipping.db")
c = conn.cursor()
global shipto
ntrack = []
sd = []
global send,recip,address,sendto,typ,weight

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def updatestatus():
    global updatewindow
    updatewindow = Tk()
    updatewindow.title("Update Status")
    updatewindow.geometry("350x500")
    updatewindow.resizable(0,0)
    #updatewindow.bind('<Return>',ifupdate)
    numinputupdate()
    updatewindow.mainloop()
    
def numinputupdate():
    
    global numintitle,numinputt,search,result
    numintitle = tk.Label(updatewindow, text="Input Tracking Number(for staff only)\n")
    numintitle.config(font=("", 12))
    numintitle.pack(anchor='center')

    numinputt = tk.Entry(updatewindow)
    numinputt.pack(anchor='center')

    #strack = numinputt.get()
    #a = numinputt.get()
    #a = [a,]
    #c.execute('SELECT * FROM  shippingcheck WHERE tracking = ?',a)
    #result = c.fetchone()
    #print(result[1])

    search = Button(updatewindow, text="Search", command = ifupdate)
    search.place(x = 100, y = 80)
    cancel = Button(updatewindow, text="Cancel", command = restart_program)
    cancel.place(x = 200, y = 80)

    #a = numinputt.get()
    #a = [a,]
    #c.execute('SELECT * FROM  shippingcheck WHERE tracking = ?',a)
    #result1 = c.fetchone()
    #print(result1[1])

    #global strack,result

def ifupdate():
    global a, strack
    strack = numinputt.get()
    a = numinputt.get()
    a = [a,]
    c.execute('SELECT * FROM  shippingcheck WHERE tracking = ?',a)
    result = c.fetchone()
    #print(str(result[1]))
    if str(result[1]) == 'LOE':
        updateloei()
    elif str(result[1]) == 'BKK':
        updatebangkok()
    elif str(result[1]) == 'SRU':
        updatesurin()
    #elif str(result[1]) == 'LOE':

    #update()
    #if result[1] == 'LOE' :
    #    update()

def updatebangkok():
    numintitle.destroy()
    numinputt.destroy()
    search.destroy()
    
    packagenumtitle = tk.Label(updatewindow, text="Package Number")
    packagenumtitle.grid(ipadx = 35, row = 0, column = 0)
    packagenum = tk.Label(updatewindow, text=a)
    packagenum.grid(row = 0, column = 1)

    emttitle1 = tk.Label(updatewindow, text=" ")
    emttitle1.grid(row = 1, column = 0)
    emttitle2 = tk.Label(updatewindow, text=" ")
    emttitle2.grid(row = 1, column = 1)

    kktitle = tk.Label(updatewindow, text = "KhonKaen")
    kktitle.grid(row = 2, column = 0)
    global kkbox2
    kkbox2 = ttk.Combobox(updatewindow, values = ["-","Pass this station","Received"])
    kkbox2.grid(row = 2, column = 1)

    emttitle3 = tk.Label(updatewindow, text=" ")
    emttitle3.grid(row = 3, column = 0)
    emttitle4 = tk.Label(updatewindow, text=" ")
    emttitle4.grid(row = 3, column = 1)

    nktitle = tk.Label(updatewindow, text = "Nakornrachasima")
    nktitle.grid(row = 4, column = 0)
    global nkbox
    nkbox = ttk.Combobox(updatewindow, values = ["-","Pass this station","Received"])
    nkbox.grid(row = 4, column = 1)

    emttitle5 = tk.Label(updatewindow, text=" ")
    emttitle5.grid(row = 5, column = 0)
    emttitle6 = tk.Label(updatewindow, text=" ")
    emttitle6.grid(row = 5, column = 1)

    title = tk.Label(updatewindow, text = "Saraburi")
    title.grid(row = 6, column = 0)
    global sarabox
    sarabox = ttk.Combobox(updatewindow, values = ["-","Pass this station","Received"])
    sarabox.grid(row = 6, column = 1)

    emttitle7 = tk.Label(updatewindow, text=" ")
    emttitle7.grid(row = 8, column = 0)
    emttitle8 = tk.Label(updatewindow, text=" ")
    emttitle8.grid(row = 8, column = 1)

    title = tk.Label(updatewindow, text = "Bangkok")
    title.grid(row = 9, column = 0)
    global bkkbox
    bkkbox = ttk.Combobox(updatewindow, values = ["-","Pass this station","Received"])
    bkkbox.grid(row = 9, column = 1)

    emttitle7 = tk.Label(updatewindow, text=" ")
    emttitle7.grid(row = 10, column = 0)
    emttitle8 = tk.Label(updatewindow, text=" ")
    emttitle8.grid(row = 10, column = 1)

    updatebutt = Button(updatewindow, text = "Update", command = setstatusbangkok)
    updatebutt.grid(row = 11, column = 0)
    canclebutt = Button(updatewindow, text = "Cancel", command = restart_program)
    canclebutt.grid(row = 11, column = 1)

def setstatusbangkok():
    kkbox2pick = kkbox2.get()
    if kkbox2pick == '-':
        c.execute('UPDATE bangkok SET khonkaen = "-" WHERE tracking = ?',a)
        conn.commit()
    elif kkbox2pick == 'Pass this station':
        c.execute('UPDATE bangkok SET khonkaen = "Pass this station" WHERE tracking = ?',a)
        conn.commit()
    elif kkbox2pick == 'Received':
        c.execute('UPDATE bangkok SET khonkaen = "Received" WHERE tracking = ?',a)
        conn.commit()
    nkboxpick = nkbox.get()
    if nkboxpick == '-':
        c.execute('UPDATE bangkok SET nakornrachasima = "-" WHERE tracking = ?',a)
        conn.commit()
    elif nkboxpick == 'Pass this station':
        c.execute('UPDATE bangkok SET nakornrachasima = "Pass this station" WHERE tracking = ?',a)
        conn.commit()
    elif nkboxpick == 'Received':
        c.execute('UPDATE bangkok SET nakornrachasima = "Received" WHERE tracking = ?',a)
        conn.commit()
    saraboxpick = sarabox.get()
    if saraboxpick == '-':
        c.execute('UPDATE bangkok SET saraburi = "-" WHERE tracking = ?',a)
        conn.commit()
    elif saraboxpick == 'Pass this station':
        c.execute('UPDATE bangkok SET saraburi = "Pass this station" WHERE tracking = ?',a)
        conn.commit()
    elif saraboxpick == 'Received':
        c.execute('UPDATE bangkok SET saraburi = "Received" WHERE tracking = ?',a)
        conn.commit()
    bkkboxpick = bkkbox.get()
    if bkkboxpick == '-':
        c.execute('UPDATE bangkok SET bangkok = "-" WHERE tracking = ?',a)
        conn.commit()
    elif bkkboxpick == 'Pass this station':
        c.execute('UPDATE bangkok SET bangkok = "Pass this station" WHERE tracking = ?',a)
        conn.commit()
    elif bkkboxpick == 'Received':
        c.execute('UPDATE bangkok SET bangkok = "Received" WHERE tracking = ?',a)
        conn.commit()
    restart_program()

def updateloei():
    numintitle.destroy()
    numinputt.destroy()
    search.destroy()
    
    packagenumtitle = tk.Label(updatewindow, text="Package Number")
    packagenumtitle.grid(ipadx = 35, row = 0, column = 0)
    packagenum = tk.Label(updatewindow, text=a)
    packagenum.grid(row = 0, column = 1)

    emttitle1 = tk.Label(updatewindow, text=" ")
    emttitle1.grid(row = 1, column = 0)
    emttitle2 = tk.Label(updatewindow, text=" ")
    emttitle2.grid(row = 1, column = 1)

    kktitle = tk.Label(updatewindow, text = "KhonKaen")
    kktitle.grid(row = 2, column = 0)
    global kkbox
    kkbox = ttk.Combobox(updatewindow, values = ["-","Pass this station","Received"])
    kkbox.grid(row = 2, column = 1)

    emttitle3 = tk.Label(updatewindow, text=" ")
    emttitle3.grid(row = 3, column = 0)
    emttitle4 = tk.Label(updatewindow, text=" ")
    emttitle4.grid(row = 3, column = 1)

    nbtitle = tk.Label(updatewindow, text = "Nongbualamphu")
    nbtitle.grid(row = 4, column = 0)
    global nbbox
    nbbox = ttk.Combobox(updatewindow, values = ["-","Pass this station","Received"])
    nbbox.grid(row = 4, column = 1)

    emttitle5 = tk.Label(updatewindow, text=" ")
    emttitle5.grid(row = 5, column = 0)
    emttitle6 = tk.Label(updatewindow, text=" ")
    emttitle6.grid(row = 5, column = 1)

    loeititle = tk.Label(updatewindow, text = "Loei")
    loeititle.grid(row = 6, column = 0)
    global loeibox
    loeibox = ttk.Combobox(updatewindow, values = ["-","Pass this station","Received"])
    loeibox.grid(row = 6, column = 1)

    emttitle7 = tk.Label(updatewindow, text=" ")
    emttitle7.grid(row = 7, column = 0)
    emttitle8 = tk.Label(updatewindow, text=" ")
    emttitle8.grid(row = 7, column = 1)

    updatebutt = Button(updatewindow, text = "Update", command = setstatusloei)
    updatebutt.grid(row = 8, column = 0)
    canclebutt = Button(updatewindow, text = "Cancel", command = restart_program)
    canclebutt.grid(row = 8, column = 1)

def setstatusloei():
    kkboxpick = kkbox.get()
    if kkboxpick == '-':
        c.execute('UPDATE loei SET khonkaen = "-" WHERE tracking = ?',a)
        conn.commit()
    elif kkboxpick == 'Pass this station':
        c.execute('UPDATE loei SET khonkaen = "Pass this station" WHERE tracking = ?',a)
        conn.commit()
    elif kkboxpick == 'Received':
        c.execute('UPDATE loei SET khonkaen = "Received" WHERE tracking = ?',a)
        conn.commit()
    nbboxpick = nbbox.get()
    if nbboxpick == '-':
        c.execute('UPDATE loei SET nongbualamphu = "-" WHERE tracking = ?',a)
        conn.commit()
    elif nbboxpick == 'Pass this station':
        c.execute('UPDATE loei SET nongbualamphu = "Pass this station" WHERE tracking = ?',a)
        conn.commit()
    elif nbboxpick == 'Received':
        c.execute('UPDATE loei SET nongbualamphu = "Received" WHERE tracking = ?',a)
        conn.commit()
    loeiboxpick = loeibox.get()
    if loeiboxpick == '-':
        c.execute('UPDATE loei SET loei = "-" WHERE tracking = ?',a)
        conn.commit()
    elif loeiboxpick == 'Pass this station':
        c.execute('UPDATE loei SET loei = "Pass this station" WHERE tracking = ?',a)
        conn.commit()
    elif loeiboxpick == 'Received':
        c.execute('UPDATE loei SET loei = "Received" WHERE tracking = ?',a)
        conn.commit()
    restart_program()

def updatesurin():
    numintitle.destroy()
    numinputt.destroy()
    search.destroy()
    
    packagenumtitle = tk.Label(updatewindow, text="Package Number")
    packagenumtitle.grid(ipadx = 35, row = 0, column = 0)
    packagenum = tk.Label(updatewindow, text=a)
    packagenum.grid(row = 0, column = 1)

    emttitle1 = tk.Label(updatewindow, text=" ")
    emttitle1.grid(row = 1, column = 0)
    emttitle2 = tk.Label(updatewindow, text=" ")
    emttitle2.grid(row = 1, column = 1)

    kktitle = tk.Label(updatewindow, text = "KhonKaen")
    kktitle.grid(row = 2, column = 0)
    global kkbox3
    kkbox3 = ttk.Combobox(updatewindow, values = ["-","Pass this station","Received"])
    kkbox3.grid(row = 2, column = 1)

    emttitle3 = tk.Label(updatewindow, text=" ")
    emttitle3.grid(row = 3, column = 0)
    emttitle4 = tk.Label(updatewindow, text=" ")
    emttitle4.grid(row = 3, column = 1)

    mhtitle = tk.Label(updatewindow, text = "Mahasarakham")
    mhtitle.grid(row = 4, column = 0)
    global mhbox
    mhbox = ttk.Combobox(updatewindow, values = ["-","Pass this station","Received"])
    mhbox.grid(row = 4, column = 1)

    emttitle5 = tk.Label(updatewindow, text=" ")
    emttitle5.grid(row = 5, column = 0)
    emttitle6 = tk.Label(updatewindow, text=" ")
    emttitle6.grid(row = 5, column = 1)

    rotitle = tk.Label(updatewindow, text = "Roiet")
    rotitle.grid(row = 6, column = 0)
    global robox
    robox = ttk.Combobox(updatewindow, values = ["-","Pass this station","Received"])
    robox.grid(row = 6, column = 1)

    emttitle7 = tk.Label(updatewindow, text=" ")
    emttitle7.grid(row = 8, column = 0)
    emttitle8 = tk.Label(updatewindow, text=" ")
    emttitle8.grid(row = 8, column = 1)

    sutitle = tk.Label(updatewindow, text = "Surin")
    sutitle.grid(row = 9, column = 0)
    global subox
    subox = ttk.Combobox(updatewindow, values = ["-","Pass this station","Received"])
    subox.grid(row = 9, column = 1)

    emttitle7 = tk.Label(updatewindow, text=" ")
    emttitle7.grid(row = 10, column = 0)
    emttitle8 = tk.Label(updatewindow, text=" ")
    emttitle8.grid(row = 10, column = 1)

    updatebutt = Button(updatewindow, text = "Update", command = setstatussurin)
    updatebutt.grid(row = 11, column = 0)
    canclebutt = Button(updatewindow, text = "Cancel", command = restart_program)
    canclebutt.grid(row = 11, column = 1)

def setstatussurin():
    kkbox3pick = kkbox3.get()
    if kkbox3pick == '-':
        c.execute('UPDATE surin SET khonkaen = "-" WHERE tracking = ?',a)
        conn.commit()
    elif kkbox3pick == 'Pass this station':
        c.execute('UPDATE surin SET khonkaen = "Pass this station" WHERE tracking = ?',a)
        conn.commit()
    elif kkbox3pick == 'Received':
        c.execute('UPDATE surin SET khonkaen = "Received" WHERE tracking = ?',a)
        conn.commit()
    mhboxpick = mhbox.get()
    if mhboxpick == '-':
        c.execute('UPDATE surin SET mahasarakham = "-" WHERE tracking = ?',a)
        conn.commit()
    elif mhboxpick == 'Pass this station':
        c.execute('UPDATE surin SET mahasarakham = "Pass this station" WHERE tracking = ?',a)
        conn.commit()
    elif mhboxpick == 'Received':
        c.execute('UPDATE surin SET mahasarakham = "Received" WHERE tracking = ?',a)
        conn.commit()
    roboxpick = robox.get()
    if roboxpick == '-':
        c.execute('UPDATE surin SET roiet = "-" WHERE tracking = ?',a)
        conn.commit()
    elif roboxpick == 'Pass this station':
        c.execute('UPDATE surin SET roiet = "Pass this station" WHERE tracking = ?',a)
        conn.commit()
    elif roboxpick == 'Received':
        c.execute('UPDATE surin SET roiet = "Received" WHERE tracking = ?',a)
        conn.commit()
    suboxpick = subox.get()
    if suboxpick == '-':
        c.execute('UPDATE surin SET surin = "-" WHERE tracking = ?',a)
        conn.commit()
    elif suboxpick == 'Pass this station':
        c.execute('UPDATE surin SET surin = "Pass this station" WHERE tracking = ?',a)
        conn.commit()
    elif suboxpick == 'Received':
        c.execute('UPDATE surin SET surin = "Received" WHERE tracking = ?',a)
        conn.commit()
    restart_program()
    
def createdb():
    conn = sqlite3.connect("shipping.db")
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS loei (tracking text,khonkaen text,nongbua lamphu text,loei text, deliver name text,receive name text,address text)')
    c.execute('CREATE TABLE IF NOT EXISTS surin (tracking text,khonkaen text,maha sarakham text,roiet text,surin text,deliver name text,receive name text,address text)')
    c.execute('CREATE TABLE IF NOT EXISTS bangkok (tracking text,khonkaen text,nakorn ratchasima text,saraburi text,bangkok text,deliver name text,receive name text,address text)')
    conn.commit()
    conn.close()

def quicktracking():

    import random
    global etrack
    global x
    for i in range(10):
        atrack = (random.randint(0,9))
        ntrack.append(atrack)
    a=0
    b=1
    for i in range(10):
        a=a+(ntrack[i]*(b))
        b=b*10
    etrack = 'QIX' + str(a) + 'TH'
    x = str(etrack) #etrack คือเลขพัสดุ
    x = [x,]
    #print('tracking number\t'+etrack)

def normaltracking():
    import random
    global rtrack
    global z
    for i in range(10):
        atrack = (random.randint(0,9))
        ntrack.append(atrack)
    a=0
    b=1
    for i in range(10):
        a=a+(ntrack[i]*(b))
        b=b*10
    rtrack = 'REG' + str(a) + 'TH'
    z = str(rtrack)
    z = [z,]
    #print('tracking number\t'+rtrack)

def addpackage() :
    window1.destroy()
    packagewindow = Tk()
    packagewindow.title("Add Package")
    #packagewindow.bind('<return>')

    packagewindow.geometry("500x200")
    packagewindow.resizable(0, 0)

    def getmessage():
        global typ,sendto
        send = sendernameinput.get()
        recip = recipnameinput.get()
        address = addressinput.get()
        sendto = sendtopick.get()
        typ = typepick.get()
        weight = float(weightinput.get())

        if sendtopick.get() == 'Bangkok' :
            if typepick.get() == 'Quick' :
                if weight <= 1 :
                    total = (weight + 30) + (7 * 4)
                elif 1 < weight <=10 :
                    total = (weight + 60) + (7 * 4)
                else :
                    total = (weight + 100) + (7 * 4)
                totalquick = str(int(total) + 1)
                quicktracking()
                c.execute('INSERT OR IGNORE INTO bangkok (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(etrack),'in system',send,recip,address,totalquick,weight))
                conn.commit()
                c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('QIX','BKK',str(etrack),send,recip,totalquick,weight))
                conn.commit()
                

            if typepick.get() == 'Norm' :
                if weight <= 1 :
                    total = (weight + 15) + (7 * 4)
                elif 1 < weight <=10 :
                    total = (weight + 15) + (7 * 4)
                else :
                    total = (weight + 50) + (7 * 4)
                totalquick = str(int(total) + 1)
                normaltracking()
                c.execute('INSERT INTO bangkok (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(rtrack),'in system',send,recip,address,totalquick,weight))
                conn.commit()
                c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('QIX','BKK',str(rtrack),send,recip,totalquick,weight))
                conn.commit()
                

        if sendtopick.get() == 'Loei' :
            if typepick.get() == 'Quick' :
                if weight <= 1 :
                    total = (weight + 30) + (7 * 4)
                elif 1 < weight <=10 :
                    total = (weight + 60) + (7 * 4)
                else :
                    total = (weight + 100) + (7 * 4)
                totalquick = str(int(total) + 1)
                quicktracking()
                c.execute('INSERT INTO loei (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(etrack),'in system',send,recip,address,totalquick,weight))
                conn.commit()
                c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('QIX','LOE',str(etrack),send,recip,totalquick,weight))
                conn.commit()
                

            if typepick.get() == 'Norm' :
                if weight <= 1 :
                    total = (weight + 15) + (7 * 4)
                elif 1 < weight <=10 :
                    total = (weight + 15) + (7 * 4)
                else :
                    total = (weight + 50) + (7 * 4)
                totalquick = str(int(total) + 1)
                normaltracking()
                c.execute('INSERT INTO loei (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(rtrack),'in system',send,recip,address,totalquick,weight))
                conn.commit()
                c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('NOR','LOE',str(rtrack),send,recip,totalquick,weight))
                conn.commit()
                

        if sendtopick.get() == 'Surin' :
            if typepick.get() == 'Quick' :
                if weight <= 1 :
                    total = (weight + 30) + (7 * 4)
                elif 1 < weight <=10 :
                    total = (weight + 60) + (7 * 4)
                else :
                    total = (weight + 100) + (7 * 4)
                totalquick = str(int(total) + 1)
                quicktracking()
                c.execute('INSERT INTO surin (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(etrack),'in system',send,recip,address,totalquick,weight))
                conn.commit()
                c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('QIX','SRU',str(etrack),send,recip,totalquick,weight))
                conn.commit()
                

            if typepick.get() == 'Norm' :
                if weight <= 1 :
                    total = (weight + 15) + (7 * 4)
                elif 1 < weight <=10 :
                    total = (weight + 15) + (7 * 4)
                else :
                    total = (weight + 50) + (7 * 4)
                totalquick = str(int(total) + 1)
                normaltracking()
                c.execute('INSERT INTO surin (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(rtrack),'in system',send,recip,address,totalquick,weight))
                conn.commit()
                c.execute('INSERT INTO shippingcheck (type,Province,tracking,delivername,recivename,price,weight) values (?,?,?,?,?,?,?)',('NOR','SRU',str(rtrack),send,recip,totalquick,weight))
                conn.commit()
                
        packagewindow.destroy()
        receipt()

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

    weighttitle = tk.Label(master = packagewindow, text="Weight(kg.)")
    weighttitle.place(x = 10, y = 150)
    weightinput = tk.Entry(master = packagewindow)
    weightinput.place(x = 90, y = 150)
    #weightinput.bind('<Return>',getmessage)

    confirmbutton = Button(packagewindow, text = "Confirm", height = 5, width = 10, command = getmessage)
    confirmbutton.place(x = 300, y = 80)

    backbutton = Button(packagewindow, text = "Back", height = 5, width = 10, command = restart_program)
    backbutton.place(x = 400, y = 80)

    packagewindow.mainloop()
    
def getdatabasebkkx():
    global result
    c.execute('SELECT * FROM bangkok WHERE tracking = ?',x)
    result = c.fetchone()
    #print(str(result[0]),str(result[5]),str(result[6]),str(result[8]),str(result[9]))

def getdatabasebkkz():
    global result
    c.execute('SELECT * FROM bangkok WHERE tracking = ?',z)
    result = c.fetchone()

def getdatabaseloeix():
    global result
    c.execute('SELECT * FROM loei WHERE tracking = ?',x)
    result = c.fetchone()
    #print(str(result[0]),str(result[4]),str(result[5]),str(result[7]),str(result[8]))

def getdatabaseloeiz():
    global result
    c.execute('SELECT * FROM loei WHERE tracking = ?',z)
    result = c.fetchone()

def getdatabasesurinx():
    global result
    c.execute('SELECT * FROM surin WHERE tracking = ?',x)
    result = c.fetchone()
    #print(str(result[0]),str(result[5]),str(result[6]),str(result[8]),str(result[9]))

def getdatabasesurinz():
    global result
    c.execute('SELECT * FROM surin WHERE tracking = ?',z)
    result = c.fetchone()

def receipt():
    if sendto == 'Bangkok' :
        if typ == 'Quick' :
            getdatabasebkkx()
        elif typ == 'Norm' :
            getdatabasebkkz()
    elif sendto == 'Loei' :
        if typ == 'Quick' :
            getdatabaseloeix()
        elif typ == 'Norm' :
            getdatabaseloeiz()
    elif sendto == 'Surin' :
        if typ == 'Quick' :
            getdatabasesurinx()
        elif typ == 'Norm' :
            getdatabasesurinz()

    global receipt
    receipt = Tk()
    receipt.title("Quix Express Receipt")
    receipt.geometry("300x500")
    receipt.resizable(0,0)

    receipttitle = tk.Label(receipt, text="Quix Express Receipt\n")
    receipttitle.config(font=("", 14))
    receipttitle.pack(anchor='center')

    sendname = tk.Label(receipt, text="Sender Name : ")
    sendname.config(font=("", 10))
    sendname.pack(anchor='w')
    #sendname2 = tk.Label(receipt, text=send)
    if sendto == 'Bangkok' or sendto == 'Surin' :
        sendname.config(text = 'Sender Name : '+str(result[5]))
    else :
        sendname.config(text = 'Sender Name : '+str(result[4]))
    #sendname2.place(x = 50, y = 50)

    recipname = tk.Label(receipt, text="Recipient Name : ")
    recipname.config(font=("", 10))
    if sendto == 'Bangkok' or sendto == 'Surin' :
        recipname.config(text = 'Recipient Name : '+str(result[6]))
    else :
        recipname.config(text = 'Recipient Name : '+str(result[5]))
    recipname.pack(anchor='w')

    weightname = tk.Label(receipt, text="Weight")
    weightname.config(font=("", 10))
    if sendto == 'Bangkok' or sendto == 'Surin' :
        weightname.config(text = 'Weight : '+str(result[9])+' Kg.')
    else :
        weightname.config(text = 'Weight : '+str(result[8])+' Kg.')
    weightname.pack(anchor='w')

    pricename = tk.Label(receipt, text="Price")
    pricename.config(font=("", 10))
    if sendto == 'Bangkok' or sendto == 'Surin' :
        pricename.config(text = 'Price : '+str(result[8])+' Baht')
    else :
        pricename.config(text = 'Price : '+str(result[7])+' Baht')
    pricename.pack(anchor='w')

    kkto = tk.Label(receipt, text="KhonKaen to")
    kkto.config(font=("", 10))
    if sendto == 'Bangkok' :
        kkto.config(text = 'KhonKaen to Bangkok')
    elif sendto == 'Surin' :
        kkto.config(text = 'KhonKaen to Surin')
    else :
        kkto.config(text = 'KhonKaen to Loei')
    kkto.pack(anchor='w')

    number = tk.Label(receipt, text="\nTracking number")
    number.config(font=("", 14))
    number.pack(anchor='center')

    packagenumber = tk.Label(receipt, text=str(result[0]))
    packagenumber.config(font=("", 14))
    packagenumber.pack(anchor='center')

    thx = tk.Label(receipt, text="Thank you for using the service\nWe will do our best\nand take care of your packages.")
    thx.config(font=("", 10))
    thx.pack()

    closebutton = Button(receipt, text="Close", command = restart_program)
    closebutton.pack(anchor='center')

    

    receipt.mainloop()

def checkagain():
    checkwindow.destroy()
    check()

def check():
    global checkwindow
    checkwindow = Tk()
    checkwindow.title("Check Status")
    checkwindow.geometry("350x500")
    checkwindow.resizable(0,0)
    numinputcheck()
    checkwindow.mainloop()

def numinputcheck():

    global numintitle2,numinputt2,search2,result2
    numintitle2 = tk.Label(checkwindow, text="Please input your package number\n")
    numintitle2.config(font=("", 12))
    numintitle2.pack(anchor='center')

    numinputt2 = tk.Entry(checkwindow)
    numinputt2.pack(anchor='center')

    search2 = Button(checkwindow, text="Search", command = ifcheck)
    search2.place(x = 100, y = 80)
    cancel2 = Button(checkwindow, text="Cancel", command = restart_program)
    cancel2.place(x = 200, y = 80)

def ifcheck():
    global b, strack
    strack = numinputt2.get()
    b = numinputt2.get()
    b = [b,]
    c.execute('SELECT * FROM  shippingcheck WHERE tracking = ?',b)
    result2 = c.fetchone()
    #print(str(result[1]))
    if str(result2[1]) == 'LOE':
        checkloei()
    elif str(result2[1]) == 'BKK':
        checkbangkok()
    elif str(result2[1]) == 'SRU':
        checksurin()

def checkloei():
    numintitle2.destroy()
    numinputt2.destroy()
    search2.destroy()

    c.execute('SELECT * FROM loei WHERE tracking = ?',b)
    conn.commit()
    result2 = c.fetchone()

    emttitle1 = tk.Label(checkwindow, text=" ")
    emttitle1.grid(row = 0, column = 0)
    emttitle2 = tk.Label(checkwindow, text=" ")
    emttitle2.grid(row = 0, column = 1)
    
    packagenumtitle = tk.Label(checkwindow, text="Package Number")
    packagenumtitle.grid(ipadx = 50, row = 1, column = 0)
    packagenum = tk.Label(checkwindow, text=b)
    packagenum.grid(row = 1, column = 1)

    emttitle1 = tk.Label(checkwindow, text=" ")
    emttitle1.grid(row = 2, column = 0)
    emttitle2 = tk.Label(checkwindow, text=" ")
    emttitle2.grid(row = 2, column = 1)

    kktitle = tk.Label(checkwindow, text = "KhonKaen")
    kktitle.grid(row = 3, column = 0)
    
    kkbox3 = tk.Label(checkwindow, text = str(result2[1]))
    kkbox3.grid(row = 3, column = 1)

    emttitle3 = tk.Label(checkwindow, text=" ")
    emttitle3.grid(row = 4, column = 0)
    emttitle4 = tk.Label(checkwindow, text=" ")
    emttitle4.grid(row = 4, column = 1)

    nktitle = tk.Label(checkwindow, text = "Nongbualamphu")
    nktitle.grid(row = 5, column = 0)
    nkbox2 = tk.Label(checkwindow, text = result2[2])
    nkbox2.grid(row = 5, column = 1)

    emttitle5 = tk.Label(checkwindow, text=" ")
    emttitle5.grid(row = 6, column = 0)
    emttitle6 = tk.Label(checkwindow, text=" ")
    emttitle6.grid(row = 6, column = 1)

    title = tk.Label(checkwindow, text = "Loei")
    title.grid(row = 7, column = 0)
    sarabox2 = tk.Label(checkwindow, text = result2[3])
    sarabox2.grid(row = 7, column = 1)

    emttitle7 = tk.Label(checkwindow, text=" ")
    emttitle7.grid(row = 8, column = 0)
    emttitle8 = tk.Label(checkwindow, text=" ")
    emttitle8.grid(row = 8, column = 1)

    updatebutt = Button(checkwindow, text = "Search Again", command = checkagain)
    updatebutt.grid(row = 9, column = 0)
    canclebutt = Button(checkwindow, text = "Exit", command = restart_program)
    canclebutt.grid(row = 9, column = 1)

def checkbangkok():
    numintitle2.destroy()
    numinputt2.destroy()
    search2.destroy()

    c.execute('SELECT * FROM bangkok WHERE tracking = ?',b)
    conn.commit()
    result2 = c.fetchone()
    
    emttitle1 = tk.Label(checkwindow, text=" ")
    emttitle1.grid(row = 0, column = 0)
    emttitle2 = tk.Label(checkwindow, text=" ")
    emttitle2.grid(row = 0, column = 1)

    packagenumtitle = tk.Label(checkwindow, text="Package Number")
    #packagenumtitle.config(font=("DB HelvethaicaMon X Bd", 20))
    packagenumtitle.grid(ipadx = 50, row = 1, column = 0)
    packagenum = tk.Label(checkwindow, text=b)
    packagenum.grid(row = 1, column = 1)

    emttitle1 = tk.Label(checkwindow, text=" ")
    emttitle1.grid(row = 2, column = 0)
    emttitle2 = tk.Label(checkwindow, text=" ")
    emttitle2.grid(row = 2, column = 1)

    kktitle = tk.Label(checkwindow, text = "KhonKaen")
    kktitle.grid(row = 3, column = 0)
    
    kkbox3 = tk.Label(checkwindow, text = str(result2[1]))
    kkbox3.grid(row = 3, column = 1)

    emttitle3 = tk.Label(checkwindow, text=" ")
    emttitle3.grid(row = 4, column = 0)
    emttitle4 = tk.Label(checkwindow, text=" ")
    emttitle4.grid(row = 4, column = 1)

    nktitle = tk.Label(checkwindow, text = "Nakornrachasima")
    nktitle.grid(row = 5, column = 0)
    
    nkbox2 = tk.Label(checkwindow, text = result2[2])
    nkbox2.grid(row = 5, column = 1)

    emttitle5 = tk.Label(checkwindow, text=" ")
    emttitle5.grid(row = 6, column = 0)
    emttitle6 = tk.Label(checkwindow, text=" ")
    emttitle6.grid(row = 6, column = 1)

    title = tk.Label(checkwindow, text = "Saraburi")
    title.grid(row = 7, column = 0)

    sarabox2 = tk.Label(checkwindow, text = result2[3])
    sarabox2.grid(row = 7, column = 1)

    emttitle7 = tk.Label(checkwindow, text=" ")
    emttitle7.grid(row = 8, column = 0)
    emttitle8 = tk.Label(checkwindow, text=" ")
    emttitle8.grid(row = 8, column = 1)

    title = tk.Label(checkwindow, text = "Bangkok")
    title.grid(row = 9, column = 0)
    global bkkbox
    bkkbox = tk.Label(checkwindow, text = result2[4])
    bkkbox.grid(row = 9, column = 1)

    emttitle7 = tk.Label(checkwindow, text=" ")
    emttitle7.grid(row = 10, column = 0)
    emttitle8 = tk.Label(checkwindow, text=" ")
    emttitle8.grid(row = 10, column = 1)

    updatebutt = Button(checkwindow, text = "Search Again", command = checkagain)
    updatebutt.grid(row = 11, column = 0)
    canclebutt = Button(checkwindow, text = "Exit", width = 10, command = restart_program)
    canclebutt.grid(row = 11, column = 1)

def checksurin():
    numintitle2.destroy()
    numinputt2.destroy()
    search2.destroy()

    c.execute('SELECT * FROM surin WHERE tracking = ?',b)
    conn.commit()
    result2 = c.fetchone()

    emttitle1 = tk.Label(checkwindow, text=" ")
    emttitle1.grid(row = 0, column = 0)
    emttitle2 = tk.Label(checkwindow, text=" ")
    emttitle2.grid(row = 0, column = 1)
    
    packagenumtitle = tk.Label(checkwindow, text="Package Number")
    packagenumtitle.grid(ipadx = 50, row = 1, column = 0)
    packagenum = tk.Label(checkwindow, text=b)
    packagenum.grid(row = 1, column = 1)

    emttitle1 = tk.Label(checkwindow, text=" ")
    emttitle1.grid(row = 2, column = 0)
    emttitle2 = tk.Label(checkwindow, text=" ")
    emttitle2.grid(row = 2, column = 1)

    kktitle = tk.Label(checkwindow, text = "KhonKaen")
    kktitle.grid(row = 3, column = 0)
    
    kkbox3 = tk.Label(checkwindow, text = str(result2[1]))
    kkbox3.grid(row = 3, column = 1)

    emttitle3 = tk.Label(checkwindow, text=" ")
    emttitle3.grid(row = 4, column = 0)
    emttitle4 = tk.Label(checkwindow, text=" ")
    emttitle4.grid(row = 4, column = 1)

    nktitle = tk.Label(checkwindow, text = "Mahasarakhom")
    nktitle.grid(row = 5, column = 0)
    
    nkbox2 = tk.Label(checkwindow, text = result2[2])
    nkbox2.grid(row = 5, column = 1)

    emttitle5 = tk.Label(checkwindow, text=" ")
    emttitle5.grid(row = 6, column = 0)
    emttitle6 = tk.Label(checkwindow, text=" ")
    emttitle6.grid(row = 6, column = 1)

    title = tk.Label(checkwindow, text = "Roiet")
    title.grid(row = 7, column = 0)

    sarabox2 = tk.Label(checkwindow, text = result2[3])
    sarabox2.grid(row = 7, column = 1)

    emttitle7 = tk.Label(checkwindow, text=" ")
    emttitle7.grid(row = 8, column = 0)
    emttitle8 = tk.Label(checkwindow, text=" ")
    emttitle8.grid(row = 8, column = 1)

    title = tk.Label(checkwindow, text = "Surin")
    title.grid(row = 9, column = 0)
    global bkkbox
    bkkbox = tk.Label(checkwindow, text = result2[4])
    bkkbox.grid(row = 9, column = 1)

    emttitle7 = tk.Label(checkwindow, text=" ")
    emttitle7.grid(row = 10, column = 0)
    emttitle8 = tk.Label(checkwindow, text=" ")
    emttitle8.grid(row = 10, column = 1)

    updatebutt = Button(checkwindow, text = "Search Again", command = checkagain)
    updatebutt.grid(row = 11, column = 0)
    canclebutt = Button(checkwindow, text = "Exit", command = restart_program)
    canclebutt.grid(row = 11, column = 1)

def mainwindow():
    global window1
    window1 = Tk()
    window1.title("Application")
    #window.minsize(width=200, height=200)
    #window.bind('<Return>',set_message)

    window1.geometry("800x450")
    window1.resizable(0, 0)

    headtop = Canvas(window1, bg="red", height=200, width=0)
    head = PhotoImage(file = "D:\WorkKKU\\1_2\\ED251007\\Project\\design.png")
    head_label = Label(window1, anchor=N, image=head)
    head_label.place(x=0, y=0, relwidth=1, relheight=1)
    headtop.pack()

    photo3 = PhotoImage(file = "D:\WorkKKU\\1_2\\ED251007\\Project\\design_03.png")
    button1 = tk.Button(window1, text="Add pasadu", image = photo3, bd = 0, command = addpackage)
    photo2 = PhotoImage(file = "D:\WorkKKU\\1_2\\ED251007\\Project\\design_05.png")
    button2 = tk.Button(window1, text="Update pasadu", image = photo2, bd = 0, command = updatestatus)
    photo1 = PhotoImage(file = "D:\WorkKKU\\1_2\\ED251007\\Project\\design_07.png")
    button3 = tk.Button(window1, text="Check pasadu", image = photo1, bd = 0, command = check)
    photo = PhotoImage(file = "D:\WorkKKU\\1_2\\ED251007\\Project\\design_09.png")
    button4 = tk.Button(window1, text="Exit Program", image = photo, bd = 0, command=window1.destroy)

    button1.place(x = 70, y = 226)
    button2.place(x = 258, y = 226)
    button3.place(x = 446, y = 226)
    button4.place(x = 635, y = 226)

    window1.mainloop()

#def login()
    windowlogin = Tk()
    windowlogin.title("Login")

mainwindow()
conn.commit()
conn.close()