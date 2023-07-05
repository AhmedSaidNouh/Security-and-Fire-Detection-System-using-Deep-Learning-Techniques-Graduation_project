import cv2
import glob

import numpy
from Weapons_detection import segmentMatchedImage
from Weapons_detection import Technique
import  os

def detect_weapon(path):
    interested_segment = sScore = ''
    count = gun = -1
    gun_path = os.path.abspath(r"guns") + r"\*"
    kalashnikovs_path = os.path.abspath(r"kalashnikovs") + r"\*"
    gun_images = glob.glob(gun_path)
    kalashnikovs_images = glob.glob(kalashnikovs_path)
    images = gun_images + kalashnikovs_images
    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()

    pistolsData = {}
    pistolsIndex = 1
    for img in images:
        img1 = cv2.imread(img, cv2.COLOR_BGR2GRAY)

        # git key points for each img
        kp1, des1 = sift.detectAndCompute(img1, None)

        # add kp and des for each img to pistolsData Dictionary
        pistolsData[pistolsIndex] = {'kp': kp1, 'des': des1}
        pistolsIndex += 1

    interestedImg = cv2.imread(path, cv2.IMREAD_COLOR)
    print(path)

    if (interestedImg is None or interestedImg.dtype != numpy.uint8):
        print("image is empty or has incorrect depth (!=CV_8U)")

    else:
        count = 0
        matchedImg = {"img": None, "kp": None, "des": None, "score": 0, "matches": None}
        maxScore = -1
        kp2 = None
        des2 = None
        for index in range(len(images)):
            # first run the techniqueprint(img+'\n')

            score, matches, kp2, des2 = Technique.run_technique(cv2.imread(images[index], cv2.IMREAD_COLOR),
                                                                pistolsData[index + 1]['kp'],
                                                                pistolsData[index + 1]['des'], interestedImg)

            if (score > maxScore):
                matchedImg["img"] = cv2.imread(images[index], cv2.IMREAD_COLOR)
                matchedImg["kp"] = pistolsData[index + 1]['kp']
                matchedImg["des"] = pistolsData[index + 1]['des']
                matchedImg["score"] = score
                matchedImg["matches"] = matches
                maxScore = score

            if (score > 0.8):
                count += 1
            # print(str(index + 1) + "-----> Score : " + str(score) + " path ----->" + images[index])

        if len(matchedImg["matches"]) < 3:
            print("the number of key points", len(matchedImg["matches"]))

        else:
            interested_segment, sScore, count, gun = segmentMatchedImage.get_segment(matchedImg, interestedImg, kp2,
                                                                                     "count : " + str(count))

        print("count : " + str(count))
        return interested_segment, sScore, count, gun
