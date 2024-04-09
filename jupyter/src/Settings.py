import os

class Settings:
    # If set to False the Distances and Knn algorithm will use native's python lists (MUCH SLOWER)
    USE_NUMPY_ARRAY = False

    # Dimensions of the images, both for processing, reading
    # and converting from flatten to image formats
    N_ROWS = 32
    N_COLUMNS = 32

    # Run the preprocessing steps
    PREPROCESS_IMAGES = False

    # Number of threads / processes that will be used to speed up the execution
    N_THREADS = 4

    # Number of tests that will be used from x_test and y_test
    # (set to 0 if you want to use all tests)
    N_TESTS_USED = 100

    LOG_FILE_NAME = f"{N_ROWS}x{N_COLUMNS}_execution_log.csv"

    #####################################################
    # Internal Use
    # (don't change if you don't know what you are doing)
    WORKSPACE = os.path.curdir
    DATASET_DIR = os.path.join(WORKSPACE, "dataset")
    IMAGES_DIR = os.path.join(DATASET_DIR, "dataset")
    PROCESSED_IMAGES_PATH = os.path.join(IMAGES_DIR, "_processed")

    USE_SIMPLIFIED_KNN = True # unused

def print_all_settings():
    print("USE_NUMPY_ARRAY:", Settings.USE_NUMPY_ARRAY)
    print("N_ROWS:", Settings.N_ROWS)
    print("N_COLUMNS:", Settings.N_COLUMNS)
    print("PREPROCESS_IMAGES:", Settings.PREPROCESS_IMAGES)
    print("N_THREADS:", Settings.N_THREADS)
    print("N_TESTS_USED:", Settings.N_TESTS_USED)
    print("WORKSPACE:", Settings.WORKSPACE)
    print("DATASET_DIR:", Settings.DATASET_DIR)
    print("IMAGES_DIR:", Settings.IMAGES_DIR)
    print("PROCESSED_IMAGES_PATH:", Settings.PROCESSED_IMAGES_PATH)

GlobalSettings = Settings()