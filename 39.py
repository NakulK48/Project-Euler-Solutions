# PROBLEM 39

import math

squares = set()
  
MAX_SIDE = 1000

perimeterCounts = {}

for i in xrange(1000):
  squares.add(i**2)

for a in xrange(MAX_SIDE):
  for b in xrange(MAX_SIDE):
    cSquared = a**2 + b**2
    if cSquared in squares:
      p = a+b+int(math.sqrt(cSquared))
      if (p > 1000):
        continue
      if p not in perimeterCounts:
        perimeterCounts[p] = 0
      perimeterCounts[p] += 1
      
mostCommonPerimeter = max(perimeterCounts, 
  key=perimeterCounts.get)
  
print mostCommonPerimeter
