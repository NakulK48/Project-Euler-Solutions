#PROBLEM 24 - Lexicographic Permutations

import math
import time

n = 10
digits = list(range(n))
d = list(digits)
dig = []

for i in d:
    dig.append(str(i))

d = "".join(dig)

permDigits = []
totalPerm = math.factorial(n)
target = 10**6

def solve(n, remainder):
    firstDigit = int((remainder-1)/ (math.factorial(n-1)))
    print(digits, permDigits)
    print()
    print(remainder, math.factorial(n-1))
    print(firstDigit)

    permDigits.append(digits.pop(firstDigit))
    if remainder == 0:
        print(permDigits)
        return
    else:
        try:
            solve(n-1, remainder - (firstDigit)*math.factorial(n-1))
        except ValueError:
            print(permDigits)
            return

start = time.clock()
solve(n, target)

b = []
for i in permDigits:
    b.append(str(i))

print()
print("Lexicographic permutation number", target, "of digits", d, "is:")
print("".join(b))
print()
print("Calculation took", time.clock() - start, "seconds.")


#1023456789 is permutation number 725760
#There are 362880 permutations beginning with 1
#We want number 274240
#9 beginning with each digit


