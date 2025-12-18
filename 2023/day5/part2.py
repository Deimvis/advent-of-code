
from collections import defaultdict
seeds = []
graph = defaultdict(lambda: defaultdict(list))
with open('input.txt') as f:
    line = f.readline()
    seeds_ranges = [int(s) for s in line[line.find(':')+1:].split()]
    for i in range(0, len(seeds_ranges), 2):
        seeds.append((seeds_ranges[i], seeds_ranges[i]+seeds_ranges[i+1]-1))
    src, dst = None, None
    for line in f:
        if line.strip() == '':
            continue
        if line.strip().endswith('map:'):
            signature = line.split()[0]
            src, _, dst = signature.split('-')
            continue
        dst_range_begin, src_range_begin, length = tuple(int(d) for d in line.split())
        rng = (src_range_begin, dst_range_begin, length)
        graph[src][dst].append(rng)


def intersect(rng1_begin, rng1_end, rng2_begin, rng2_end):
    begin = max(rng1_begin, rng2_begin)
    end = min(rng1_end, rng2_end)
    if end < begin:
        return None
    return (begin, end)


for src in graph:
    assert len(graph[src]) == 1
    for dst in graph[src]:
        graph[src][dst].sort()

ans = float('+inf')
for seed_range in seeds:
    rngs = [seed_range]  # [(rng_begin, rng_end)]
    type_ = 'seed'
    while type_ != 'location':
        dst_type = next(iter(graph[type_].keys()))
        rngmaps = graph[type_][dst_type]
        new_rngs = []
        i = 0
        for rng in rngs:
            rng_begin = rng[0]
            rng_end = rng[1]
            while rng_begin <= rng_end:
                while i < len(rngmaps) and rngmaps[i][0] <= rng_end and intersect(rng_begin, rng_end, rngmaps[i][0], rngmaps[i][0]+rngmaps[i][2]-1) is None:
                    i += 1
                if i == len(rngmaps) or rngmaps[i][0] > rng_end:
                    new_rngs.append(rng)
                    break
                common_rng = intersect(rng_begin, rng_end, rngmaps[i][0], rngmaps[i][0]+rngmaps[i][2]-1)
                assert common_rng is not None
                mapshift = rngmaps[i][1] - rngmaps[i][0]
                new_rng = [common_rng[0] + mapshift, common_rng[1] + mapshift]
                new_rngs.append(new_rng)
                if common_rng[0] > rng_begin:
                    free_rng = [rng_begin, common_rng[0]-1]
                    new_rngs.append(free_rng)
                rng_begin = common_rng[1]+1
        rngs = new_rngs
        new_rngs.sort()
        type_ = dst_type
    ans = min(ans, rngs[0][0])
print(ans)
