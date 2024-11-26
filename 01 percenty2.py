print("Zadaj max pocet bodov:")

max_bodov = int(input())

#funkcia na validaciu bodov


def validuj():
    while True: #nekonecny cyklus
        try:
            pocet_bodov = int(input(f"Zadaj pocet bodov (0 - {max_bodov} )\n"))

            if(0 <= pocet_bodov and pocet_bodov <= max_bodov):
                return pocet_bodov
            else:
                print(f"pocet bodov ma byt v rozsahu 0 po {max_bodov}")
        
        except ValueError:
            print("Jozefko ty si Kretenio")

def vypocitaj_percenta(pocet_bodov):
    return round((pocet_bodov / max_bodov) *100 , 2)

def klasifikacia(percenta):
        if(percenta >= 90 and percenta <= 100):
              print("\nMAS JEDNA\n")

        elif(percenta >= 75 and percenta <= 89):
                print("\nMAS DVA\n")

        elif(percenta <= 74 and percenta >= 50):
                print("\nMAS TRI\n")

        elif(percenta <= 49 and percenta >= 25):
                print("\nMAS STYRI\n")
            
        elif(percenta <= 24 and percenta >= 0):
                print("\nMAS PAT\n")



pocet_bodov = validuj()
percenta = vypocitaj_percenta(pocet_bodov)
hodnotenie = klasifikacia(percenta)

print(f"Pocet bodov je: {pocet_bodov} , Percenta: {percenta}")


