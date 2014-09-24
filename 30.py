#PROBLEM 30

def verify(a):
    b = str(a)
    sum = 0
    for i in b:
        sum += int(i)**5
    if sum == a:
        return True
    else:
        return False

def makeList(mx):
    i = 2
    a = []
    while i < mx:
        if verify(i):
            a.append(i)
        i += 1
    return a

def sol(mx):
    return sum(makeList(mx))
