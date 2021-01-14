import cv2
import pyautogui
import imutils
import time
import numpy as np
#from time import localtime, strftime, gmtime
#from datetime import datetime

class ScrShot:
    def __init__(self):
        self.basename = "screenshot"
        self.path = 'C:\\Users\\DDWU\\Desktop\\Documents\\My-Paper\\2021-negligence-detection\\screenshot\\images'

    def take_screenshot(self):
        #curTime = time.strftime("%Y%m%d-%H%M%S")
        #file_name = "_".join([self.basename, curTime])
        #file_name += ".png"
        #print(file_name + " created!")
        #image = pyautogui.screenshot()
        #image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        #cv2.imwrite(self.path + "\\" + file_name, image)

        pyautogui.screenshot("current_image.jpg")
        print("Current image created!")
        image1 = cv2.imread("current_image.jpg")
        cv2.imshow("Current Screenshot", imutils.resize(image1, width=1000))
        #cv2.imshow("Current Screenshot", image1)

        time.sleep( float(1) )
        pyautogui.screenshot("next_image.jpg")
        image2 = cv2.imread("next_image.jpg")
        diff = cv2.subtract( image1, image2 )
        cv2.imwrite("diff.jpg", diff)
        #cv2.imshow("Image Difference", imutils.resize(diff, width=1000))
        cv2.waitKey(0)

scrShot = ScrShot()
scrShot.take_screenshot()

from skimage.transform import resize

print("Start CNN decision")
image = cv2.imread("diff.jpg")
input_image = []
input = resize(image, preserve_range=True, output_shape=(224,224)).astype(int)
input_image.append(input)
input_image = np.array(input_image)
print("End!!")


