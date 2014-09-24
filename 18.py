#PROBLEM 18

triangle = []


triangle.append("75".split())
triangle.append("95 64".split())
triangle.append("17 47 82".split())
triangle.append("18 35 87 10".split())
triangle.append("20 04 82 47 65".split())
triangle.append("19 01 23 75 03 34".split())
triangle.append("88 02 77 73 07 63 67".split())
triangle.append("99 65 04 28 06 16 70 92".split())
triangle.append("41 41 26 56 83 40 80 70 33".split())
triangle.append("41 48 72 33 47 32 37 16 94 29".split())
triangle.append("53 71 44 65 25 43 91 52 97 51 14".split())
triangle.append("70 11 33 28 77 73 17 78 39 68 17 57".split())
triangle.append("91 71 52 38 17 14 91 43 58 50 27 29 48".split())
triangle.append("63 66 04 68 89 53 67 30 73 16 69 87 40 31".split())
triangle.append("04 62 98 27 23 09 70 98 73 93 38 53 60 04 23".split())

rows = len(triangle)

maxtotal = 0

def depth(row, column):
    thisCell = int(triangle[row][column])
    if (row == 14):
        return thisCell
    else:
        return max(thisCell + depth(row+1, column), thisCell + depth(row+1, column+1))

print(depth(0,0))
