from knn_algorithm import classify

def main():
    all_points = [(1,2,'flower_a'),(2,1,'flower_a'),(3,3,'flower_b'),(5,4,'flower_b'),(3,1,'flower_a')]

    unknown_point = (7,9)

    print(classify(list_of_points=all_points, k=1, point=unknown_point))
    
if __name__ == '__main__':
    main()