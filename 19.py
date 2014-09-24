#PROBLEM 19b



def leapYear(year):
    if year%4 == 0:
        return True
    else:
        return False

def generate():
    lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leaplengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    a = []
    for bob in range(1901,2001):
        if leapYear(bob):
            a += leaplengths
        else:
            a += lengths
    return a

def solution(dayChosen):
    days = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    a = generate()
    initial = 1
    count = 0
    position = 0
    day = days.index(dayChosen)
    print("Day Chosen: " + dayChosen)
    for blob in a:
        initial += blob
        position += 1
        b = initial%7
        if b == day:
            count += 1
            c = position / 12
            d = (position % 12)
            
            
            print(months[d] + " " + str(int(c)+1901), end = ', ')
    return [count, days[day]]

print("Choose a day: ")
dayChosen = input()

e = solution(dayChosen)

print("Number of " + str(e[1]) + "s: " + str(e[0]))

#answer = 171
    




