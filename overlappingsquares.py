import sys, re

class square:
    def __init__(self):
        self.id=0
        self.x=0
        self.y=0
        self.height=0
        self.width=0
    def parse(self, input):
        m = re.match('#(\d+)\s*@\s*(\d+),(\d+):\s*(\d+)x(\d+)', input)
        self.id=m.group(1)
        self.x=int(m.group(2))
        self.y=int(m.group(3))
        self.width=int(m.group(4))
        self.height=int(m.group(5))
    def getPointsInSquare(self):
        ret = []
        for x in range(self.x,self.x + self.width):
            for y in range(self.y,self.y+self.height):
                ret.append(f'{x},{y}')
        return ret
        
with open(sys.argv[1]) as f:
    lines = f.readlines()
squares = []
noOverlaps = set()
for line in lines:
    s = square()
    s.parse(line)
    #print(s.getPointsInSquare())
    squares.append(s)
    noOverlaps.add(s.id) # assume no squares overlap at first.

print(f'{len(squares)} total squares')
counts = {}
for sq in squares:
    for coord in sq.getPointsInSquare():
        if coord not in counts.keys():
            counts[coord] = []
        counts[coord].append(sq.id) # build a meta-grid that tracks the id of each square that overlaps a coordinate
c = 0
for item in filter(lambda x: len(x[1]) > 1, counts.items()):
    c+=1 #count all coordinates that overlap (have more than 1 square id in the meta grid)
    for id in item[1]:
        if id in noOverlaps:
            noOverlaps.remove(id) #remove this square id from the set of squares that do not overlap.
print(c)
print(noOverlaps)