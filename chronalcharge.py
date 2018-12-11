#advent of code day 11

import sys

def calculatePowerLevel(x,y, serial):
    rackId = x + 10
    power = rackId * y
    power += serial
    power *= rackId
    power = (power // 100) % 10
    power -= 5
    return power

def get3x3Power(x,y,grid):
    power = 0
    for xprime in range(x-1,x+2):
        for yprime in range(y-1,y+2):
            power += grid[xprime][yprime]
    return power
serialNumber = int(sys.argv[1])

#fill in the power levels
grid = {}
for x in range(1,301):
    grid[x] = {}
    for y in range(1,301):
        grid[x][y] = calculatePowerLevel(x,y, serialNumber)

#determine most powerful 3x3 square.
maxPower = 0
topLeft = ""
for x in range(2,300):
    for y in range(2,300):
        squareId = (x-1,y-1)
        power = get3x3Power(x,y,grid)
        if power > maxPower:
            maxPower = power
            topLeft = f'{squareId}'

print(topLeft)