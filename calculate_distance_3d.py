import math

def calculate_distance_3d(x1, y1, z1, x2, y2, z2):
    diff_x = x2 - x1
    diff_y = y2 - y1
    diff_z = z2 - z1
    distance = math.sqrt((diff_x**2) + (diff_y**2) + (diff_z**2))
    return distance


distance = calculate_distance_3d(0, 0, 0, 1, 1, 1)
print(distance)

distance1 = calculate_distance_3d(2, 3, 5, 2, 3, 5)
print(distance1)

distance3 = calculate_distance_3d(1, 2, 3, 4, 6, 9)
print(distance3)
    

