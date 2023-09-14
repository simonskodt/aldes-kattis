"""
This following solution gives 45 points.
"""

from collections import deque

men = deque() # stack for free proposers
man_rank, woman_rank = {}, {} # map from proposers/rejecters to their preference list
current_pairs = {} # map for current engagements

def main():
    # n lines to follow, m undirected edges
    n, m = map(int, input().split())

    setup(n, True)
    setup(n, False)

    # Gale-Shapley algorithm
    while men:
        man = men.pop() # choose a man
        woman = find_highest_ranked_woman(man)

        if is_free(woman):
            become_engaged(man, woman)
        else:
            other_man = current_pairs[woman]
            if w_prefer_m1_to_m2(woman, man, other_man):
                become_engaged(man, woman)
                men.append(other_man) # other_man becomes free
            else:
                men.append(man) # m2 and w remain engaged

    print_engagements()

def setup(n, is_man):
    for _ in range(n//2):
        line = input().split()
        name = line[0]
        if is_man:
            men.append(name)

        preferences = deque(line[1:]) if is_man else line[1:]
        rank_dict = man_rank if is_man else woman_rank
        rank_dict[name] = preferences

def become_engaged(man, woman):
    current_pairs[woman] = man

def find_highest_ranked_woman(man):
    return man_rank[man].popleft()

def is_free(woman):
    return current_pairs.get(woman) is None

def w_prefer_m1_to_m2(woman, m1, m2):
    w_pref = woman_rank[woman]

    return w_pref.index(m1) < w_pref.index(m2)

def print_engagements():
    for woman, man in current_pairs.items():
        print(woman, man)

if __name__ == "__main__":
    main()