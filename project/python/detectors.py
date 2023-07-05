import os
import detect_face
import split_frame
import detect_fire
from Weapons_detection import main_class
import  cv2
import  matplotlib.pyplot as plt
import weaponclassifier

def writeFile(words):
    try:
      f = open(r"../files/guns.txt", "w")
      f.write(words)
    except:
        print("cant weapons")


sec=0
count=1
check=True
f= open(r"../files/location of videos.txt", "r")
video_path=f.readlines()

if int(video_path[0]) == 1:

    while check:
        split_frame.sec=sec
        split_frame.count=count

        check,path=split_frame.main(video_path[1])
        sec=split_frame.sec
        count=split_frame.count
        if check:
         detect_face.main(path)
         detect_fire.main(path)

         interested_segment ,sScore, w,gun=main_class.detect_weapon(path)
         if(gun==1):
             name_weapon = weaponclassifier.predict_weapons(interested_segment)
             writeFile(name_weapon)


else:
    print("realtime")
    vidPath=video_path[1]
    print(vidPath)
    for img in os.listdir(vidPath):
        print(img)

        image_path = os.path.join(vidPath, img)

        detect_face.main(image_path)
        detect_fire.main(image_path)

        interested_segment, sScore, w, gun = main_class.detect_weapon(image_path)
        if (gun == 1):
            name_weapon = weaponclassifier.predict_weapons(interested_segment)
            writeFile(name_weapon)
           # plt.show()
           # cv2.waitKey(0)



