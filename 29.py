#PROBLEM 29

def gen():
    a = 2
    b = 2
    c = []
    while a <= 100:
        while b <= 100:
            c.append(a**b)
            b += 1
        b = 2
        a += 1
    c.sort()
    return c

def solution(a):
    i = 1
    while i < len(a):
        if a[i-1] == a[i]:
            a.pop(i)
            solution(a)
        i += 1
    return a

a = solution(gen())
print(len(a))


