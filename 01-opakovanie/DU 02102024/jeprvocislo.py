delitel = 2
print("Zadaj cele cislo, vacsie ako 3:")
cislo = int(input())


while delitel < cislo-1:
    if cislo % delitel == 0:
      print(f"Číslo {cislo} NIE je prvočíslo")
      break
    delitel+=1
    if delitel == cislo-1:
       print(f"Číslo {cislo} je prvočíslo")
    