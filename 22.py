#PROBLEM 22

import names

a = names.names
a.sort()



def letterscore(x):
    return (ord(x) - 64)

def wordsum(y):
    sum = 0
    for letter in y:
        sum += letterscore(letter)
    return sum

def solution():
    position = 1
    sum = 0
    for name in a:
        sum += (wordsum(name) * position)
        position += 1
    return sum
