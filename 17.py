#PROBLEM 17

units = [""] + "one two three four five six seven eight nine".split()
unitLengths = []
for i in units:
    unitLengths.append(len(i))

hundredand = len("hundredand")
hundred = len("hundred")

teens = "ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
teenLengths = []
for i in teens:
    teenLengths.append(len(i))

tens = "twenty thirty forty fifty sixty seventy eighty ninety".split()
tenLengths = []
for i in tens:
    tenLengths.append(len(i))

onethousand = len("onethousand")
onehundred = len("onehundred")

def numberLength(n):
    if (n == 0):
        return 0
    if (n == 1000):
        return onethousand
    if (n == 100):
        return onehundred
    if (n < 10):
        return unitLengths[n]
    if (n < 20):
        return teenLengths[n-10]
    if (n < 100):
        u = n % 10
        ul = unitLengths[u]
        t = int(n/10)
        tl = tenLengths[t-2]
        return tl + ul
    else:
        utl = numberLength(n % 100)
        h = int(n/100)
        hl = unitLengths[h]
        if (utl == 0):
            return hl + hundred
        return utl + hl + hundredand

total = 0

for i in range(1, 1001):
    total += numberLength(i)

print(numberLength(342))
print(numberLength(115))
print(total)
        
