from Knn import Knn
from Distances import cosine_distance

knn = Knn()

points = [
    (1, [1, 2]),
    (1, [2, 2]),
    (2, [6, 6]),
]

more_points = [
    (2, [5, 3]),
    (2, [8, 6]),
    (1, [2, 1]),
]

test_point = [3, 4]

print("added", knn.add_points(points), "points")
print("added", knn.add_points(more_points), "points")

print(knn.get_points())

print("Test point:", test_point)
print("The result was:", knn.classify(test_point))
print("The cosine result was:", knn.classify(test_point, metric=cosine_distance))
