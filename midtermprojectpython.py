import sqlite3 as db
import sqlite3

ntrack = []
i = 0
def index():
    print('ขนส่งของพวยพิ้งและโบ๊ทๆ')
    print('[1] เพิ่มพัสดุ\n[2] อัพเดทพัสดุ\n[3] เช็คเลขแทร็กกิ้ง\n[x] ออกจากโปรแกรม')

def add():
    sname = input('ชื่อผู้ส่งพัสดุ :')
    gname = input('ชื่อผู้รับพัสดุ :')
    stype = input('รูปแบบการส่ง\n[1] ส่งด่วน EMS\n[2] ส่งธรรมดา REG\nเลือกรูปแบบที่ต้องการส่ง : ')
    if stype == '1':
        priceems()
        emstracking()
    else:
        pricereg()
        regtracking()
'''
def createdb():
    conn = sqlite3.connect("ploypinkshipping.db")
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS user (sname text,gname text,sprovince text,gprovince text,tracking text)')
    conn.commit()
    conn.close()

def addtodb():
    conn = sqlite3.connect("ploypinkshipping.db")
    c = conn.cursor()
    c.execute('INSERT INTO user (sname,gname,sprovince,gprovince,tracking) values (?,?,?,?,?)')
    conn.commit()
    conn.close()
'''
def priceems():
    print('สาขาปลายทาง\n[3] นครราชสีมา\n[4] กรุงเทพ')
    kk = int(input('เลือกสาขาปลายทาง : '))
    priceems =float(input('weight of package (kg) :'))
    if priceems <= 1 :
        Totalems = (priceems + 30) + (7*kk)
    elif 1 < priceems <= 10 :
        Totalems = (priceems + 60) + (7*kk)
    else:
        Totalems = (priceems + 100) + (7*kk)
    print(str(int(Totalems)+1) +' baht')
    
def pricereg():
    print('สาขาปลายทาง\n[3] นครราชสีมา\n[4] กรุงเทพ')
    kk = int(input('เลือกสาขาปลายทาง : '))
    priceems =float(input('weight of package (kg) :'))
    if priceems <= 1 :
        Totalems = (priceems + 15) + (7*kk)
    elif 1 < priceems <= 10 :
        Totalems = (priceems + 15) + (7*kk)
    else:
        Totalems = (priceems + 50) + (7*kk)
    print(str(int(Totalems)+1) +' baht')

def emstracking():
    import random
    for i in range(10):
        atrack = (random.randint(0,9))
        ntrack.append(atrack)
    a=0
    b=1
    for i in range(10):
        a=a+(ntrack[i]*(b))
        b=b*10
    print('EMS' + str(a) + 'TH')

def regtracking():
    import random
    for i in range(10):
        atrack = (random.randint(0,9))
        ntrack.append(atrack)
    a=0
    b=1
    for i in range(10):
        a=a+(ntrack[i]*(b))
        b=b*10
    print('REG' + str(a) + 'TH')

#finalprogram

while True:
    index()
    choose = input('choose menu : ')
    if choose == '1':
        a = int(input('number of box :'))
        while(i<a):
            add()
            i+=1
    elif choose == '2':
        c.execute ('''SELECT * FROM customers''')
        result = c.fetchall()
        for x in result:
            print(x)