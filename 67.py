#PROBLEM 67

from def67 import triangle

for rowNum in range(98, -1, -1):
    length = len(triangle[rowNum])
    for colNum in range(length):
        maxChild = max(triangle[rowNum+1][colNum], triangle[rowNum+1][colNum+1])
        triangle[rowNum][colNum] += maxChild

print(triangle[0][0])
