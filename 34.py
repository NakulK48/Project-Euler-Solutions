#PROBLEM 34

import math

facs = []
for i in range(10):
    facs.append(math.factorial(i))

sols = []

for i in range(10**6):
    a = str(i)
    sm = 0
    for j in a:
        sm += int(facs[int(j)])
    if sm == i:
        sols.append(i)

print(sum(sols) - 3)
    
    
