import sys

n = int(next(sys.stdin)) # number of plates
WEIGHT_LIMIT = 1000
weights = [int(next(sys.stdin)) for _ in range(n)]

def solve(n, W):
    M = [[0 for _ in range(W*2+1)] for _ in range(n+1)]

    if n == 0:
        return 0
    if n == 1:
        return weights[0]
    
    for i in range(1, n+1):  # row
        for w in range(W*2+1): # col
            if w < weights[i-1]:
                M[i][w] = M[i-1][w]
            else:
                take = weights[i-1] + M[i-1][w-weights[i-1]]
                drop = M[i-1][w]
                M[i][w] = closest_to_weight_limit(take, drop, M[i][w])

    return M[n][W*2]

def closest_to_weight_limit(take, drop, weight):
    diff1 = abs(take - (WEIGHT_LIMIT - weight))
    diff2 = abs(drop - (WEIGHT_LIMIT - weight))
    if diff1 == diff2:
        return max(take, drop)
    return take if diff1 < diff2 else drop

print(solve(n, WEIGHT_LIMIT))