import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load the first and second images
# img1 = cv2.imread('./sample data/1 (70).jpg')
# img1 = cv2.imread('./sample data/High_power_Inglis_(6971784217).jpg')
# img1 = cv2.imread('./sample data/Air-Pistols.png')
img1 = cv2.imread('./sample data/71zzibHJzYL._AC_UF350,350_QL50_.jpg')
img2 = cv2.imread('./sample data/1 (132).jpg')

# Convert the images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Create a SIFT object
sift = cv2.xfeatures2d.SIFT_create()

# Find the keypoints and descriptors of the first and second images
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# Define FLANN-based matching parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

# Create FLANN matcher object
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Perform nearest-neighbor matching between the query and scene descriptors
matches = flann.knnMatch(des1, des2, k=2)

# Apply ratio test to select only good matches
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)



good_matches = sorted(good_matches, key=lambda x: x.distance)
img3 = cv2.drawMatches(img1, kp1,
                       img2, kp2,
                       good_matches,
                       flags=2, outImg=None)

plt.imshow(img3)
plt.show()

# Get the bounding box of the detected keypoints in the second image
x_min = int(min([kp2[m.trainIdx].pt[0] for m in good_matches]))
x_max = int(max([kp2[m.trainIdx].pt[0] for m in good_matches]))
y_min = int(min([kp2[m.trainIdx].pt[1] for m in good_matches]))
y_max = int(max([kp2[m.trainIdx].pt[1] for m in good_matches]))

# Compute the width and height of the bounding box
width = x_max - x_min
height = y_max - y_min

# Define the padding factor to increase the size of the bounding box
padding_factor = 0.2

# Compute the new dimensions of the bounding box after applying the padding factor
new_width = int(width * (1 + 2 * padding_factor))
new_height = int(height * (1 + 2 * padding_factor))

# Compute the new x and y coordinates of the bounding box
new_x_min = int(x_min - padding_factor * width)
new_x_max = int(x_max + padding_factor * width)
new_y_min = int(y_min - padding_factor * height)
new_y_max = int(y_max + padding_factor * height)

# Make sure the new coordinates are within the boundaries of the second image
new_x_min = max(new_x_min, 0)
new_y_min = max(new_y_min, 0)
new_x_max = min(new_x_max, img2.shape[1])
new_y_max = min(new_y_max, img2.shape[0])

# Extract the interested segment from the second image
interested_segment = img2[new_y_min:new_y_max, new_x_min:new_x_max]

# Show the interested segment
cv2.imshow('Interested Segment', interested_segment)
cv2.waitKey(0)
cv2.destroyAllWindows()
