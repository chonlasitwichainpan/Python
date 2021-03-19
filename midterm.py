import sqlite3 as db
import sqlite3
conn = sqlite3.connect(r"D:\WorkKKU\1_2\ED251007\Chonlasit_Pythonshipping.db")
c = conn.cursor()
global shipto
ntrack = []

   # c.execute('''INSERT INTO bangkok(khonkaen) VALUES('in system')''')
   # c.execute('INSERT INTO bangkok (tracking) values (?)',(str(etrack)))

def createdb():
    conn = sqlite3.connect("shipping.db")
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS loei (tracking text,khonkaen text,nongbua lamphu text,loei text, deliver name text,receive name text,address text)')
    c.execute('CREATE TABLE IF NOT EXISTS surin (tracking text,khonkaen text,maha sarakham text,roiet text,surin text,deliver name text,receive name text,address text)')
    c.execute('CREATE TABLE IF NOT EXISTS bangkok (tracking text,khonkaen text,nakorn ratchasima text,saraburi text,bangkok text,deliver name text,receive name text,address text)')
    conn.commit()
    conn.close()
    
def index():
    print('Quix Express')
    print('[1] add package\n[2] update package\n[3] checking track\n[x] exit')

def priceems():
    priceems =float(input('weight of package (kg) :'))
    if priceems <= 1 :
        Totalems = (priceems + 30) + (7*shipto)
    elif 1 < priceems <= 10 :
        Totalems = (priceems + 60) + (7*shipto)
    else:
        Totalems = (priceems + 100) + (7*shipto)
    ftotalems = str(int(Totalems)+1)
    print('\nTotal\t\t'+ftotalems +' baht')

def emstracking():
    import random
    global etrack
    for i in range(10):
        atrack = (random.randint(0,9))
        ntrack.append(atrack)
    a=0
    b=1
    for i in range(10):
        a=a+(ntrack[i]*(b))
        b=b*10
    etrack = 'EMS' + str(a) + 'TH'
    str(etrack)
    print('tracking number\t'+etrack)

def pricereg():
    shipto = int(input('\nDeliver to\n[4] Bangkok\n[5] Loei\n[6] Surin\n\nEnter your choice : '))
    if shipto == 4:
        priceems =float(input('weight of package (kg) :'))
        if priceems <= 1 :
            Totalems = (priceems + 15) + (7*shipto)
        elif 1 < priceems <= 10 :
            Totalems = (priceems + 15) + (7*shipto)
        else:
            Totalems = (priceems + 50) + (7*shipto)
        ftotalems = str(int(Totalems)+1)
        print('\nTotal\t\t'+ftotalems +' baht')
    elif shipto == 5:
        priceems =float(input('weight of package (kg) :'))
        if priceems <= 1 :
            Totalems = (priceems + 15) + (7*shipto)
        elif 1 < priceems <= 10 :
            Totalems = (priceems + 15) + (7*shipto)
        else:
            Totalems = (priceems + 50) + (7*shipto)
        ftotalems = str(int(Totalems)+1)
        print('\nTotal\t\t'+ftotalems +' baht')
    elif shipto == 6:
        priceems =float(input('weight of package (kg) :'))
        if priceems <= 1 :
            Totalems = (priceems + 15) + (7*shipto)
        elif 1 < priceems <= 10 :
            Totalems = (priceems + 15) + (7*shipto)
        else:
            Totalems = (priceems + 50) + (7*shipto)
        ftotalems = str(int(Totalems)+1)
        print('\nTotal\t\t'+ftotalems +' baht')

def regtracking():
    import random
    global rtrack
    for i in range(10):
        atrack = (random.randint(0,9))
        ntrack.append(atrack)
    a=0
    b=1
    for i in range(10):
        a=a+(ntrack[i]*(b))
        b=b*10
    rtrack = 'REG' + str(a) + 'TH'
    print('tracking number\t'+rtrack)

