#name = input('What is your name?\n')
#print('Hi, %s.'%name)
#print('Welcome to Python.')

"""a = 10
b = 9
if a > b :
    print("a > b")
    print("ok")"""
#ถ้าจะคอมเมนท์ใช้ # หรือ """ หรือ ''' ก็ได้

'''name = input('What is your name?\n')
surname = input('What is your surname?\n')
gradelevel = input('What is your grade level?\n')
studentid = input('What is your student ID?\n')
print('\nName is %s.'%name)
print('Surname is %s.'%surname)
print('Grade level is %s.'%gradelevel)
print('Student ID is %s.'%studentid)'''

'''x = 20
y = 35.24
z = 1j
a = float(x)
b = int(y)
c = complex(x)
print(float(x),int(y),complex(x))'''

'''first = input('Input your First Number\n')
second = input('Input your Second Number\n')
third = input('Input your Third Number\n')
fourth = input('Input your Fourth Number\n')
fifth = input('Input your Fifth Number\n')
print('Float of %s Equal'%first,float(first))
print('Complex of %s Equal'%first,complex(first))
print('Float of %s Equal'%second,float(second))
print('Complex of %s Equal'%second,complex(second))
print('Float of %s Equal'%third,float(third))
print('Complex of %s Equal'%third,complex(third))
print('Float of %s Equal'%fourth,float(fourth))
print('Complex of %s Equal'%fourth,complex(fourth))
print('Float of %s Equal'%fifth,float(fifth))
print('Complex of %s Equal'%fifth,complex(fifth))'''

'''num1 = input('Input First Number\n')
num2 = input('Input Second Number\n')
print(num1+" = "+num2+" :", num1 == num2)
print(num1+" > "+num2+" :", num1 > num2)
print(num1+" < "+num2+" :", num1 < num2)'''

'''print(bool("Wadafak"))
print(bool(""))
print(bool(100))
print(bool(0))'''

'''a = 60
b = 13
c = 0

c = a & b
print(c)

c = a | b
print(c)

c = a ^ b
print(c)

c = ~a
print(c)

c = a << 2
print(c)

c = a >> 2
print(c)'''

'''print(">>>>>Day Converter Program<<<<<")
day = int(input('Input number of Days >>> '))
print(day," Days >>> Hours ",day*24," Hours")
print(day," Days >>> Minutes ",day*24*60," Minutes")
print(day," Days >>> Secounds ",day*24*60*60," Secounds")'''

'''friend = ["Jan","Cream","Phu","Bam","Aom","Pee","Bas","Kong","Da","James"]
#friend[9] = "May"
#friend[3] = "Boat"
friend.append("Dome")
friend.append("Poondang")
friend.insert(1,"Z-Sa")
friend.insert(8,"Ped")
friend.remove("Aom")
friend.pop()
friend.pop(3)
del friend[7]
friend.clear()
del friend
print(friend)'''

'''animal = {"cat","dog","rat","pig","ant"}
animal.add("monkey")
animal.update(["python","capybara","spider","wonbat","penguin","crocodile"])
print(animal)'''

'''print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\t\t\t\t\tPlease pick up your Item\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
store = []
for x in range(5) :
    item = input("\t\t\t\t\tPick up your Order "+str(x+1)+" is :   ")
    store.append(item)
print("\n")
print("\t\t\t\t\tYour Order in Shopping cart : ")
print("\t\t\t\t\t1. "+store[0])
print("\t\t\t\t\t2. "+store[1])
print("\t\t\t\t\t3. "+store[2])
print("\t\t\t\t\t4. "+store[3])
print("\t\t\t\t\t5. "+store[4])'''

