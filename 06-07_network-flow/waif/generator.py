import random

n = random.randint(1, 10)
m = random.randint(1, 10)
p = random.randint(0, m)

print(n, m, p)

for j in range(n):
    k = random.randint(1, min(10, m))
    toys = random.sample(range(1, m+1), k)
    print(k, *toys)

unused_toys = set(range(1, n+1))
for j in range(p):
    l = random.randint(1, min(10, m+1))
    toys = set(random.sample(list(unused_toys), min(l, len(unused_toys))))
    for t in toys:
        unused_toys.remove(t)
    r = random.randint(1, l)
    print(l, *toys, r)