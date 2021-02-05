press1 = ["ลาดกระบัง >>> บางบ่อ   : 25","ลาดกระบัง >>> บางปะกง : 30","ลาดกระบัง >>> พนัสนิคม  : 45","ลาดกระบัง >>> บ้านบึง   : 55","ลาดกระบัง >>> บางพระ  : 60"]
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
        print(x)