#PROBLEM 21

import time

start = time.clock()
def factorfind(a):
    mx = int(a/2) + 1
    factors = []
    for i in range(1,mx):
        if a % i == 0:
            factors.append(i)
    return sum(factors)

pairs = []

for a in range(10000):
    if a not in pairs:
        b = factorfind(a)
        if b < 10000 and factorfind(b) == a and a != b:
            pairs.append(a)
            pairs.append(b)

print(sum(pairs))
print("That took", time.clock()-start, "seconds")
            
