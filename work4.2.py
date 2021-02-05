import os
choice = 0
vocabulary = {}

def menu() :
    global choice
    print ("Dictionary\n 1.Add Vocabulary\n 2.Show Vocabulary\n 3.Delete Vocabulary\n 4.Exit Program\n")
    choice = input ("Select your Order : ")

def addvocab() :
    vocab = input ("Input your Vocabulary : ")
    typ = input ("Input your type of Vocabulary (n , v , adj , adv) : ")
    mean = input ("Input your meaning of Vocabulary : ")
    vocabulary.update({vocab:{mean,typ}})
    print ("\n")

def showvocab() :
    print ("Your Vocabulary will show by \n Vocabulary  {'Type','Meaning'}")
    for key,value in vocabulary.items() :
        print (key+'          ',value)

def deletevocab() :
    delete = input ("Type Vocabulary you want to Delete : ")
    confirm = input ("Confirm you want to Delete Vocabulary (Y for YES or N for NO) : ")
    if confirm == 'y' :
        vocabulary.pop(delete)
        print ("You Delete >>"+delete+"<< from Dictionary")
    elif confirm == 'n' :
        print ("You didn't Delete Vocabulary\n")

while True :
    menu()
    if choice == '1' :
        clearscreen = os.system('cls')
        addvocab()
    elif choice == '2' :
        clearscreen = os.system('cls')
        showvocab()
    elif choice == '3' :
        clearscreen = os.system('cls')
        deletevocab()
    elif choice == '4' :
        a = input("Are you sure you want to Exit the Program (Y for YES or N for NO) : ")
        if a.lower() == 'n' :
            clearscreen = os.system('cls')
        elif a.lower() =='y' :
            clearscreen = os.system('cls')
            print ("You are Exit the Program")
            break