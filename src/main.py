from Knn import Knn

knn = Knn()

points = [
    (1,[1,2]),
    (1,[2,2]),
    (2,[6,6]),
]

more_points = [
    (2,[5,3]),
    (2,[8,6]),
    (1,[2,1]),
]

test_point = [1,4.1]

print('added', knn.add_points(points), 'points')
print('added', knn.add_points(more_points), 'points')

print(knn.get_points())

classification = knn.classify(test_point)

print("Test point:", test_point)
print("The result was:", classification)
