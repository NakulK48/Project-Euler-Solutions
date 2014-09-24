#PROBLEM 27

#Considering quadratics of the form:

   # n² + an + b, where |a| < 1000 and |b| < 1000

import math

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
                return False
    return True

highest = [0,0,0]

def countPrimes(a,b):
    i = 0
    while True:
        c = i**2 + a*i + b
        print(c, end=', ')
        if not isPrime(c):
            return i+1
        i += 1

for a in range(-1000,1000):
    for b in range(-1000,1000):
        d = countPrimes(a,b)
        if d > highest[2]:
            highest = [a,b,d]

print (highest)
print ("Product of a and b is: ", highest[0] * highest[1])

#Answer = -59231, a = -61, b = 971
            

            
        
