print('Zadaj body max')
a = int(input())
print('Zadaj kolko mas bodov')
b = int(input())
c = b/a*100
print("Mas tolkoto" ,round(c,2) , "%")#round zaokruhli na 2 desatne miesta



if(c >= 90 and c <= 100):

    print("MAS JEDNA")

elif(c >= 75 and c <= 89):

    print("MAS DVA")

elif(c <= 74 and c >= 50):

    print("MAS TRI")

elif(c <= 49 and c >= 25):

    print("MAS STYRI")
    
elif(c <= 24 and c >= 0):

    print("MAS PAT")
