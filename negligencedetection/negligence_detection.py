import cv2
import numpy as np
import pyautogui
import imutils
import time
import os


class ScrShot:
    def __init__(self):
        self.basename = "screenshot"
        self.path = 'C:\\Users\\DDWU\\Desktop\\Documents\\My-Paper\\2021-negligence-detection\\screenshot\\images'
        self.scriptDir = os.path.dirname(os.path.abspath(__file__))

    def take_screenshot(self):
        pyautogui.screenshot(self.scriptDir + os.path.sep + "current_image.jpg")
        print("Current image created!")
        image1 = cv2.imread(self.scriptDir + os.path.sep + "current_image.jpg")
        cv2.imshow("Current Screenshot", imutils.resize(image1, width=512))

        time.sleep( float(1) )
        pyautogui.screenshot(self.scriptDir + os.path.sep + "next_image.jpg")
        image2 = cv2.imread(self.scriptDir + os.path.sep + "next_image.jpg")
        diff = cv2.subtract( image1, image2 )
        cv2.imwrite(self.scriptDir + os.path.sep + "diff.jpg", diff)
        cv2.imshow("Image Difference", imutils.resize(diff, width=512))
        cv2.waitKey(0)

# scrShot = ScrShot()
# scrShot.take_screenshot()

from keras.models import load_model
from skimage.transform import resize

print("Start CNN decision")
scriptDir = os.path.dirname(os.path.abspath(__file__))
image = cv2.imread(scriptDir + os.path.sep + "diff.jpg")
# image = cv2.imread("current_image.jpg")
img2 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
img3 = resize(img2, preserve_range=True, output_shape=(300, 512))

single_input = np.reshape( img3, (1,153600) )
#single_input = np.reshape( img3, (1, 300, 512, 1) )
single_input = single_input.astype('float64')
single_input = single_input / 255

#input_image = []
#input_image.append(img3)
#input_image = np.array(input_image)
#input_image = input_image.reshape( input_image.shape[0], 153600 )
#input_image = input_image.astype('float64')
#input_image = input_image / 255

model = load_model(scriptDir + os.path.sep + '../model/test_best.hdf5')
#predictions = np.argmax( model.predict(input_image), axis=-1 )
output = model.predict( single_input )
print(output)
prediction = np.argmax( output, axis= -1 )
if prediction == 0:
    print("Detection Result: Working ")
else:
    print("Detection Result: Game Playing")

