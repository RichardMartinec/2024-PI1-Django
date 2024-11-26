import random
import datetime

names_list = ["Juraj","Matúš","Michal","Jakub","Ondrej"]
surnames_list = ["Kráľovský","Veľký","Nový","Šikovný"]
ranks_list = ["Učiteľ", "študent"]
classes_list = ["AT","AI","IT"]

grade = random.randint(1,5)

years  = random.randint(1978,2007)

name = random.choice(names_list)
surname = random.choice(surnames_list)
rank = random.choice(ranks_list)
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


person1 = Mainone(name,surname,years,rank,clas)
person1.sentence()