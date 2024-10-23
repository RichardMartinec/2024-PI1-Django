print('Zadaj cislo a')
a = int(input())
print('Zadaj cislo b')
b = int(input())

def scitanie(a,b):
    c = a+b
    print("Scitanie:" ,c)

def odcitanie(a,b):
    if(a > b):
       d = a-b
       print("Odcitanie:",d)
    else:
        d= b-a
        print("Odcitanie:",d)

def nasobenie(a,b):
    e = a*b
    print("Nasobenie:",e)

def podiel(a,b):
    f = a/b
    print("Podiel:",round(f,2))


if(a % 2  == 0):
   print("cislo a je párne")
else:
    print("cislo a je neparne")

if(b % 2  == 0):
   print("cislo b je párne")
else:
    print("cislo b je neparne")


scitanie(a,b)
odcitanie(a,b)
nasobenie(a,b)
podiel(a,b)




