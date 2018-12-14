#advent of code day 12

import sys


with open(sys.argv[1]) as f:
    initialState = "..." + f.readline().strip()[15:]
    f.readline()
    rawTransitions = f.readlines()

transitions = {}
for t in rawTransitions:
    transitions[t[:5]] = t[9]

state = initialState
for gen in range(20:
    print(f'generation {gen} first plant:{state.find("#")}')
    print(state.lstrip('.'))
    nextState = ""
    for potIndex in range(len(state)):
        startSlice = max(0,potIndex - 2)
        endSlice = min(len(state), potIndex + 3)
        segment = state[startSlice:endSlice]
        #print(f'pot index: {potIndex}')
        #print(f'taking [{startSlice}:{endSlice}]')
        
        if startSlice == 0:
            while len(segment) < 5:
                segment = "." + segment
        if endSlice == len(state):
            while len(segment) < 5:
                segment = segment + "."
        #print(segment)
        if segment in transitions:
            nextState += transitions[segment]
        else:
            nextState += "."
    state = nextState + "."
#print(state)
checkSum = 0
for i in range(len(state)):
    if state[i] == "#":
        checkSum += i - 3
print(checkSum)
