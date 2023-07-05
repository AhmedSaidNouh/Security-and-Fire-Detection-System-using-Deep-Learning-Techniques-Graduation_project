
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
def write(label):
	try:
		f = open(r"../files/detect_fire.txt", "w")

		f.write(label)
		f.close()
	except:
		print('cant fire')

def main(path):
	img = cv2.imread(path)
	# Convert the image to HSV color space
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Define the lower and upper thresholds for the color red
	lower_red = np.array([0, 50, 50])
	upper_red = np.array([20, 250, 250])

	# Create a mask for the red color range
	mask = cv2.inRange(hsv, lower_red, upper_red)

	# Count the number of pixels in the mask that are not zero
	num_red_pixels = cv2.countNonZero(mask)

	# Calculate the percentage of red pixels in the image
	total_pixels = img.shape[0] * img.shape[1]
	red_pixel_percentage = num_red_pixels / total_pixels

	# If the percentage of red pixels is above a certain threshold, there is fire in the image
	if red_pixel_percentage > 0.2:
		label = "fire"
	else:
		label = "no_fire"
	write(label)
