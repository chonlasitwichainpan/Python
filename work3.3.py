print("Input your fav food or type exit to exit program")
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
        break