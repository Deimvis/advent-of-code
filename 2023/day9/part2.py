
ans = 0
with open('input.txt') as f:
    for line in f:
        arr = list(map(lambda x: int(x), line.split()))
        layers = [arr]
        while not all(map(lambda x: x == 0, layers[-1])):
            new_layer = [layers[-1][i] - layers[-1][i-1] for i in range(1, len(layers[-1]))]
            layers.append(new_layer)
        val = 0
        for i in reversed(range(len(layers))):
            val = layers[i][0] - val
        ans += val
print(ans)
