import cv2
from matplotlib import pyplot as plt


def get_segment(matchedImg, img1, kp1, count):
    img3 = cv2.drawMatches(
        matchedImg["img"], matchedImg["kp"],
        img1, kp1,
        matchedImg["matches"],
        flags=2, outImg=None)
    gun = 0
    if (matchedImg["score"] > 7):
        sScore = "They are similar\n" + "similarity: " + matchedImg["score"].__str__()
        gun = 1
    else:
        sScore = "They are not similar\n" + "similarity: " + matchedImg["score"].__str__()

    # Get the bounding box of the detected keypoints in the second image
    x_min = int(min([kp1[m.trainIdx].pt[0] for m in matchedImg["matches"]]))
    x_max = int(max([kp1[m.trainIdx].pt[0] for m in matchedImg["matches"]]))
    y_min = int(min([kp1[m.trainIdx].pt[1] for m in matchedImg["matches"]]))
    y_max = int(max([kp1[m.trainIdx].pt[1] for m in matchedImg["matches"]]))

    # Compute the width and height of the bounding box
    width = x_max - x_min
    height = y_max - y_min

    # Define the padding factor to increase the size of the bounding box
    padding_factor = 0.4

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
    new_x_max = min(new_x_max, img1.shape[1])
    new_y_max = min(new_y_max, img1.shape[0])

    # Extract the interested segment from the second image
    interested_segment = img1[new_y_min:new_y_max, new_x_min:new_x_max]

    return interested_segment, sScore, count, gun
