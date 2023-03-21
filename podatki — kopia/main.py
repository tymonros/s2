def isPrime(liczba):
    for i in range(2,int(liczba/2)+1):
        if liczba==2 or liczba==1:
            return True
        elif liczba%i==0:
            return False
    return True


liczba = int(input())
primeTab =[]
temp = liczba
while liczba > 0:
    if(isPrime(temp)==True):
        primeTab.append(temp)
        liczba-=temp
        temp = liczba
    else:
        temp-=1
suma = 0
for each in primeTab:
    suma+=1


