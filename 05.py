#5

def fits(a):
    factors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for entry in factors:
        if a % entry != 0:
            return False
    return True

def answer():
    
    count = 2520
    while count < 1000000000: #one billion
        if fits(count):
            return count
        count += 2520
    return "No answer found"
        
    
