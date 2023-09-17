import math

closest_pair = []
n = int(input()) # number of lines
coordinates = [tuple(map(float, input().split())) for _ in range(n)]
sort_coord = sorted(coordinates, key=lambda x: x[0])

def main():
    min_dist = float('inf')

    for i in range(n-1):
        x = x_coord(i)
        y = x_coord(i+1)
        distance = math.dist([x], [y])
        if distance < min_dist:
            min_dist = distance
            update_closest_pair(i)

    print_coords()

def x_coord(i):
    return sort_coord[i][0]

def y_coord(i):
    return sort_coord[i][1]

def update_closest_pair(i):
    closest_pair.clear()
    closest_pair.append((x_coord(i), y_coord(i)))
    closest_pair.append((x_coord(i+1), y_coord(i+1)))

def print_coords():
    for coord in closest_pair:
        print(f"{coord[0]:.2f} {coord[1]:.2f}")

if __name__ == "__main__":
    main()