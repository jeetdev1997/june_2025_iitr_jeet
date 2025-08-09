import math
def manhattan_distance(x1, y1, x2, y2):
    diff_x = x1 - x2
    diff_y = y1 - y2
    if(diff_x < 0):
        diff_x = diff_x * (-1)
    if(diff_y < 0):
        diff_y = diff_y * (-1)
    distance = diff_x + diff_y
    return distance



distance1 = manhattan_distance(2, 3, 5, 1)
print(distance1) 
distance2 = manhattan_distance(0, 0, 0, 0) 
print(distance2) 
distance3 = manhattan_distance(-1, -1, 1, 1)
print(distance3) 




