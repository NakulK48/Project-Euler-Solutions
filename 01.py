import time

start = time.clock()
count = 0
sum = 0

while count < 1000:
    if count % 5 == 0 or count % 3 == 0:
        sum += count
    count += 1

print (sum)
print (time.clock() - start)
        
