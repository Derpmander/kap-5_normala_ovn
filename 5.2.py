t = str(input("Skriv en text: "))
print(len(t))
print(f"Det första tecknet är {t[0]}")
h = len(t)
h = h - 1
print(f"Det sista tecknet är {t[h]}")

if t[0]==t[h]:
    print("Good job")
elif t[0] != t[h]:
    print("No") 