#3

comp = 600851475143
factors = []
count = 1

while count < comp:
    if comp % count == 0:
        factors.append(count)
    count += 1

primefactors = []

for entry in factors:
    while count < comp:
        if comp % count == 0:
            primefactors.append(count)
        count += 1
