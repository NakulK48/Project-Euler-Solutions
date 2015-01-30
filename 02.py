#2

memo = {0:1, 1:2}

def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

def fourmil():
    count = 1
    result = 0
    while result < 4000000:
        result = fib(count)
        count += 1
    count -= 1
    result = fib(count)
    return result, count

def answer():
    count = 1
    sum = 0
    while count < 32:
        if fib(count) % 2 == 0:
            sum += fib(count)
        count += 1

    return sum
