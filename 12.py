#12

def trigen():
    count = 1
    triangles = []
    while count < 100000:
        tri = 0.5 * count * (count+1)
        triangles.append(int(tri))
        count += 1
    for entry in triangles:
        numFactors = factorfind(entry)
        if numFactors > 500:
            return entry
            

def factorfind(a):
    count = 1
    lowfactors = []
    while count <= int((a**0.5)):
        if a % count == 0:
            lowfactors.append(count)
        count += 1
    factors = []
    for entry in lowfactors:
        factors.append(a)
    return (len(factors)*2)
        
        

        
    
