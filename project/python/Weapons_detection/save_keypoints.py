import cv2
import os

# Set up SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# Path to directory containing images
image_dir = '../guns/'

# Path to output file for keypoints and descriptors
output_file = '../guns keypoints/keypoints.txt'

# Open output file for writing
with open(output_file, 'w') as f:
    # Loop through all images in directory
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            # Load image
            img = cv2.imread(os.path.join(image_dir, filename))

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Detect keypoints and compute descriptors
            kp, des = sift.detectAndCompute(gray, None)

            # Write keypoints and descriptors to file
            f.write(f'{filename}\n')
            f.write(f'{len(kp)}\n')
            for i in range(len(kp)):
                x, y = kp[i].pt
                size = kp[i].size
                angle = kp[i].angle
                response = kp[i].response
                octave = kp[i].octave
                f.write(f'{x} {y} {size} {angle} {response} {octave} ')
                for j in range(len(des[i])):
                    f.write(f'{des[i][j]} ')
                f.write('\n')