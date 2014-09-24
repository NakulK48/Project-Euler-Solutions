#PROBLEM 26

from decimal import *

getcontext().prec = 1000

def dec(a):
    return (Decimal(1)/Decimal(a))

lengths = []

for i in range(1,1000):
    a = str(dec(i))
    for j in range(1,900):
        if a[2:j+2] == a[j+2:2*j+4]:
            k = j
            break
    lengths.append([i, j])

#UNSUCCESSFUL: abandoned
        
    
