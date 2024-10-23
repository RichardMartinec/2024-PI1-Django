prvocisla = [1, 2, 3]
delitel = 2
medzicislo = 3


print("Zadaj cele cislo vacsie ako 3:")
cislo = int(input())


while medzicislo < cislo:
    while delitel < medzicislo-1:
        if medzicislo % delitel == 0:
            #print(f"Číslo {medzicislo} NIE je prvočíslo")
            break
        delitel+=1
        if delitel == medzicislo-1:
            #print(f"Číslo {medzicislo} je prvočíslo")
            prvocisla.append(medzicislo)
    medzicislo+=1
    delitel = 2
while delitel < cislo-1:
    if cislo % delitel == 0:
      #print(f"Číslo {cislo} NIE je prvočíslo")
      break
    delitel+=1
    if delitel == cislo-1:
       #print(f"Číslo {cislo} je prvočíslo")
       prvocisla.append(cislo)
print("Najdene prvocisla su:", prvocisla)


    