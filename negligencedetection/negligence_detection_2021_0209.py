import datetime

import cv2
import numpy as np
import pyautogui
import time

import requests
from keras.models import load_model
from skimage.transform import resize
from keras.applications.vgg16 import VGG16
from info.userinfo import UserInfo
SAVE_PATH = "./negligencedetection/"
SEND_PATH = "./CaptureImage/"


class ScrShot:
    def __init__(self):
        self.basename = "screenshot"
        self.path = 'C:\\Users\\DDWU\\Desktop\\Documents\\My-Paper\\2021-negligence-detection\\screenshot\\images'
        # self.path = './result'

    def take_screenshot(self):
        current_img = pyautogui.screenshot()
        current_img.save(SAVE_PATH + "current_image.jpg")

        image1 = cv2.imread(SAVE_PATH + "current_image.jpg")
        # cv2.imshow("Current Screenshot", imutils.resize(image1, width=512))
        time.sleep(float(1))
        next_img = pyautogui.screenshot()
        next_img.save(SAVE_PATH + "next_image.jpg")
        image2 = cv2.imread(SAVE_PATH + "next_image.jpg")
        # cv2.imshow("Next Screenshot", imutils.resize(image2, width=512))

        diff = cv2.subtract(image1, image2)
        cv2.imwrite(SAVE_PATH + "diff.jpg", diff)
        print("Difference image created!")
        # cv2.imshow("Image Difference", imutils.resize(diff, width=512))
        # cv2.waitKey(0)
        return current_img

class Detection:
    def __init__(self):
        self.vgg16_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        self.model = load_model('.\\model\\TF_best.hdf5')

    def detect(self, work_id):
        scrShot = ScrShot()
        send_image = scrShot.take_screenshot()
        diff_set = []

        print("Start CNN decision")

        image = cv2.imread(SAVE_PATH + "diff.jpg")
        single_input = resize(image, preserve_range=True, output_shape=(224, 224, 3)).astype('float64')
        single_input = single_input / 255
        diff_set.append(single_input)
        diff_set = np.array(diff_set)

        # vgg16_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        vgg_input = self.vgg16_model.predict(diff_set)
        vgg_input = vgg_input.reshape(vgg_input.shape[0], 7 * 7 * 512)

        # model = load_model('.\\model\\TF_best.hdf5')
        output = self.model.predict(vgg_input)
        print(output)
        prediction = np.around(output)
        print(prediction)

        if prediction == 0:
            print("Detection Result: Working ")
            work = True
        else:
            print("Detection Result: Game Playing")
            now = datetime.datetime.now()
            time_format = now.strftime("%Y%m%d_%H-%M-%S")

            send_image.save(SEND_PATH + str(work_id) + "_" + time_format + ".jpg")
            work = False
        print("End of Distraction Detection..")

        # # 서버로 이미지를 전송하는 부분
        # url = "http://localhost:8090/awsDBproject/sending/captureImage"
        # file = {
        #     'image': open(SAVE_PATH + 'current_image.jpg', 'rb')
        # }
        # data = {
        #     'id': UserInfo.instance().id,
        #     'work': work
        # }
        # requests.post(url, files=file, data=data)