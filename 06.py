#6

def squaresum(limit):
    count = 1
    sum = 0
    while count <= limit:
        sum += (count)**2
        count += 1
    return sum

def sumsquare(limit):
    sum = 1/2 * (limit) * (limit+1)
    return int(sum**2)

print (sumsquare(100) - squaresum(100))
