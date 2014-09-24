#PROBLEM 28

#Up to 500

def jump(n):
    if (n == 2):
        return 10
    else:
        return 8 + jump(n-1)

def base(n):
    if (n == 1):
        return 3
    else:
        return base(n-1) + jump(n)

    
def thisSpiral(n):
    thisBase = base(n)
    thisIncrement = n * 2
    return (4*thisBase + 6*thisIncrement)
    
total = 1

for i in range(500):
    total += thisSpiral(i+1)

print(total)
