persnum = input(str("Skriv in ditt personnummer (yyyymmdd-xxxx):"))
print (persnum) 
print (f"det tal är nr {persnum[11]}")
if persnum[11] == 1 or persnum[11] == 3 or persnum[11] == 5 or persnum[11] == 7 or persnum[11] == 9:
    print ("Woman")
else:
    print ("Man")