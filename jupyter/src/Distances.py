from math import sqrt
import numpy as np
from src.Settings import *

def dot_product(point_a: list, point_b: list) -> float:
    if len(point_a) != len(point_b) or len(point_a) < 2:
        return -1

    sum = 0
    for i in range(len(point_a)):
        sum += point_a[i] * point_b[i]

    return sum


def euclidean_distance(point_a: list, point_b: list) -> float:
    if GlobalSettings.USE_NUMPY_ARRAY:
        return np.linalg.norm(point_a-point_b)
    else:
        if len(point_a) != len(point_b) or len(point_a) < 2:
            return -1
    
        sum = 0
        for i in range(len(point_a)):
            sum += (point_a[i] - point_b[i]) ** 2
    
        return sqrt(sum)


def cosine_distance(point_a: list, point_b: list) -> float:
    if GlobalSettings.USE_NUMPY_ARRAY:
        return 1 - (
            (np.dot(point_a,point_b))
            / (np.sqrt(np.dot(point_a,point_a)) * np.sqrt(np.dot(point_b, point_b)))
        )
    else:
        if len(point_a) != len(point_b) or len(point_a) < 2:
            return -1
    
        return 1 - (
            (dot_product(point_a, point_b))
            / (sqrt(dot_product(point_a, point_a)) * sqrt(dot_product(point_b, point_b)))
        )
