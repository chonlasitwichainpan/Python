'''choice = 0
choice2 = 0
game = ["Tom Clancy's Rainbow Six Siege : 540 Baht\n","Grand Theft Auto V : 699 Baht\n","Player Unknown's Battle Grounds : 599 Baht\n","Hunt Showdown : 719 Baht","Battlefield V : 1899 Baht\n"]
store = []

def menu() :
    global choice
    print("Menu\n 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม")
    choice = input('เลือกเมนู :')

def menu2() :
    global choice
    print(" 1.Tom Clancy's Rainbow Six Siege : 540 Baht\n 2.Grand Theft Auto V : 699 Baht\n 3.Player Unknown's Battle Grounds : 599 Baht\n 4.Hunt Showdown : 719 Baht\n 5.Battlefield V : 1899 Baht\n")
    choice2 = input("เลือกสินค้าเข้าตะกร้า")

while True :
    menu()
    if choice == '1' :
        print(" 1.Tom Clancy's Rainbow Six Siege : 540 Baht\n 2.Grand Theft Auto V : 699 Baht\n 3.Player Unknown's Battle Grounds : 599 Baht\n 4.Hunt Showdown : 719 Baht\n 5.Battlefield V : 1899 Baht\n")
    
    elif choice == '2' :
        while True :
            print(" 1.Tom Clancy's Rainbow Six Siege : 540 Baht\n 2.Grand Theft Auto V : 699 Baht\n 3.Player Unknown's Battle Grounds : 599 Baht\n 4.Hunt Showdown : 719 Baht\n 5.Battlefield V : 1899 Baht\n 6.Exit to menu")
            menu2()
            if choice2 =='1':
                store.add("RB6")
            elif choice2 =='2':
                store.add("GTAV")
            elif choice2 == '3':
                store.add("PUBG")
            elif choice2 == '4':
                store.add("Hunt")
            elif choice2 == '5':
                store.add("BFV")
            elif choice2 == '6':
                break

    elif choice == '3' :
        print(store)
    
    elif choice == '4' :'''




#เขียนโปรแกรมร้านขายของ   1.แสดงรายการสินค้า
#                       2.หยิบสินด้าเข้าตะกร้า
#                       3.แสดงจำนวนและราคาของสินค้า
#                       4.
#                       5.ปิดโปรแกรม

import os
choice = 0
gamecount = [0,0,0,0,0]
choose = 0
def menu() :
    global choice
    print("Menu\n 1.Show game list\n 2.Pice up your game to cart\n 3.Shows the quantity and price of the picked item\n 4.Remove your game from crat\n 5.Exit Program")
    choice = input("Select your Order : ")
    screen_clear()

def game() :
    print("GameList\n 1.Tom Clancy's Rainbow Six Siege : 540 Baht\n 2.Grand Theft Auto V : 699 Baht\n 3.Player Unknown's Battle Grounds : 599 Baht\n 4.Hunt Showdown : 719 Baht\n 5.Battlefield V : 1899 Baht\n")

def gamechoose() :
    global choose
    print("Chose Game From List\n 1.Tom Clancy's Rainbow Six Siege\n 2.Grand Theft Auto V\n 3.Player Unknown's Battle Grounds\n 4.Hunt Showdown\n 5.Battlefield V\n")
    choose = int(input("Choose your game by type Number :  "))
    if choose == 1 :
        gamecount[0] += 1
    elif choose == 2 :
        gamecount[1] += 1
    elif choose == 3 :
        gamecount[2] += 1
    elif choose == 4 :
        gamecount[3] += 1
    elif choose == 5 :
        gamecount[4] += 1
    screen_clear()

def showgamechoose() :
    list_game =['RB6' , 'GTA5' , 'PUBG' , 'HuntShowdown' , 'BF5']
    list_price =[540,699,599,719,1899]
    print("{0:-<13}{1:-<13}{2:-<13}{3}".format('Game' , 'Price' , 'amount' , 'TotalPrice'))
    for i in range(0,5) :
        print("{0:-<13}{1:-<13}{2:-<13}{3}".format(list_game[i],list_price[i],gamecount[i],gamecount[i]*list_price[i]))

def gameunchoose() :
    print('\t\nUnchoose Game From List\n 1.RB6\n 2.GTA5\n 3.PUBG\n 4.HuntShowdown\n 5.BF5')
    unchoose = int(input("Choose Number Of Game To Remove From List Or Type -1 To Exit"))
    if unchoose == 1:
        gamecount[0] -= 1
    elif unchoose == 2:
        gamecount[1] -= 1
    elif unchoose == 3:
        gamecount[2] -= 1
    elif unchoose == 4:
        gamecount[3] -= 1
    elif unchoose == 5:
        gamecount[4] -= 1

def screen_clear():
    clearscreen = os.system('cls')

while True :
    menu()
    if choice == '1' :
        screen_clear()
        game()
    elif choice == '2' :
        screen_clear()
        gamechoose()
    elif choice == '3' :
        screen_clear()
        showgamechoose()
    elif choice == '4' :
        gameunchoose()
        screen_clear()
    elif choice == '5' :
        a = input("Are you sure want to exit the program Y/N : ")
        if a.lower() == 'n' :
            screen_clear()
        elif a.lower() =='y' :
            screen_clear()
            break