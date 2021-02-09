import time
global numberofcompetitor
competitorname = []
points = []
shootingtime = []
hitfactor = []
timeis = time.localtime()
timenow = time.strftime('Date : %d %B %Y / Time : %H:%M:%S', timeis)
day = time.strftime('%A' , timeis)
year = time.strftime('%Y' , timeis)
numberofcompetitor = int (input ("Please enter number of Competitor : "))

def datetime() :
    timeis = time.localtime()
    timenow = time.strftime('Date : %d %B %Y / Time : %H:%M:%S', timeis)
    day = time.strftime('%A' , timeis)
    year = time.strftime('%Y' , timeis)

#def enternumcompetitor() :

def inputyourscore() :
    for num in range (numberofcompetitor) :
        data = input ("Please enter Competitor Information By (name,points,shootingtime) :>> ")
        datasplit = data.split(",") #แยกข้อมูลด้วย >>,<< จุดไข่น้อยๆอันนี้
        competitorname.append(datasplit[0])
        points.append(datasplit[1])
        shootingtime.append(datasplit[2])
        hitfactor.append(float(points[num])/float(shootingtime[num]))

def showscore() :
    print ("Shotgun "+day+" Traning "+year)
    print (timenow)
    print (""+"-"*120)
    print ("{0:-<10}{1:-<13}{2:-<12}{3:-<15}{4:-<20}{5:-<20}{6:-<20}".format('No.','Points','Time','Hit Factor','Stage Points,','Stage Percent','Competitor Name'))
    print (""+"-"*120)
    for maxhit in range(numberofcompetitor) :
        minhit = maxhit
        for minhit in range(numberofcompetitor) :
            if hitfactor[maxhit] > hitfactor[minhit] :
                hit,name,score,time = hitfactor[maxhit],competitorname[maxhit],points[maxhit],shootingtime[maxhit]
                hitfactor[maxhit],competitorname[maxhit],points[maxhit],shootingtime[maxhit] = hitfactor[minhit],competitorname[minhit],points[minhit],shootingtime[minhit]
                hitfactor[minhit],competitorname[minhit],points[minhit],shootingtime[minhit] = hit,name,score,time
    for num in range(numberofcompetitor) :
        stagepoints = (((hitfactor[num])/max(hitfactor)))*50
        stagepercents = (stagepoints/((max(hitfactor)/(max(hitfactor)))*50))*100
        print ("{0: <10}{1: <13}{2: <12}{3: <15}{4: <20}{5:-<20}{6: <20}".format(num+1,int(points[num]),shootingtime[num],'%.4f'%hitfactor[num],'%.4'%stagepoints,'%.2f'%stagepercents,competitorname[num]))
