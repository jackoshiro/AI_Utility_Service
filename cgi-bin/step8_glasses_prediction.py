#!/usr/bin/env python
# make a prediction for a new image.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys
stderr = sys.stderr
sys.stderr = open('/dev/null', 'w')
import sys
import logging
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model

sys.stderr = stderr
print(flush=True)

# load and prepare the image
def load_image(filename):
        # load the image
        img = load_img(filename, target_size=(224, 224))
        # convert to array
        img = img_to_array(img)
        # reshape into a single sample with 3 channels
        img = img.reshape(1, 224, 224, 3)
        # center pixel data
        img = img.astype('float32')
        img = img - [123.68, 116.779, 103.939]
        return img

# load an image and predict the class
def run_example():
        # load the image
        img = load_image('/data/images/image.jpg')
        # load model
        model = load_model('/data/glasses_final_model.h5')
        # predict the class
        print('<html> <body> <h2>')
        result = model.predict(img)
        if result[0] < 0.49:
          print("There is %2d%% chance face with glasses." % ((1 - result[0])*100 ))
        elif result[0] > 0.51:
          print("There is %2d%% chance face without glasses." % ((result[0])*100 ))
        else:
          print("The image does not contain face, but I could be wrong. Please try again.")
        print('<hr> </h2> </body> </html>')

# entry point, run the example
run_example()
