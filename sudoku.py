import json
import sys

def printboard(b):
    for row in b:
        print(row)

def findblanks(b):
    blanks = {}
    for i, row in enumerate(b):
        for j, val in enumerate(row):
            if val == '0':
                blanks[(i,j)] = 0
    return blanks


print(sys.argv[1])

boards = []
newboard = None
with open(sys.argv[1]) as f:
    for line in f:
        linelist = list(line.rstrip())
        if linelist[0] == 'G':
            print(line)
            boards.append(newboard)
            newboard = []
        else:
            newboard.append(linelist)
        # print()
    boards.append(newboard)

print(len(boards))
printboard(boards[1])
print(findblanks(boards[1]))
# print(json.dumps(boards, indent=2))