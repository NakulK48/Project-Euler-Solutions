#PROBLEM 40

word = []

for i in range(1000000):
    word.append(str(i+1)) 

a = "".join(word) #Joining the list into a string

b = 1

for i in range(7): #Powers of ten up to one million
    c = 10**i
    b *= int(a[c-1]) #For example, the tenth digit will be b[9], so you need to subtract 1.

print(b)

#Answer = 210



