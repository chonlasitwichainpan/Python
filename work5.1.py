#5.1
import os
def info() :
    global name,year,saka,kana,province
    clearscreen = os.system('cls')
    print("Introduce yourself by Name/Grade/Department/Faculty/Province\n")
    info = input ("Name-Surname / Grade / Department / Faculty / Province : ")
    infosplit = info.split('/')
    name = infosplit[0]
    year = infosplit[1]
    saka = infosplit[2]
    kana = infosplit[3]
    province = infosplit[4]

class nisit :
    def __init__(self,name,year,saka,kana,province) :
        self.name = name
        self.year = year
        self.saka = saka
        self.kana = kana
        self.province = province
    def shownisit(self) :
        print ("\nHi my name is : "+self.name+"   Student grade : "+self.year+" Department : "+self.saka+" Faculty : "+self.kana+" From : "+self.province+"\n")

info()
n = nisit(name,year,saka,kana,province)
n.shownisit()

#Chonlasit Wichainpan/1/Computer/Education/RoiEt