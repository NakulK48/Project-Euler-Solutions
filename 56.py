#PROBLEM 56

import time

prods = []

start = time.clock()

for i in range(1,100): 
    for j in range(1,100):
        prods.append(i**j) #Generating table of powers

mx = 0

for prod in prods:
    sm = 0
    for digit in str(prod):
        sm += int(digit) #Calculate digital sum
    if sm > mx: #Compare to highest digital sum so far
        mx = sm

print(mx)
print("That took,", time.clock()-start, "seconds")
