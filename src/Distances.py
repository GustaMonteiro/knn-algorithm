from math import sqrt

def euclidean_distance(point_a:list, point_b:list) -> float:
    if len(point_a) != len(point_b) or len(point_a) < 2:
        return -1
    
    sum = 0
    for i in range(len(point_a)):
        sum += (point_a[i] - point_b[i])**2

    return sqrt(sum)