#PROBLEM 69

import math

primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def isprime(n):
    if n <= 100:
        return n in primes_under_100
    if n % 2 == 0 or n % 3 == 0:
        return False

    for f in range(5, int(n ** .5), 6):
        if n % f == 0 or n % (f + 2) == 0:
            return False
    return True


def phi(x):
    div = []
    i = 1
    while i < int(math.sqrt(x)):
        if x % i == 0:
            if isprime(i):
                div.append(i)
            if isprime(int(x/i)):
                div.append(int(x/i))
        i += 1
    prod = 1
    for b in div:
        prod *= (1 - 1/b)
    return div
        
    
