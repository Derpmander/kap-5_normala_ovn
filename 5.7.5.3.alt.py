import datetime

dt = datetime.datetime.now()
persnum = input ("Mata in ditt personnummer(yyyymmdd-xxxx): ")
persSplit = persnum.split("-")
dtpers = dt.strptime(persSplit[0], "%y%m%d")

if (dt.month == dtpers.month and dt.day == dtpers.day):
    print ("Grattis på födelsedagen ", dtpers.date())

if int(persSplit [1][-2]) % 2 == 0:
    print ("Woman")
else:
    print ("Man")