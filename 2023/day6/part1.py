
with open('input.txt') as f:
    time_line = f.readline()
    times = [int(t) for t in time_line[len('Time:'):].split()]
    distance_line = f.readline()
    distances = [int(d) for d in distance_line[len('Distance:'):].split()]

ans = 1
for t, d in zip(times, distances):
    opts = 0
    for wait_t in range(1, t):
        result_dist = wait_t * (t - wait_t)
        opts += result_dist > d
    ans *= opts
print(ans)
