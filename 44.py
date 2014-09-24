#PROBLEM 44: Pentagon Numbers

import time
import math

start = time.clock()

pent = []
for i in range(1,10000):
    a = (i / 2) * (3 * i - 1)
    pent.append(int(a))

diffs = []

def ispent(num):
    n = (math.sqrt(24*num + 1) + 1)/6
    if n == int(n):
        return True
    else:
        return False

count = 0

for i in pent:
    count += 1
    for j in pent[count:]:
        if j > i:
            a = i + j
            b = i - j
            if ispent(a) and ispent(math.fabs(b)):
                diffs.append(math.fabs(b))
            
print(int(min(diffs)))

print(time.clock() - start)
