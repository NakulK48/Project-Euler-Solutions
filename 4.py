#4

import time

def isp(b): #isPalindrome
    a = str(b)
    if a[::-1] == a: #Read the string backwards and compare with the original
        return True
    return False



def palinnum():
    start = time.clock()
    first = 0
    second = 0
    success = []
    while first < 1000:
        while second < 1000:
            result = first * second
            
            if isp(result):
                success.append(result)
            second += 1
        first += 1
        second = 0
    highest = 0
    for element in success:
        if element > highest:
            highest = element
            
    print (time.clock() - start)     
    return highest
    
        
        
