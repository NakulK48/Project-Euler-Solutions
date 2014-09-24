#14

import time

def chain(a):
    chain = [a]
    num = a
    while num > 1:
        if num % 2 == 0:
            chain.append(num / 2)
        else:
            chain.append(3*num + 1)
        num = chain[-1]
    return len(chain)

def answer():
    start = time.clock()
    max = 0
    count = 2
    while count < 1000000:
        length = chain(count)
        if length > max:
            max = length
            highest = count
        count += 1
    print ("Chain is " + str(max) + " lengths long.")
    print (time.clock() - start)
    return highest
