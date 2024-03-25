from Knn import Knn

knn = Knn()

points = [
    (1,[1,2]),
    (1,[2,2]),
    (2,[6,6]),
]

test_point = [4,4.1]

print('added', knn.add_points(points), 'points')

print(knn.get_points())

classification = knn.classify(test_point)

print("The result was:", classification)
