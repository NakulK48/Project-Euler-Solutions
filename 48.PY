#PROBLEM 48

def solution(x):
    i = 1
    sum = 0
    while i <= x:
        sum += i**i
        i += 1
    a = str(sum)
    return a[-10:]
