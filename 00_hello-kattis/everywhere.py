T = int(input())
unique_cities = set()

for _ in range(T):
    n = int(input())
    for _ in range(n):
        unique_cities.add(input())
    print(len(unique_cities))
    unique_cities.clear()