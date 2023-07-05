import numpy as np
import cv2
from keras.models import Model
from keras.layers import Input, GlobalAveragePooling2D, Dense, Dropout ,Flatten
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import decode_predictions


def predict_weapons(image):
    class_names = {0: 'guns', 1: 'kalashnikovs'}

    my_vgg16 = my_vgg16_model()
    # Load the image

    # Resize the image to match the input shape of the VGG16 model
    img = cv2.resize(image, (500, 500))

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

    weapon_name = class_names[max_index[0]]

    return weapon_name


# Define your own VGG16 model with your modified layers
def my_vgg16_model():
    vgg_model = VGG16(weights='imagenet', include_top=False, input_shape=(500, 500, 3))

    for layer in vgg_model.layers[:7]:
        layer.trainable = False
    x = vgg_model.output
    x = Flatten()(x)  # Flatten dimensions to for use in FC layers
    x = Dense(512, activation='relu')(x)
    x = Dense(420, activation='relu')(x)
    x = Dense(256, activation='relu')(x)
    x = Dense(128, activation='relu')(x)
    x = Dense(64, activation='relu')(x)
    x = Dense(32, activation='relu')(x)
    x = Dense(16, activation='relu')(x)
    x = Dense(8, activation='relu')(x)
    x = Dropout(0.5)(x)  # Dropout layer to reduce overfitting
    x = Dense(2, activation='softmax')(x)
    transfer_model = Model(inputs=vgg_model.input, outputs=x)

    transfer_model.load_weights('./weapons_video_class_model.h5')

    return transfer_model


# print(predict_face('../kalashnikovs/1.png'))
