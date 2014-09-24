#PROBLEM 42

import words

a = words.words

triangles = []

for i in range(20):
    triangles.append(int(1/2*i*(i+1)))

def wordValue(word):
    sum = 0
    for letter in word:
        sum += ord(letter)-64
    return sum

count = 0

for word in a:
    b = wordValue(word)
    if b in triangles:
        count += 1

print(count)
