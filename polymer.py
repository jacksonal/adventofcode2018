import sys

def react(polymer):        
    newStr = ""
    while len(polymer) > 0:
        if len(newStr) == 0:
            newStr+=polymer[0]
            polymer = polymer[1:]
        else:
            #just compare the tail of the new string (case swapped) with the head of the old string and pop them both if equal
            if newStr[-1].swapcase() == polymer[0]:
                newStr=newStr[:-1]
                polymer=polymer[1:]
            else: #otherwise append the head of the old string to the tail of the new string.
                newStr+=polymer[0]
                polymer = polymer[1:]
    return newStr

with open(sys.argv[1]) as f:
    polymer = f.read()

print(len(react(polymer)))
length = len(polymer)
for i in range(65,91): #dumb way to get the alphabet.
    cur = f'{chr(i)}'
    copy = polymer.replace(cur,"")
    copy = copy.replace(cur.lower(),"")
    curLen = len(react(copy))
    length = min(length,curLen)
print(length)