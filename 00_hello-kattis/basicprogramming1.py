# With if-statements instead of match-case. Python 3.10 supports
# match-case, but kattis runs Python 3.8, so this code has been
# rewritten to run in Python versions before 3.10.

import statistics as st

N, t = map(int, input().split())
A = list(map(int, input().split()))

if t == 1:
    print(7)
elif t == 2:
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    m = st.median(A[:3])
    print(m)
elif t == 4:
    print(sum(A))
elif t == 5:
    s = sum(i for i in A if i % 2 == 0)
    print(s)
elif t == 6:
    B = map(lambda x : x % 26, A)
    # chr() and ord() to convert between letters and int numbers
    # chr(97) = 'a', ord('a') = 97
    chars = map(lambda x : chr(x+97), B)
    print(''.join(chars))
elif t == 7:
    is_visited = [False] * N
    i = 0
    while True: 
        if i >= N:
            print("Out")
            break
        elif is_visited[i]:
            print("Cyclic")
            break
        elif i == N-1:
            print("Done")
            break
        else:
            is_visited[i] = True
            i = A[i]
