print("Please Select Menu")
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
        print("Your price is 55 Baht")