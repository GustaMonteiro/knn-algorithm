from enum import Enum
from math import sqrt

class Metrics(Enum):
    EUCLIDEAN = 1

class Distances:
    def euclidean_distance(a:tuple[float, float, str], b:tuple[float, float, str]) -> float:
        return sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))
