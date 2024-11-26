import random
import datetime

names_list = open("04-objekty/mena.txt", "r")
surnames_list = open("04-objekty/priezviska.txt", "r")
classes_list = ["AT","AI","IT"]

grade = random.randint(1,4)

years  = random.randint(2000,2007)
years_teacher  = random.randint(1978,1999)

#name = random.choice(names_list)
#surname = random.choice(surnames_list)
clas = random.choice(classes_list)

class Mainone:
    def __init__(self, name, surname, years, rank, clas):
        self.name = name
        self.surname = surname
        self.years = years
        self.age = datetime.date.today().year - self.years
        self.rank = rank
        self.clas = clas
        self.grade = grade

    def sentence(self):
        print(f"Ahoj, ja som {self.name} {self.surname}, mám {self.age} rokov a som {rank} {grade} {clas} triedy")


i = int(input("Zadaj, koľko chceš: "))
rank = input("Zadaj, čoho chem: ")

for x in names_list:
  print(x, names_list.readline())