'''press1 = ["ลาดกระบัง >>> บางบ่อ   : 25","ลาดกระบัง >>> บางปะกง : 30","ลาดกระบัง >>> พนัสนิคม  : 45","ลาดกระบัง >>> บ้านบึง   : 55","ลาดกระบัง >>> บางพระ  : 60"]
press2 = ["ลาดกระบัง >>> บางบ่อ   : 45","ลาดกระบัง >>> บางปะกง : 45","ลาดกระบัง >>> พนัสนิคม  : 70","ลาดกระบัง >>> บ้านบึง   : 90","ลาดกระบัง >>> บางพระ  : 100"]
press3 = ["ลาดกระบัง >>> บางบ่อ   : 60","ลาดกระบัง >>> บางปะกง : 70","ลาดกระบัง >>> พนัสนิคม  : 110","ลาดกระบัง >>> บ้านบึง   : 130","ลาดกระบัง >>> บางพระ  : 140"]
print(">>>>>>>>>>Motorway toll calculation program<<<<<<<<<<")
print("4 wheel car             press 1")
print("6 wheel car             press 2")
print("more then 6 wheel car   press 3")
press = int(input("\nSelect Your Type of Wheel : "))
if press == 1 :
    for x in press1 :
        print(x)
if press == 2 :
    for x in press2 :
        print(x)
if press == 3 :
    for x in press3 :
        print(x)'''

'''print("Please Select Menu")
print("Press 1 for extra pay")
print("Press 2 for rent pay")
press = int(input("Select Menu : "))
if press == 1 :
    distant1 = int(input("Input your distant : "))
    if distant1 < 25 :
        print("Your price is 25 Baht")
    else :
        print("Your price is 80 Baht")
if press == 2 :
    distant2 = int(input("Input your distant : "))
    if distant2 < 25 :
        print("Your price is 25 Baht")
    else :
        print("Your price is 55 Baht")'''

'''count = int(input("input count of number"))
i = 0
j = 0
while(i < count) :
    number = int(input("Input number : "))
    i += 1
    j = j + number
print("Total is : "+str(j))'''

'''print("Input your fav food or type exit to exit program")
i = 1
a = 0
food = []
while(i) :
    a = input("Your fav food No. "+str(i)+" is : ")
    food.append(a)
    i+=1
    if a=="exit" :
        print("Your fav food is :")
        print(food)
        break'''

'''a=[]
while True :
    b = input("---------\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ [x]\n")
    b = b.lower()
    if b == 'a' :
        c = input("ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด)")
        print("\n*****ข้อมูลเข้าสู่ระบบแล้ว*****\n")
    elif b == 's' :
        print("{0:-<6}{0:-<10}{0:-<10}".format(""))
        print("{0:-<8}{1:-<10}{2:10}".format("รหัส","ชื่อ","จังหวัด"))
        for d in a :
                e = d.split(":")
                print("{0[0]:<6}{0[1]:<10}({0[2]:<10})".format(e))
                continue
    elif b == 'x' :
        break
print("ทำคำสั่งต่อไป")'''

'''n =int(input('please enter student :'))
num = [0,0,0,0,0,0]
score = ['90-100','80-89','70-79','60-69','50-59','0-49']
for i in range(0,n):
    st =int(input('Enter student score :'))
    if st <= 100 and st >= 90 :
        num[0] +=1 
    elif st <= 89 and st >=80 :
        num[1] +=1
    elif st <= 79 and st >=70 :
        num[2] +=1
    elif st <=69 and st >=60 :
        num[3] +=1
    elif st <=59 and st >=50 :
        num[4] +=1
    else :
        num[5] +=1
for i in range(0,6):
    print(score[i]+':'+num[i]*'*')'''

'''import os
choice = 0
filename = ''

def menu() :
    global choice
    print("Menu\n 1.Open Steam\n 2.Open Notepad\n 3.Exit ")
    choice = input('Select Menu :')

def opennotepad() :
    filename = 'C:\\Windows\\notepad.exe'
    print('Memorandum writing %s' %filename)
    os.system(filename)
    
def opensteam() :
    filename = 'D:\\Steam\\steam.exe'
    print('Steam Game Luncher %s' %filename)
    os.system(filename)

while True :
    menu()
    if choice == '1' :
        opensteam()
    elif choice == '2' :
        opennotepad()
    else :
        break'''

'''def Introduce(arg1 , arg2 = 'com' , arg3 = 'ed' , arg4 = 'kku') :
    print("Hello, I am "+arg1+", "+arg2+" "+arg3+" "+arg4)

Introduce("Python")
Introduce(arg1 = "Python")
Introduce(arg1 = "Python" , arg3 = "Sci")
Introduce("python" , arg4 = "CMU")'''

choice = 0
def menu() :
    global choice
    print("1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปนแกรม")
    choice = input("Select menu :   ")

