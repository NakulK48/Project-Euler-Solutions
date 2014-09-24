#10

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True

def answer(limit):
    count = 2
    sum = 0
    while count < limit:
        if isPrime(count):
            sum += count
        count += 1
    return sum
        
primes = []
