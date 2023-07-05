import main_class
from matplotlib import pyplot as plt
import cv2

interested_segment, sScore, count, gun = main_class.detect_weapon("../weapons frames/frames_video1frame_11.jpg")
if (gun == 1):
    print('there is weapon')
plt.imshow(cv2.cvtColor(interested_segment, cv2.COLOR_BGR2RGB)), plt.title(
    sScore + '\n' + count + '\n' + 'Interested Segment')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
