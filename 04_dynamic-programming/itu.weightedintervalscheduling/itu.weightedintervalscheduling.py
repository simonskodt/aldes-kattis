import sys
from sys import stdin

# Prevent the default recursion limit
sys.setrecursionlimit(500_000)

# Number of intervals
n = int(next(stdin))

# Start interval s, end interval f, and weight w. 
intervals = [tuple(map(int, next(stdin).split())) for _ in range(n)]

# Sort the intervals by end interval, O(n log n)
intervals.sort(key=lambda end_interval: end_interval[1])

# Cache the results through memoization 
opt = [-1] * n

def main():
    res = solve(n-1)
    print(res)

def solve(i):
    """Recursive function to find the maximum total weight of non-overlapping intervals"""
    if opt[i] != -1:
        return opt[i]
    if i < 0:
        return 0
    if i == 0:
        return intervals[0][2]
    
    take = intervals[i][2] + solve(find_non_overlapping_interval(i) - 1)
    drop = solve(i-1)

    opt[i] = max(take, drop)
    return opt[i]

def find_non_overlapping_interval(i):
    """Initiate binary search with the start interval of the current interval"""
    current_start = intervals[i][0]
    return binary_search(intervals, current_start)

def binary_search(lst, target):
    """
    Find non-overlapping interval via binary search, O(log n).
    Compare the targets start interval to the end intervals
    of all other intervals.
    """
    low, high = 0, len(lst)

    while low < high:
        mid = (low + high) // 2

        if target < lst[mid][1]: # ignore right half
            high = mid
        else:                    # ignore left half
            low = mid + 1

    return low

def binary_search2(lst, target):
    """Find non-overlapping interval via binary search, O(log n)"""
    low, high = 0, len(lst)

    while low <= high:
        mid = (high+low) // 2

        if lst[mid][1] < target: # ignore left half
            low = mid+1
        elif lst[mid][1] > target: # ignore right half
            high = mid-1
        else: 
            return mid+1 # target is at mid
    
    return low # if element does not exist

if __name__ == "__main__":
    main()