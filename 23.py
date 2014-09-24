#PROBLEM 23

import math
import time

def facsum(n):
    i = 1
    facs = []
    while i < math.sqrt(n):
        if n % i == 0:
            facs.append(i)
            facs.append(int(n/i))
        i += 1
    return sum(facs) - n

def abund(n):
    if facsum(n) > n:
        return True
    else:
        return False

def abunds():
    i = 1
    a = []
    while i < 28123:
        if abund(i):
            a.append(i)
        i += 1
    return a

def sums():
    s = []
    a = abunds()
    i = 1
    j = i
    while i < len(a):
        while j < len(a):
            s.append(a[i]+a[j])
            j += 1
        i += 1
        j = i
    return s

def nonsums():
    start = time.clock()
    s = sums()
    n = []
    i = 1
    while i < 28123:
        if i not in s:
            n.append(i)
        i += 1
    print ("Execution took",time.clock()-start,"seconds")
    return sum(n)
    
