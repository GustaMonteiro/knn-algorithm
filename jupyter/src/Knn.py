from src.Distances import euclidean_distance
import numpy as np
from src.Settings import *

class Knn:
    def __init__(self) -> None:
        self.__k: int = 1
        self.__n: int = 0
        self.__points: list[tuple[int, list]] = []
        self.__metric = euclidean_distance

    def clear(self):
        self.__n = 0
        self.__points.clear()

    def is_valid_point(self, obj) -> bool:
        if not isinstance(obj, tuple) or len(obj) != 2:
            return False
        if not isinstance(obj[0], int):
            return False
        if not isinstance(obj[1], list) or not all(
            isinstance(x, float) or isinstance(x, int) for x in obj[1]
        ):
            return False
        return True

    def is_valid_list_of_points(self, obj) -> bool:
        if not isinstance(obj, list):
            return False
        if not all(self.is_valid_point(x) for x in obj):
            return False
        return True

    def set_k(self, new_k):
        if new_k < 1:
            return -1

        self.__k = new_k

        return new_k

    def get_k(self):
        return self.__k

    def add_points(self, points: list[tuple[int, list]]) -> int:
        if not GlobalSettings.USE_NUMPY_ARRAY:
            if not self.is_valid_list_of_points(points):
                print("[Error] - You need to pass a list of tuples to insert points")
                return -1

        if len(points) == 0:
            print("[Warning] - The list of points was empty")
            return -1

        if self.__n == 0:
            self.__n = len(points[0][1])

        # check if all points has same length
        for _, coordinates in points:
            if len(coordinates) != self.__n:
                print(
                    "[Error] - Not all provided points are incompatible with the dimension of the current points"
                )
                print("[Info] - Dimension of current points:", self.__n)
                return -1

        self.__points += points
        print(len(points), "points were added!")
        
        return len(points)

    def get_points(self):
        return self.__points

    def classify(self, point: list[float | int], *args, **kwargs) -> int:
        metric_to_be_used = (
            kwargs.get("metric") if kwargs.get("metric") is not None else self.__metric
        )
        
        if not GlobalSettings.USE_NUMPY_ARRAY:
            if not isinstance(point, list) or len(point) != self.__n:
                return -1

        # distances = []
        possible_classification = -1
        smallest_distance = 99999999

        for classification, coordinates in self.__points:
            distance = metric_to_be_used(coordinates, point)
            if distance < smallest_distance:
                smallest_distance = distance
                possible_classification = classification
            # distances.append((distance, classification))

        # distances.sort()

        # _, classification = distances[0]

        return possible_classification
