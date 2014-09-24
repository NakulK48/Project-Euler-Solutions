#PROBLEM 25

result = {1:1, 2:1}

def fib(num):
    if num not in result:
        result[num] = fib(num-1) + fib(num-2)
    return result[num]

def solution():
    i = 3
    while True:
        i += 1
        a = fib(i)
        if len(str(a)) >= 1000:
            return i
