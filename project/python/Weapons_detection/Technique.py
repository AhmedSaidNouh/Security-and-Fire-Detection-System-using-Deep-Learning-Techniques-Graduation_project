import cv2
from Weapons_detection import CrossCheck
from Weapons_detection import Thresholdbasedondistance
from Weapons_detection import DavidLowesRatio
from matplotlib import pyplot as plt


def run_technique(img1, kp1, des1, img2):
    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()

    # find the keypoints an[pllld descriptors with SIFT
    kp2, des2 = sift.detectAndCompute(img2, None)



    # Define FLANN-based matching parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Perform nearest-neighbor matching between the query and scene descriptors
    matches1 = flann.knnMatch(des1, des2, k=2)
    matches2 = flann.knnMatch(des2, des1, k=2)


    # Run david lowes technique
    matchesFromDavidLowes1 = DavidLowesRatio.run_david_lowes(matches1)
    matchesFromDavidLowes2 = DavidLowesRatio.run_david_lowes(matches2)

    # Run CrossCheck technique
    matchesFromCrossCheck = CrossCheck.run_cross_check(matchesFromDavidLowes1, matchesFromDavidLowes2)

    # Run Threshold based on distance technique
    matchesFromThresholdBased = Thresholdbasedondistance.run_threshold_based_distance(matchesFromCrossCheck)

    score = (len(matchesFromThresholdBased) / min(len(kp1), len(kp2))) * 100
    matchesFromThresholdBased = sorted(matchesFromThresholdBased, key=lambda x: x.distance)


    return score, matchesFromThresholdBased,kp2,des2
