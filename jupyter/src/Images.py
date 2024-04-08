import os
import shutil
import cv2
import matplotlib.pyplot as plt
import numpy as np

def remove_dir_recursively(dir_path):
    try:
        shutil.rmtree(dir_path)
        print("Directory", dir_path, "removed")
    except FileNotFoundError:
        print("Directory", dir_path, "does not exist")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(f"An error occurred: flatten_to_image{str(e)}")
    return

def get_all_images_path(dir_path, extension=None):
    allowed_extension = extension if extension is not None else "png"
    images_path = [
        os.path.join(dir_path, image) for image in os.listdir(dir_path)
        if os.path.splitext(image)[1] == '.'+allowed_extension
    ]
    return images_path

def create_dir(dir_path, delete_existent=False): 
    if delete_existent: 
        remove_dir_recursively(dir_path)
    os.mkdir(dir_path)
    return

def write_image(path, image):
    cv2.imwrite(
        path, 255*image, [cv2.IMWRITE_JPEG_QUALITY, 100]
    )
    return

def open_and_process_image(image_path, n_rows, n_columns):
    return cv2.resize(
        cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_RGB2GRAY)/255,
        (n_rows, n_columns)
    )

def preprocess_images_from_dir(
    *, dir_path=None, n_rows=None, n_columns=None, extension=None
):
    images_path = get_all_images_path(dir_path, extension)
    print("Found", len(images_path), "image(s)")

    if len(images_path) == 0:
        return
    
    PROCESSED_IMAGES_DIR = os.path.join(dir_path, "_processed")
    create_dir(PROCESSED_IMAGES_DIR, delete_existent=True)
    
    print("Writing images...")
    for path in images_path:
        image = open_and_process_image(path, n_rows, n_columns)

        write_image(
            os.path.join(PROCESSED_IMAGES_DIR, path.split("/")[-1]),
            image
        )

    print("Finished!")
    return

def flatten_to_image(flatten, n_rows, n_columns):
    return np.reshape(flatten, (n_rows, n_columns))

def plot_image(image):
    plt.imshow(image, cmap="gray")
    plt.show()
    return

def read_processed_image(image_path, n_rows, n_columns):
    return cv2.resize(
        cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)/255.0, (n_rows, n_columns)
    )


