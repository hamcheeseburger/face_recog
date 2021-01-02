# camera.py

import cv2


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        # Grab a single frame of video
        # self.video.read()은 cv2.VideoCapture(0).read() 과 같음!
        ret, frame = self.video.read()
        return frame


# 어떤 스크립트 파일이든 파이썬 인터프리터가 최초로 실행한 스크립트 파일의 __name__에는
# '__main__'이 들어갑니다.
# 이는 프로그램의 시작점(entry point)이라는 뜻입니다.

# 모듈로 가져올 땐 실행이 안되는 것 같음
# python camera.py 할 때 실행되는 쾨드
if __name__ == "__main__":
    cam = VideoCamera()
    while True:
        frame = cam.get_frame()

        # 읽어 온 프레임 출력
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    print("finish")
