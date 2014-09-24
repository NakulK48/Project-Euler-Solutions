#7

def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    count = 2
    while count < int(num**0.5)+1:
        if num % count == 0:
            return False
        count += 1
    return True



def answer(a):
    count = 2
    sofar = 0
    while count < 10**10:
        
        if isPrime(count):
            sofar += 1
            if sofar == a:
                return (count)
                
        count += 1
