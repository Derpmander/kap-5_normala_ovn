persnum = input(str("Skriv in ditt personnummer (yyyymmdd-xxxx):"))
print (persnum) 
print (f"det tal är nr {persnum[11]}")
if persnum[11] != 2 or 4 or 6 or 8 :
    print ("Woman")
elif persnum[11] == 2 or 4 or 6 or 8:
    print ("Man")