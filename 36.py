#PROBLEM 36

def palin(num):
    a = str(num)
    if a == a[::-1]:
        return True
    else:
        return False

def binpalin(num):
    a = bin(num)[2:]
    if a == a[::-1]:
        return True
    else:
        return False

doublepalins = []

for i in range(1000000):
    if palin(i) and binpalin(i):
        doublepalins.append(int(i))

print(sum(doublepalins))
