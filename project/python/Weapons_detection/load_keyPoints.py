import numpy as np
import cv2


def read_kp_des_file(file_path):
    """
    Reads the keypoints and descriptors from a file and returns a dictionary of keypoints
    and descriptors for each image, where the keys are the image filenames and the values
    are tuples of keypoints and descriptors arrays.

    Args:
        file_path (str): The path to the keypoints and descriptors file.

    Returns:
        A dictionary of keypoints and descriptors for each image, where the keys are the
        image filenames and the values are tuples of keypoints and descriptors arrays.
    """
    keypoints = {}
    with open(file_path, 'r') as f:
        while True:
            # Read the filename
            filename = f.readline().strip()
            if not filename:
                break
            # Read the number of keypoints
            num_keypoints = int(f.readline().strip())
            # Read the keypoints and descriptors
            kp_list = []
            des_list = []
            for i in range(num_keypoints):
                kp_str = f.readline().strip().split()
                x, y, size, angle, response, octave = map(float, kp_str[:6])
                des = list(map(float, kp_str[6:]))
                kp = cv2.KeyPoint(x, y, size, angle, response, int(octave))
                kp_list.append(kp)
                des_list.append(des)
            des_array = np.array(des_list, dtype=np.float32)
            keypoints[filename] = (kp_list, des_array)
    return keypoints

# key=read_kp_des_file('../guns keypoints/keypoints.txt')
# print(key)