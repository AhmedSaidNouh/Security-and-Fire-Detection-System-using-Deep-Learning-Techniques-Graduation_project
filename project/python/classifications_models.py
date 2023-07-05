import cv2
import matplotlib.pyplot as pl
def face_classification(roi_color,x):
    #roi_color = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
    save = f"D:\computer scince\GP\python\split face\sss{x}.jpg"
    f = open(r"D:\computer scince\GP\python\files\result of detect.txt", "w")
    write= save+','+'nouh'
    f.write(write)
    f.close()
    cv2.imwrite(save, roi_color)