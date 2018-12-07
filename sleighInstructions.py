#adventofcode day 7

import sys

class worker:
    def __init__(self, id):
        self.id=id
class node:
    def __init__(self, id):
        self.children = []
        self.parents = []
        self.id = id
    def addChild(self, node):
        self.children.append(node)
    def addParent(self, node):
        self.parents.append(node)
    def removeChild(self,node):
        if node in self.children:
            self.children.remove(node)
    def removeParent(self, node):
        if node in self.parents:
            self.parents.remove(node)
    def getChildren(self):
        return self.children
    def getParents(self):
        return self.parents

def printNodes(nodeList):
    print([node.id for node in nodeList])

def reset(lines):
    nodes = {}
    for instruction in lines:
        parentId = instruction[5] #index of the two ids: 5 and 36.
        childId = instruction[36]
        if parentId not in nodes.keys():
            nodes[parentId] = node(parentId)
        if childId not in nodes.keys():
            nodes[childId] = node(childId)
        nodes[parentId].addChild(nodes[childId])
        nodes[childId].addParent(nodes[parentId])
    return nodes

with open(sys.argv[1]) as f:
    lines = f.readlines()

nodes=reset(lines)

ready = sorted(filter(lambda x: len(x.getParents()) == 0 and len(x.getChildren()) > 0,nodes.values()), key=lambda x: x.id)
leaves = filter(lambda x: len(x.getChildren()) == 0,nodes.values())

tail=""
output=""
for node in sorted(leaves, key=lambda x: x.id):
    tail+=node.id

while len(ready) > 0:
    next = ready[0]
    output+=next.id
    for node in nodes.values():
        node.removeParent(next)
    next.children.clear()
    ready = sorted(filter(lambda x: len(x.getParents()) == 0 and len(x.getChildren()) > 0,nodes.values()), key=lambda x: x.id)

#part 1
print(output+tail)

nodes = reset(lines)
ready = sorted(filter(lambda x: len(x.getParents()) == 0 and len(x.getChildren()) > 0,nodes.values()), key=lambda x: x.id)
workers = [worker(x) for x in range(5)]

#while len(ready) > 0:
#    while len(ready) > 0 and len(workers) > 0:
        