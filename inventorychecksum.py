import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

twoCount = 0
threeCount = 0
for id in lines:
    counts = {}
    for char in id:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    if 2 in counts.values():
        twoCount += 1 
    if 3 in counts.values():
        threeCount += 1
print(twoCount * threeCount)

sharedLetters = ""
for i in range(len(lines[0])):
    boxes = set()
    for transformed in map(lambda id: id[:i] + id[i+1:], lines):
        if transformed in boxes:
            sharedLetters = transformed
            break
        else:
            boxes.add(transformed)
    if len(sharedLetters) > 1:
        break
print(sharedLetters)