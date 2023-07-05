import cv2
import numpy as np

# Load the first image
img1 = cv2.imread('./sample data/1 (70).jpg')

# Convert the first image to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Extract keypoints and descriptors for the first image
kp1, des1 = sift.detectAndCompute(gray1, None)

# Load the second image
img2 = cv2.imread('./sample data/1 (3).jpg')

# Convert the second image to grayscale
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Extract keypoints and descriptors for the second image
kp2, des2 = sift.detectAndCompute(gray2, None)

# Initialize FLANN matcher
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Match keypoints
matches = flann.knnMatch(des1, des2, k=2)

# Filter matches based on Lowe's ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

# Get the keypoints from the good matches
src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

# Compute homography matrix
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# Get the dimensions of the second image
h, w = img2.shape[:2]

# Define the corners of the second image
corners = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)

# Transform the corners of the second image using the homography matrix
transformed_corners = cv2.perspectiveTransform(corners, M)

# Find the minimum and maximum x and y coordinates of the transformed corners
min_x = int(np.min(transformed_corners[:, :, 0]))
max_x = int(np.max(transformed_corners[:, :, 0]))
min_y = int(np.min(transformed_corners[:, :, 1]))
max_y = int(np.max(transformed_corners[:, :, 1]))

# Extract the interested segment from the second image
interested_segment = img2[min_y:max_y, min_x:max_x]

# Show the interested segment
cv2.imshow('Interested Segment', interested_segment)
cv2.waitKey(0)
cv2.destroyAllWindows()
