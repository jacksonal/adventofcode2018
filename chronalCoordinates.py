#advent of code 2018 day 6
import sys

with open(sys.argv[1]) as f:
    rawCoordinates = f.readlines()

def distance(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])
def isEdge(p):
    return p[0] == minx or p[0] == maxx or p[1] == miny or p[1] == maxy

parsedCoords = [(int(raw.split(',')[0]),int(raw.split(',')[1])) for raw in rawCoordinates]

#determine the bounds of the plane
minx = miny = 10000
maxx = maxy = 0
for coord in parsedCoords:
    minx = min(minx,coord[0])
    maxx = max(maxx,coord[0])
    miny = min(miny,coord[1])
    maxy = max(maxy,coord[1])

withinrange = 0
#for each point in the plane, determine which input coordinate is closest
plane = {}
for x in range(minx,maxx):
    plane[x] = {}
    for y in range(miny, maxy):
        distances = sorted([(i, distance(parsedCoords[i],(x,y))) for i in range(len(parsedCoords))],key=lambda x:x[1])
        if sum([x[1] for x in distances]) < 10000: #part 2 find all points within 10000 of all input coordinates
            withinrange+=1
        if distances[0][1] == distances[1][1]: #no closest coordinate
            plane[x][y] = '.'
        else:
            plane[x][y] = distances[0][0]

area = {x:0 for x in range(len(parsedCoords))}
area['.'] = 0
#accumulate area
for x in range(minx,maxx):
    for y in range(miny, maxy):
        if isEdge((x,y)) and plane[x][y] in area.keys():
            area.pop(plane[x][y])
        elif plane[x][y] in area.keys():
            area[plane[x][y]] += 1
#part1
print(max(area.values()))
#part2
print(withinrange)