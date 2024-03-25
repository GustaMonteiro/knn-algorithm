from Distances import euclidean_distance

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
        if not isinstance(obj[1], list) or not all(isinstance(x, float) or isinstance(x, int) for x in obj[1]):
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

    def add_points(self, points:list[tuple[int, list]]) -> int:
        if not self.is_valid_list_of_points(points):
            print("[Error] - You need to pass a list of tuples to insert points")
            return -1

        if len(points) == 0:
            print("[Warning] - The list of points was empty")
            return -1

        if self.__n == 0:
            self.__n = len(points[0][1])

        # check if all points has same length
        for point in points:
            if len(point[1]) != self.__n:
                print("[Error] - Not all provided points are incompatible with the dimension of the current points")
                print("[Info] - Dimension of current points:", self.__n)
                return -1

        for point in points:
            self.__points.append(point)

        return len(points)

    def get_points(self):
        return self.__points

    def classify(self, point: list[float | int], *args, **kwargs) -> int:
        metric_to_be_used = kwargs.get("metric") if kwargs.get("metric") is not None else self.__metric

        if not isinstance(point, list) or len(point) != self.__n:
            return -1

        distances = []

        for ref in self.__points:
            distance = metric_to_be_used(ref[1], point)
            distances.append((distance, ref[0]))

        distances.sort()

        print(distances)

        return distances[0][1]


