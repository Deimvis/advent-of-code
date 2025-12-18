
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

from collections import defaultdict
graph = defaultdict(set)
for line in lines:
    src, dst = line.split('-')
    graph[src].add(dst)
    graph[dst].add(src)


nodes = list(graph.keys())
n = len(nodes)

def expand_clique(cur: set, i):
    maxclique = cur.copy()
    for j in range(i, n):
        neighs = graph[nodes[j]]
        if len(cur.intersection(neighs)) == len(cur):
            cur.add(nodes[j])
            if len(cur) > len(maxclique):
                maxclique = cur.copy()
            maxclique_next = expand_clique(cur, j+1)
            if len(maxclique_next) > len(maxclique):
                maxclique = maxclique_next.copy()
            cur.remove(nodes[j])
    return maxclique
        

maxclique = expand_clique(set(), 0)
ans = ','.join(sorted(maxclique))
print(ans)
