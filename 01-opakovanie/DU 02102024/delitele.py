delitel = 1

print("Zadaj cele cislo:")
cislo = int(input())


while delitel < cislo + 1:
    if cislo % delitel == 0:
        print(f"Číslo {cislo} je delitelne cislami: {delitel}")
        #print(delitel)
    delitel += 1
