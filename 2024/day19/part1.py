
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]


ss = [s.strip() for s in lines[0].split(',')]
from aho import Aho
aho = Aho(ss)

ans = 0
for target in lines[2:]:
    t = target.strip()
    result = aho.search_words(t)
    from collections import defaultdict
    graph = defaultdict(list)
    for s, inds in result.items():
        for ind in inds:
            graph[ind].append(ind+len(s))
    
    def dfs(node, seen):
        if node == len(t):
            return True
        for neigh in graph[node]:
            if neigh not in seen:
                seen.add(neigh)
                if dfs(neigh, seen):
                    return True
        return False

    possible = dfs(0, set())
    ans += possible

print(ans)
