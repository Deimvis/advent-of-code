
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
    
    dp = [0]*(len(t)+1)
    dp[0] = 1
    for i in range(len(t)):
        for neigh in graph[i]:
            dp[neigh] += dp[i]
    
    options = dp[len(t)]
    ans += options

print(ans)
