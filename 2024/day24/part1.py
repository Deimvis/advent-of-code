
with open('input.txt') as f:
    data = f.read()
    defs, gates = map(lambda s: s.split('\n'), data.split('\n\n'))

from collections import defaultdict
values = {}
din = defaultdict(int)
graph = defaultdict(set)
fns = {}

for d in defs:
    var, value = map(lambda s: s.strip(), d.split(':'))
    values[var] = int(value.strip())

for g in gates:
    expr, res = g.split('->')
    res_var = res.strip()
    inp1, op, inp2 = expr.strip().split()
    
    din[res_var] += 2
    graph[inp1].add(res_var)
    graph[inp2].add(res_var)
    if op == 'AND':
        fns[res_var] = lambda inp1=inp1, inp2=inp2: values[inp1] & values[inp2]
    elif op == 'OR':
        fns[res_var] = lambda inp1=inp1, inp2=inp2: values[inp1] | values[inp2]
    elif op == 'XOR':
        fns[res_var] = lambda inp1=inp1, inp2=inp2: values[inp1] ^ values[inp2]
    else:
        raise RuntimeError(f'Got unknown operator {op}')


from collections import deque
q = deque()
for node in values:
    if din[node] == 0:
        q.append(node)

while q:
    node = q.popleft()
    for neigh in graph[node]:
        din[neigh] -= 1
        if din[neigh] == 0:
            values[neigh] = fns[neigh]()
            q.append(neigh)

zvalues = []
for k, v in values.items():
    if k.startswith('z'):
        zvalues.append((k, v))
zvalues.sort(reverse=True)
ans = 0
for _, v in zvalues:
    ans = (ans << 1) + v
print(ans)
