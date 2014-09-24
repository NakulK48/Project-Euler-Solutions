#PROBLEM 52

#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import time

start = time.clock()

i = 1

truths = []

while True:
    truths = []
    a = str(i)
    f = str(6*i)
    if len(f) == len(a):
        A, B, C, D, E, F = [], [], [], [], [], [],
        for j in a:
            A.append(j)
        for j in str(2*i):
            B.append(j)
        for j in str(3*i):
            C.append(j)
        for j in str(4*i):
            D.append(j)
        for j in str(5*i):
            E.append(j)
        for j in f:
            F.append(j)
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        E.sort()
        F.sort()
        if A == B == C == D == E == F:
            print ("The answer is", a, "whose multiples are:",str(2*i),str(3*i),str(4*i),str(5*i),f)
            print ("That took",time.clock()-start,"seconds")
            break
    i += 1
