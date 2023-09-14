res = [] # for printing results

T = int(input()) # number of test cases

def read_line(n):
    return list(map(int, input().split()))

for _ in range(T):
    n = int(input()) # number of ints on each line
    fst_line = read_line(n)
    snd_line = read_line(n)

    fst_line.sort()
    snd_line.sort(reverse=True)

    total = 0
    for x1, x2 in zip(fst_line, snd_line):
        total += x1 * x2

    res.append(total)

for i in range(T):
    print(f"Case #{i+1}: {res[i]}")