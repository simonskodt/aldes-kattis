intervals, J = [], []

def main():
    n = int(input())

    for _ in range(n):
        s, f = map(int, input().split())
        intervals.append((s, f))

    # Timsort, O(n log n)
    intervals.sort(key=lambda x: x[1], reverse=True)

    for j in reversed(intervals):
        if len(J) == 0 or is_compatible_with_J(j):
            J.append(j)
        
    print(len(J))

def is_compatible_with_J(new_interval):
    """
    Check if the finish time of the current interval is less
    than or equal to the start time of another interval.
    """
    last_interval = J[-1]
    return last_interval[1] <= new_interval[0]

if __name__ == "__main__":
    main()