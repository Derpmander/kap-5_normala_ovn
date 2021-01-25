persnum = input(str("Skriv in ditt personnummer (yyyymmdd-xxxx):"))
print (persnum) 
print (f"det tal är nr {persnum[11]}")
if persnum[11] == 1:
    print ("Woman")
else:
    print ("Man")