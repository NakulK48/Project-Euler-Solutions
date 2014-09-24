#PROBLEM 39

triples = [[ 3 , 4 , 5 ], [ 5, 12, 13], [ 7, 24, 25], [ 8, 15, 17], [ 9, 40, 41], [11, 60, 61], [12, 35, 37], [13, 84, 85], [16, 63, 65], [20, 21, 29], [28, 45, 53], [33, 56, 65], [36, 77, 85], [39, 80, 89], [48, 55, 73], [65, 72, 97]]

triplemins = []

print(triples[0])

trip = []

for i in range(66):
    trip.append(0)

for sublist in triples:
    a = sublist[0]
    b = sublist[1]
    c = sublist[2]
    d = [b,c]
    triplemins.append(a)
    trip[a] = d

print(trip)
    
