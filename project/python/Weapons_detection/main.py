import cv2
from matplotlib import pyplot as plt
import CrossCheck
import Thresholdbasedondistance
import DavidLowesRatio

pistol_img = cv2.imread('./sample data/1 (70).jpg', 0)

scale_percent = 200  # percent of original size
width = int(pistol_img.shape[1] * scale_percent / 100)
height = int(pistol_img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
pistol_img = cv2.resize(pistol_img, dim, interpolation=cv2.INTER_AREA)


man_carry_img = cv2.imread('./sample data/1 (17).jpg', 0)

sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints an[pllld descriptors with SIFT
kp_pistol_img, des_pistol_img = sift.detectAndCompute(pistol_img, None)
kp_man_carry_img, des_man_carry_img = sift.detectAndCompute(man_carry_img, None)

# create BFMatcher object
bf = cv2.BFMatcher()

# Match descriptors.
matches1 = bf.knnMatch(des_pistol_img, des_man_carry_img, 5)
matches2 = bf.knnMatch(des_man_carry_img, des_pistol_img,5 )

# Run david lowes technique
matchesFromDavidLowes1 = DavidLowesRatio.run_david_lowes(matches1)
matchesFromDavidLowes2 = DavidLowesRatio.run_david_lowes(matches2)

# Run CrossCheck technique
matchesFromCrossCheck = CrossCheck.run_cross_check(matchesFromDavidLowes1, matchesFromDavidLowes2)

# Run Threshold based on distance technique
matchesFromThresholdBased = Thresholdbasedondistance.run_threshold_based_distance(matchesFromCrossCheck)

score = (len(matchesFromThresholdBased) / min(len(kp_pistol_img), len(kp_man_carry_img))) * 100
matchesFromThresholdBased = sorted(matchesFromThresholdBased, key=lambda x: x.distance)
img3 = cv2.drawMatches(pistol_img, kp_pistol_img,
                       man_carry_img, kp_man_carry_img,
                       matchesFromThresholdBased,
                       flags=2, outImg=None)
if (score > 0.199):
    sScore = "They are similar\n" + "similarity: " + score.__str__()
else:
    sScore = "They are not similar\n" + "similarity: " + score.__str__()

print(sScore)
plt.imshow(img3), plt.title(sScore), plt.show()

print("Num of matches: ", len(matchesFromThresholdBased))

# plt.imshow(pistol_img)
# plt.show()
