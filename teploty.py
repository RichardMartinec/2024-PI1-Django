import random

teploty = []
poc=30
for i in range(poc):
    teploty.append(random.randint(-10,50))
print("Teploty pocas poslednych 30 dni boli: \n", teploty)


priemer  = 0

for i in range(poc):
    priemer = priemer + teploty[i]

priemer = priemer/poc
print("Priemerná teplota bola:",priemer)

najviac = teploty[0]
for i in range(poc):
    if najviac <= teploty[i]:
        najviac = teploty[i]
        poradie = i
        denporadie = (i+1) % 7
match denporadie:
    case 1:
        result = "Pondelok"
    case 2:
        result = "Utorok"
    case 3:
        result = "Streda"
    case 4:
        result = "Stvrtok"
    case 5:
        result = "Piatok"
    case 6:
        result = "Sobota"
    case 7:
        result = "Nedela"
print("Najvyššia teplota bola:",najviac, "a bola v:", poradie+1, "deň čo bol", result)
najmenej = teploty[0]
for i in range(poc):
    if najmenej >= teploty[i]:
        najmenej = teploty[i]
        poradie = i
        denporadie = (i+1) % 7
match denporadie:
    case 1:
        result = "Pondelok"
    case 2:
        result = "Utorok"
    case 3:
        result = "Streda"
    case 4:
        result = "Štvrtok"
    case 5:
        result = "Piatok"
    case 6:
        result = "Sobota"
    case 7:
        result = "Nedela"
print("Najnižšia teplota bola:",najmenej, "a bola v:", poradie+1, "deň, čo bol", result)