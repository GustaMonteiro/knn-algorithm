from src.Settings import *

from src.Distances import euclidean_distance

import time
import multiprocessing

def split_data_into_chunks(data, num_chunks):
    avg_chunk_size = len(data) // num_chunks
    chunks = [data[i:i+avg_chunk_size] for i in range(0, len(data), avg_chunk_size)]
    return chunks

def thread_classify_function(file_lock, results_lock, knn, test_data, total_correct, total_wrong, metric=euclidean_distance):
    total_start = time.time()
    log = ""
    count = 0
    correct = 0
    wrong = 0
    for point, right_answer in test_data:
        start = time.time()
        returned_answer = knn.classify(point, metric=metric)
        total = time.time() - start
        log += f"{right_answer},{returned_answer},{returned_answer == right_answer},{total}\n"
        count += 1
        if count % (int(0.2 * len(test_data))) == 0:
            print(f"{multiprocessing.current_process().name} processed {count}/{len(test_data)}")

        if returned_answer == right_answer:
            correct += 1
        else:
            wrong += 1
        
    with file_lock:
        with open(GlobalSettings.LOG_FILE_NAME, "a") as file:
            file.write(log)

    with results_lock:
        total_correct.value += correct
        total_wrong.value += wrong
            
    print(f"Total time for {multiprocessing.current_process().name}: {time.time() - total_start}s")