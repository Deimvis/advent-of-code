
from collections import defaultdict, deque
seeds = []
graph = defaultdict(lambda: defaultdict(list))
with open('input.txt') as f:
    line = f.readline()
    seeds = [int(s) for s in line[line.find(':')+1:].split()]
    src, dst = None, None
    for line in f:
        if line.strip() == '':
            continue
        if line.strip().endswith('map:'):
            signature = line.split()[0]
            src, _, dst = signature.split('-')
            continue
        rng = tuple(int(d) for d in line.split())
        graph[src][dst].append(rng)


ans = float('+inf')
for seed in seeds:
    seen = set(['seed'])
    q = deque([('seed', seed)])
    while q:
        type_, val = q.popleft()
        if type_ == 'location':
            ans = min(ans, val)
            break
        for dst_type in graph[type_]:
            if dst_type not in seen:
                seen.add(dst_type)
                dst_val = None
                for rng in graph[type_][dst_type]:
                    if rng[1] <= val <= rng[1] + rng[2]:
                        dst_val = rng[0] + (val - rng[1])
                        break
                if dst_val is None:
                    dst_val = val
                q.append((dst_type, dst_val))
print(ans)