def add():
    dname = input('Enter your deliver name : ')
    rname = input('Enter your recive name : ')
    aname = input('Enter address of recieve : ')
    shipto = int(input('\nDeliver to\n[4] Bangkok\n[5] Loei\n[6] Surin\n\nEnter your choice : '))
    if shipto == 4:
        stype = input('\nkind of shipping\n[1] EMS\n[2] REG\n\nEnter your type : ')
        if stype == '1':
            priceems =float(input('weight of package (kg) :'))
            if priceems <= 1 :
                Totalems = (priceems + 30) + (7*shipto)
            elif 1 < priceems <= 10 :
                Totalems = (priceems + 60) + (7*shipto)
            else:
                Totalems = (priceems + 100) + (7*shipto)
            ftotalems = str(int(Totalems)+1)
            print('\nTotal\t\t'+ftotalems +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            emstracking()
            c.execute('INSERT INTO bangkok (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(etrack),'in system',dname,rname,aname,ftotalems,priceems))

        elif stype == '2':
            pricereg =float(input('weight of package (kg) :'))
            if pricereg <= 1 :
                Totalreg = (pricereg + 15) + (7*shipto)
            elif 1 < pricereg <= 10 :
                Totalreg = (pricereg + 15) + (7*shipto)
            else:
                Totalreg = (pricereg + 50) + (7*shipto)
            ftotalreg = str(int(Totalreg)+1)
            print('\nTotal\t\t'+ftotalreg +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            regtracking()
            c.execute('INSERT INTO bangkok (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(rtrack),'in system',dname,rname,aname,ftotalreg,pricereg))
    
    if shipto == 5:
        stype = input('\nkind of shipping\n[1] EMS\n[2] REG\n\nEnter your type : ')
        if stype == '1':
            priceems =float(input('weight of package (kg) :'))
            if priceems <= 1 :
                Totalems = (priceems + 30) + (7*shipto)
            elif 1 < priceems <= 10 :
                Totalems = (priceems + 60) + (7*shipto)
            else:
                Totalems = (priceems + 100) + (7*shipto)
            ftotalems = str(int(Totalems)+1)
            print('\nTotal\t\t'+ftotalems +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            emstracking()
            c.execute('INSERT INTO loei (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(etrack),'in system',dname,rname,aname,ftotalems,priceems))

        elif stype == '2':
            pricereg =float(input('weight of package (kg) :'))
            if pricereg <= 1 :
                Totalreg = (pricereg + 15) + (7*shipto)
            elif 1 < pricereg <= 10 :
                Totalreg = (pricereg + 15) + (7*shipto)
            else:
                Totalreg = (pricereg + 50) + (7*shipto)
            ftotalreg = str(int(Totalreg)+1)
            print('\nTotal\t\t'+ftotalreg +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            regtracking()
            c.execute('INSERT INTO loei (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(etrack),'in system',dname,rname,aname,ftotalreg,pricereg))
    if shipto == 6:
        stype = input('\nkind of shipping\n[1] EMS\n[2] REG\n\nEnter your type : ')
        if stype == '1':
            priceems =float(input('weight of package (kg) :'))
            if priceems <= 1 :
                Totalems = (priceems + 30) + (7*shipto)
            elif 1 < priceems <= 10 :
                Totalems = (priceems + 60) + (7*shipto)
            else:
                Totalems = (priceems + 100) + (7*shipto)
            ftotalems = str(int(Totalems)+1)
            print('\nTotal\t\t'+ftotalems +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            emstracking()
            c.execute('INSERT INTO surin (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(etrack),'in system',dname,rname,aname,ftotalems,priceems))

        elif stype == '2':
            pricereg =float(input('weight of package (kg) :'))
            if pricereg <= 1 :
                Totalreg = (pricereg + 15) + (7*shipto)
            elif 1 < priceems <= 10 :
                Totalreg = (pricereg + 15) + (7*shipto)
            else:
                Totalreg = (pricereg + 50) + (7*shipto)
            ftotalreg = str(int(Totalreg)+1)
            print('\nTotal\t\t'+ftotalreg +' baht')
            #สิ้นสุดการคำนวณราคาที่นี่
            regtracking()
            c.execute('INSERT INTO surin (tracking,khonkaen,delivername,recivename,address,price,weight) values (?,?,?,?,?,?,?)',(str(etrack),'in system',dname,rname,aname,ftotalreg,pricereg))

def register():
    username = input('Enter new username : ')
    password = input('Enter new password : ')
    c.execute('INSERT INTO login(username,password) VALUES(?,?)',(username,password))

def login():
    global verusername
    verusername = input('Enter your username : ',)
    verusername = (verusername,)
    c.execute('SELECT * FROM login WHERE username = ?',verusername)
    if c.fetchone():
        verpassword = input('Enter your password : ')
        c.execute('SELECT * FROM login WHERE username = ?',verusername)
        result = c.fetchone()
        '''
        for x in result:
            if verusername == x[1]:
                print('ได้แล้วมึงงง')
            else:
                print('ไปเขียนใหม่')
        '''
    else:
        print('ไม่พบ user')


c.execute('SELECT * FROM login')

conn.commit()
conn.close()