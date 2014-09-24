#PROBLEM 31

import time

start = time.clock()

a = 1
b = 2
c = 5
d = 10
e = 20
f = 50
g = 100
h = 200

maxes = {}

x = [a,b,c,d,e,f,g,h]

for i in x:
    maxes[i] = int(200/i)

A,B,C,D,E,F,G,H = 0,0,0,0,0,0,0,0

ans = 0



while A <= maxes[a]:
    while B <= maxes[b]:
        while C <= maxes[c]:
            while D <= maxes[c]:
                while E <= maxes[c]:
                    while F <= maxes[c]:
                        while G <= maxes[c]:
                            while H <= maxes[c]:
                                if a*A + b*B + c*C + d*D + e*E + f*F + g*G + h*H == 200:
                                    print (A,B,C,D,E,F,G,H)
                                    ans += 1
                                H+= 1
                            G += 1
                            H = 0
                        F += 1
                        G = 0
                    E += 1
                    F = 0
                D += 1
                E = 0
            C += 1
            D = 0
        B += 1
        C = 0
    A += 1
    B = 0

print(ans)
print(time.clock() - start)
                                    
            

