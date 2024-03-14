from distances import Metrics, Distances

__metrics = {Metrics.EUCLIDEAN: Distances.euclidean_distance}

def classify(list_of_points:list[tuple[float, float, str]], k:int, point:tuple[float, float], metric:Metrics = Metrics.EUCLIDEAN) -> str:
    distances = []

    for current in list_of_points:
        distance = __metrics[metric](point, current)
        distances.append((distance, current[2]))

    distances.sort()

    counter = {}

    for i in range(k):
        category = distances[i][1]

        if category in counter:
            counter[category] += 1
        else:
            counter[category] = 1

    max_count = 0
    classification = ""

    for category, count in counter.items():
        if count > max_count:
            max_count = count
            classification = category

    return classification
