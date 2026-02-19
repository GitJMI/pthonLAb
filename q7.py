def checkPrime(num):
    isPrime = True
    if num == 0 or num == 1 :
        isPrime = False
    for i in range(2,(num//2)+1):
        if num % i == 0:
            isPrime = False
    return isPrime


list =[]
primeL = []
notPrimeL =[]
for i in range(20):
    list.append(i)
    
for i in list:
    if checkPrime(i):
        primeL.append(i)
        
    if checkPrime(i) == False:
        notPrimeL.append(i)

print(f"prime nos: {primeL}")
print(f"notPrimeL nos: {notPrimeL}")