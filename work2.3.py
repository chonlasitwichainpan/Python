print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\t\t\t\t\tPlease pick up your Item\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
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
print("\t\t\t\t\t5. "+store[4])