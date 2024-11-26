import datetime

class Osoba:
    def __init__(self, meno, priezvisko, rok):     # koštruktor, funkcia, ktorá sa spustí pri vytváraní objektu
        self.meno = meno
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok

    def pozdrav(self):
        #print("Ahoj, ja som", self.meno, self.priezvisko, "a mám", self.vek, "rokov")
        print(f"Ahoj, ja som {self.meno} {self.priezvisko} a mám {self.vek} rokov")

class Student(Osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno, priezvisko, rok)
        self.trieda = trieda

    def pozdrav(self):
        Osoba.pozdrav(self)
        print(f"Som študent {self.trieda} triedy")


class Ucitel(Osoba):
    def __init__(self, meno, priezvisko, rok, titul="", trieda=""):
        super().__init__(meno, priezvisko, rok)
        self.titul = titul
        self.trieda = trieda

    def pozdrav(self):
        print(f"Dobrý deň, volám sa {self.titul} {self.meno} {self.priezvisko} a mám {self.vek} rokov")
        if self.trieda != "":
            print(f"Som triedny učiteľ {self.trieda} triede")

jano = Osoba("Ján", "Mrkvička", 2006)
jano.pozdrav()
fero = Osoba("Fero", "Marec", 2000)
fero.pozdrav()
student = Student("Ondrej", "Šarlina", 2007, "III.AT")
student.pozdrav()
sutek = Ucitel("Michal", "Šutek", 1978, "Mgr.", "III.AT")
palica = Ucitel("Michal", "Palica", 1985,)
sutek.pozdrav()
palica.pozdrav()