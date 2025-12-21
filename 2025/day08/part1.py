
import sys
lines = [line.strip() for line in sys.stdin]
while len(lines) > 0 and len(lines[-1]) == 0:
    lines.pop()

CONNECTIONS = 1000

class DisjointSet:
    def __init__(self, n):
        self.node2root = {i:i for i in range(n)}
        self.node2rank = {i:0 for i in range(n)}

    def find(self, node):
        if self.node2root[node] != node:
            self.node2root[node] = self.find(self.node2root[node])
        return self.node2root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return False
        rank1 = self.node2rank[root1]
        rank2 = self.node2rank[root2]
        if rank1 <= rank2:
            self.node2root[root1] = root2
            self.node2rank[root2] += (rank1 == rank2)
        else:
            self.node2root[root2] = root1
        return True

def mysqrt(x):
    if x < 2:
        return x

    left = mysqrt(x >> 2) << 1
    right = left + 1
    return left if right * right > x else right

boxes = []
for l in lines:
    x, y, z = map(int, l.strip().split(','))
    boxes.append((x, y, z))
n = len(boxes)

from heapq import heappush, heappop
dists = []
for i in range(n):
    x1,y1,z1 = boxes[i]
    for j in range(i+1, n):
        x2,y2,z2 = boxes[j]
        d = mysqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
        heappush(dists, (-d, i, j))
        if len(dists) > CONNECTIONS:
            heappop(dists)

ds = DisjointSet(n)
for dneg, i, j in dists:
    ds.union(i, j)

sizes = [0]*n
for i in range(n):
    sizes[ds.find(i)] += 1

ans = 1
from itertools import islice
for sz in islice(sorted(sizes, reverse=True), 0, 3):
    ans *= sz
print(ans)