import sys

freq = 0
history = {0}
found = False
with open(sys.argv[1]) as f:
    lines = f.readlines()
       
while found == False:
    for line in lines:       
        freq += int(line)
        if freq in history:
            found = True
            break
        else:
            history.add(freq)
print(freq)
    