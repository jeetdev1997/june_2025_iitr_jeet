import math

def find_distance_2d(x1, y1, x2, y2):
    diff_x = x2 - x1
    diff_y = y2 - y1
    distance = math.sqrt((diff_x**2) + (diff_y**2))
    return distance

distance = find_distance_2d(5, 4, 2, 6)
print(distance)

