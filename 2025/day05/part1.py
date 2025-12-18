
import sys
lines = [line.strip() for line in sys.stdin]

intervals = []
for i in range(len(lines)):
    if len(lines[i].strip()) == 0:
        break
    s, e = map(int, lines[i].split('-'))
    intervals.append((s, e))

queries = list(map(int, lines[i+1:]))

# print(intervals, queries)
points = []
for s, e in intervals:
    points.append((s, 1))
    points.append((e+1, -1))
points.sort()
# print(points)
import itertools
upoints = []
for k, points in itertools.groupby(points, lambda x: x[0]):
    diff = 0
    for p in points:
        diff += p[1]
    if diff != 0:
        upoints.append((k, diff))
# print(upoints)
precalc = [(-1, False)]
cur = 0
for k, diff in upoints:
    cur += diff
    is_included = (cur > 0)
    if precalc[-1][1] != is_included:
        precalc.append((k, is_included))
# print(precalc)

import bisect
ans = 0
for v in queries:
    ind = bisect.bisect_right(precalc, (v, False))-1
    is_included = precalc[ind][1]
    ans += is_included
print(ans)
