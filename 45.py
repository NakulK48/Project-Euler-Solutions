#PROBLEM 45

import time

start = time.clock()
tri = []
pent = []
hexa = []

for i in range(100000):
    tri.append(int(i*(i+1)*1/2))
    pent.append(int(i*(3*i-1)*1/2))
    #You don't need a hexagon list. N(hexagon) will just be (N(tri)+1)/2

'''print (tri[:25])
print (pent[:25])
print (tri[1:][::2][:25])'''

i = 0

for num in tri:
    try:
        a = tri.index(num)
        b = pent.index(num)
        print(num, a, b, 1/2*(a+1))
    except ValueError:
        continue

print("That took", time.clock()-start, "seconds")
