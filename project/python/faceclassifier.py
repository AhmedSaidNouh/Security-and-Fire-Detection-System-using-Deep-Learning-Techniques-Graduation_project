import numpy as np
import cv2
from keras.models import Model
from keras.layers import Input, GlobalAveragePooling2D, Dense, Dropout
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import decode_predictions


def predict_face(image):
    class_names = {0: 'pins_Adriana Lima', 1: 'pins_Alex Lawther', 2: 'pins_Alexandra Daddario', 3: 'pins_Alvaro Morte',
                   4: 'pins_Amanda Crew', 5: 'pins_Andy Samberg', 6: 'pins_Anne Hathaway', 7: 'pins_Anthony Mackie',
                   8: 'pins_Avril Lavigne', 9: 'pins_Ben Affleck', 10: 'pins_Bill Gates', 11: 'pins_Bobby Morley',
                   12: 'pins_Brenton Thwaites', 13: 'pins_Brian J. Smith', 14: 'pins_Brie Larson',
                   15: 'pins_Chris Evans',
                   16: 'pins_Chris Hemsworth', 17: 'pins_Chris Pratt', 18: 'pins_Christian Bale',
                   19: 'pins_Cristiano Ronaldo', 20: 'pins_Danielle Panabaker', 21: 'pins_Dominic Purcell',
                   22: 'pins_Dwayne Johnson', 23: 'pins_Eliza Taylor', 24: 'pins_Elizabeth Lail',
                   25: 'pins_Emilia Clarke',
                   26: 'pins_Emma Stone', 27: 'pins_Emma Watson', 28: 'pins_Gwyneth Paltrow', 29: 'pins_Henry Cavil',
                   30: 'pins_alycia dabnem carey', 31: 'pins_amber heard', 32: 'pins_barack obama',
                   33: 'pins_barbara palvin', 34: 'pins_camila mendes', 35: 'pins_elizabeth olsen',
                   36: 'pins_ellen page',
                   37: 'pins_elon musk', 38: 'pins_gal gadot', 39: 'pins_grant gustin'}
    criminals = ['pins_Adriana Lima', 'pins_Alex Lawther', 'pins_Alexandra Daddario',
                 'pins_Alvaro Morte', 'pins_Amanda Crew', 'pins_Andy Samberg',
                 'pins_Anne Hathaway', 'pins_Anthony Mackie', 'pins_Avril Lavigne',
                 'pins_Ben Affleck', 'pins_Bill Gates', 'pins_Bobby Morley',
                 'pins_Brenton Thwaites', 'pins_Brian J. Smith', 'pins_Brie Larson',
                 'pins_alycia dabnem carey', 'pins_amber heard', 'pins_barack obama',
                 'pins_barbara palvin', 'pins_camila mendes']
    my_vgg16 = my_vgg16_model()
    # Load the image
   #img = cv2.imread(path)

    # Resize the image to match the input shape of the VGG16 model
    img = cv2.resize(image, (100, 100))

    # Convert the image to a numpy array
    img = np.array(img)

    # Expand the dimensions of the image to match the input shape of the VGG16 model
    img = np.expand_dims(img, axis=0)

    # Scale the pixel values to be between 0 and 1
    img = img.astype('float32') / 255

    # Make a prediction using the VGG16 model
    predictions = my_vgg16.predict(img)

    predictions = np.array(predictions)

    max_index = np.argmax(predictions, axis=1)

    person_name = class_names[max_index[0]]
    criminal = 0
    if (criminals.__contains__(person_name)):
        criminal = 1
    return person_name, criminal
    # print(max_index)
    # # Print the predicted class probabilities
    # print(class_names[max_index[0]])


# Define your own VGG16 model with your modified layers
def my_vgg16_model():
    # Load the original VGG16 model architecture
    vgg16 = VGG16(weights=None, include_top=False, input_shape=(100, 100, 3))

    # Add your own layers
    main_model = vgg16.output
    main_model = GlobalAveragePooling2D()(main_model)
    main_model = Dense(1024, activation='relu')(main_model)
    main_model = Dense(1024, activation='relu')(main_model)
    main_model = Dense(512, activation='relu')(main_model)
    main_model = Dropout(0.5)(main_model)
    main_model = Dense(40, activation='softmax')(main_model)

    # Define a new model with your modified layers
    model = Model(inputs=vgg16.input, outputs=main_model)

    # Create an instance of your custom VGG16 model with ten classes
    # my_vgg16 = my_vgg16_model()

    # Load your own saved VGG16 model weights
    model.load_weights('./face_video_class_model.h5')
    return model