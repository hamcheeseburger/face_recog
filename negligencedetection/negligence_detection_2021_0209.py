import datetime

import cv2
import numpy as np
import pyautogui
import time
from keras.models import load_model
from skimage.transform import resize
from keras.applications.vgg16 import VGG16

SAVE_PATH = "./negligencedetection/"
SEND_PATH = "./CaptureImage/"


class ScrShot:
    def __init__(self):
        self.basename = "screenshot"
        # self.path = 'C:\\Users\\DDWU\\Desktop\\Documents\\My-Paper\\2021-negligence-detection\\screenshot\\images'
        self.path = './result'

    def take_screenshot(self):
        current_image = pyautogui.screenshot()
        current_image.save(SAVE_PATH + "current_image.jpg")
        image1 = cv2.imread(SAVE_PATH + "current_image.jpg")
        #cv2.imshow("Current Screenshot", imutils.resize(image1, width=512))
        time.sleep( float(1) )

        next_image = pyautogui.screenshot()
        next_image.save(SAVE_PATH + "next_image.jpg")
        image2 = cv2.imread(SAVE_PATH + "next_image.jpg")
        #cv2.imshow("Next Screenshot", imutils.resize(image2, width=512))

        diff = cv2.subtract( image1, image2 )
        cv2.imwrite(SAVE_PATH + "diff.jpg", diff)
        print("Difference image created!")
        #cv2.imshow("Image Difference", imutils.resize(diff, width=512))
        #cv2.waitKey(0)

        return current_image


class Detection:
    def __init__(self):
        self.vgg16_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        self.model = load_model('.\\model\\TF_best.hdf5')

    def detect(self, work_id):
        print("detect")
        scrShot = ScrShot()
        save_image = scrShot.take_screenshot()
        diff_set = []

        print("Start CNN decision")

        image = cv2.imread(SAVE_PATH + "diff.jpg")
        single_input = resize(image, preserve_range=True, output_shape=(224, 224, 3)).astype('float64')
        single_input = single_input / 255
        diff_set.append(single_input)
        diff_set = np.array(diff_set)

        vgg_input = self.vgg16_model.predict( diff_set )
        vgg_input = vgg_input.reshape( vgg_input.shape[0], 7*7*512 )

        # output값이 1과 가까울 수록 GamePlaying
        # 현재는 around()로 하고 있기 때문에 0.5이상이면 gameplaying, 0.5이하이면 working으로 판별함
        output = self.model.predict(vgg_input)
        print(output)
        prediction = np.around(output)
        print(prediction)
        if prediction == 0:
            print("Detection Result: Working ")
        else:
            print("Detection Result: Game Playing")
            now = datetime.datetime.now()
            time_format = now.strftime("%Y%m%d_%H-%M-%S")

            save_image.save(SEND_PATH + str(work_id) + "_" + time_format + ".jpg")
        print("End of Distraction Detection..")

