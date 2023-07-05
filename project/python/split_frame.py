import cv2

sec=0
count=1
def getFrame(path):
    global sec
    vidcap = cv2.VideoCapture(path)
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        path_image=f'../frames_offline/video1frame_{count}.jpg'
        cv2.imwrite(path_image,image)  # save frame as JPG file
        return hasFrames, path_image
    return hasFrames,0


def main(path):
    global sec
    global count

    frameRate = 0.5 #//it will capture image in each 0.5 second
    success,path_image = getFrame(path)
    if success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        return success,path_image
    else:

        return False,0