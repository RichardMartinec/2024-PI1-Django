import random
import datetime

#names_list = open("04-objekty/mena.txt", encoding="utf8")
#surnames_list = open("04-objekty/priezviska.txt", encoding="utf8")
classes_list = ["AT","AI","IT"]

#grade = random.randint(1,4)

#years  = random.randint(2000,2007)
#years_teacher  = random.randint(1978,1999)

#name = random.choice(names_list)
#surname = random.choice(surnames_list)
#clas = random.choice(classes_list)

class Mainone:
    def __init__(self, name, surname, years, rank, clas, grade):
        self.name = name
        self.surname = surname
        self.years = years
        self.age = datetime.date.today().year - self.years
        self.rank = rank
        self.clas = clas
        self.grade = grade

    def sentence(self):
        print(f"Ahoj, ja som {self.name} {self.surname}, mám {self.age} rokov a som {rank} {grade} {clas} triedy.")


i = int(input("Zadaj, koľko mien chceš: "))
rank = input("Zadaj, učiteľ alebo žiak: ")

if rank in ("ziak", "žiak"):
   for x in range(0, i):
        name_index = random.randint(1,199)
        names_list = open("04-objekty/mena.txt", encoding="utf8")
        for y in range(0,name_index):
            name = names_list.readline(15)
            #print(y, name, "\n")
        names_list.close()
        #print(y, "\n")
        #print(name_index, "\n")
        #print(name, "\n")
        surname_index = random.randint(1,952)
        surnames_list = open("04-objekty/priezviska.txt", encoding="utf8")
        for y in range(0,surname_index):
            surname = surnames_list.readline(15)
        surnames_list.close()
        years_ziak  = random.randint(2005,2008)
        clas = random.choice(classes_list)
        grade = random.randint(1,4)
        ziak = Mainone(name, surname, years_ziak, rank, clas, grade)
        ziak.sentence()
        #print(x, names_list.readline())
elif rank in ("ucitel", "učiteľ"):
    for x in range(0, i):
        name_index = random.randint(1,199)
        names_list = open("04-objekty/mena.txt", encoding="utf8")
        for y in range(0,name_index):
            name = names_list.readline(15)
        names_list.close()
        #print(name_index, "\n")
        #print(name, "\n")
        surname_index = random.randint(1,952)
        surnames_list = open("04-objekty/priezviska.txt", encoding="utf8")
        for y in range(0,surname_index):
            surname = surnames_list.readline(15)
        surnames_list.close()
        years_ucitel  = random.randint(1978,1999)
        clas = random.choice(classes_list)
        grade = random.randint(1,4)
        ucitel = Mainone(name, surname, years_ucitel, rank, clas, grade)
        ucitel.sentence()
        #print(x, names_list.readline())

  

  









