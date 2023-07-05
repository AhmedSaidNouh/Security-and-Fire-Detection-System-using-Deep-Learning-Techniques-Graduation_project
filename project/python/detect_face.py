from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
import split_face
import cv2
def main(path):
    filename = path #File location
    pixels = cv2.imread(filename,cv2.COLOR_BGR2RGB) # defined above, otherwise uncomment
    # detector is defined above, otherwise uncomment
    detector = MTCNN()
    # detect faces in the image
    faces = detector.detect_faces(pixels)
    if faces:
       print("detect_face")
       split_face.draw_facebox(filename, faces, 17)

    #print(faces)