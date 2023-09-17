import math

def main():
    n = int(input()) # number of lines
    coordinates = [tuple(map(float, input().split())) for _ in range(n)]

    pair = find_closest_pair(coordinates)
    print_closest_pair(pair)

def find_closest_pair(coordinates):
    """
    Return the closest pair of points from a list of coordinates.
    """
    sorted_points = sorted(coordinates, key=lambda x: x[0])
    closest_pair = closest_pair_rec(sorted_points)
    return closest_pair

def closest_pair_rec(points):
    """
    Recursively find the closest pair of points, a divide-and-conquer approach.
    """
    p_length = len(points)
    if (p_length <= 3):
        return brute_force_all_pair_wise_distances(points)
    
    mid = p_length // 2
    left = points[:mid]
    right = points[mid:]

    l_pair = closest_pair_rec(left)
    r_pair = closest_pair_rec(right)

    min_left = math.dist(l_pair[0], l_pair[1])
    min_right = math.dist(r_pair[0], r_pair[1])
    min_dist = min(min_left, min_right)

    points_in_strip = find_points_in_strip_and_sort(points, mid, min_dist)
    min_strip_dist, min_strip_points = calc_strip_distances(points_in_strip)

    if min_strip_dist < min_dist:
        return min_strip_points
    elif min_left < min_right:
        return l_pair
    else:
        return r_pair

def brute_force_all_pair_wise_distances(points):
    """
    Calculate the closest pair of points using a brute-force approach.
    """
    min_dist = float("inf")

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            current_dist = math.dist(points[i], points[j])
            if current_dist < min_dist:
                min_dist = current_dist
                closest_pair = (points[i], points[j])

    return closest_pair

def calc_strip_distances(strip):
    """
    Compute the closest pair of points within a strip of a specified width.
    """
    min_dist = float("inf")
    min_point = (0, 0)

    for i in range(len(strip)):
        for j in range(i+1, min(i+12, len(strip))):
            current_dist = math.dist(strip[i], strip[j])
            if current_dist < min_dist:
                min_dist = current_dist
                min_point = (strip[i], strip[j])

    return min_dist, min_point

def find_points_in_strip_and_sort(points, mid, min_dist):
    """
    Filter points within a specified strip width and sort them by y-coordinate.
    """
    mid_line = (points[mid-1][0] + points[mid][0]) / 2
    points_in_strip = [point for point in points if mid_line - min_dist < point[0] < mid_line + min_dist]
    return sorted(points_in_strip, key=lambda x: x[1])

def print_closest_pair(pair):
    """
    Print the coordinates of the closest pair of points.
    """
    for point in pair:
        print(f"{point[0]:.2f} {point[1]:.2f}")

if __name__ == "__main__":
    main()