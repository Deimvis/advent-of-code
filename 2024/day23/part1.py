
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

from collections import defaultdict
graph = defaultdict(set)
for line in lines:
    src, dst = line.split('-')
    graph[src].add(dst)
    graph[dst].add(src)


ans = 0
nodes = list(graph.keys())
n = len(nodes)
for i in range(n):
    for j in range(i+1, n):
        for q in range(j+1,n):
            a,b,c = nodes[i],nodes[j],nodes[q]
            if len(set([a,b,c])) < 3: continue
            has_t = lambda x: x[0] == 't'
            if any(map(has_t, [a,b,c])) and (b in graph[a]) and (c in graph[a]) and (c in graph[b]):
                ans += 1
print(ans)
