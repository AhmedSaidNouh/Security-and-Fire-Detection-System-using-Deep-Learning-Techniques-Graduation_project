import faceclassifier
import matplotlib.pyplot as plt
import matplotlib.pyplot as pl
import cv2
import classifications_models as cl
import  faceclassifier


def save(predict,roi_color,x):
  if predict[1]==1:
        #roi_color = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
    save = f'../split face/sss{x}.jpg'
    try:
        f = open(r"../files/face.txt", "w")
        write= save+','+predict[0]
        f.write(write)
        f.close()
        cv2.imwrite(save, roi_color)
    except:
        print("cant open face")


def draw_facebox(filename, result_list, i):
    # load the image
    data = cv2.imread(filename,cv2.COLOR_BGR2RGB)
    # plot the image
    plt.imshow(data)
    # get the context for drawing boxes
    ax = plt.gca()
    # plot each box
    #os.mkdir(r"D:\computer scince\GP\face final\New folder\save/" + str(i + 1))
    c = 0
    for result in result_list:

        # get coordinates
        x, y, width, height = result['box']
        roi_color = data[abs(y - 5):y + height + 10, abs(x - 5):x + width + 10]
        #classification
        predict= faceclassifier.predict_face(roi_color)
        print(predict)
        save(predict,roi_color,x)


        '''''
        ##classification
        if c == 0:
            cl.face_classification(roi_color,x)
            c=c+1
            '''''

       # pl.imshow(roi_color)
       # pl.show()


        # roi_color = cv2.cvtColor(roi_color, cv2.COLOR_BGR2RGB)
       # save = f"D:/computer scince/GP/face final/New folder/datasets/split face/5/{i + 1}_{x}.jpg"
        #cv2.imwrite(save, roi_color)

        # create the shape
        rect = plt.Rectangle((x - 15, y - 15), width + 25, height + 25, fill=False, color='green')
        # draw the box
        ax.add_patch(rect)
        # show the plot
   # plt.show()  # filename = 'test1.jpg' # filename is defined above, otherwise uncomment
    # load image from file



#-----------------------------------------------#


# display faces on the original image


