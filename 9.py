#9

import math

def answer():
    a = 1
    b = 1
    triplets = []
    while a < 1000:
        while b < 1000:
            d = (a**2 + b**2)
            c = math.sqrt(d)
            if c == int(c):
                triplets.append([a*b*c, a+b+c])
            b += 1
        b = 1
        a += 1
    for entry in triplets:
        if entry[1] == 1000:
            return entry[0]
                
        
