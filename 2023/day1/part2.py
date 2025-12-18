
ans = 0
words = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
with open('input.txt') as f:
    for line in f:
        first = None
        last = None
        for i in range(len(line)):
            c = line[i]
            if c.isdigit():
                if first is None:
                    first = c
                last = c
            else:
                for word in words:
                    if line[max(i-4, 0):i+1].endswith(word):
                        c = words[word]
                        if first is None:
                            first = c
                        last = c
        ans += int(first + last)
print(ans)
