from videoUi import Ui_videoForm
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets
import cv2
import main
import os

# 수정된 videoUi.py를 이용함
# camera_On, camera Off 버튼을 camera 버튼으로 합침
# sound 버튼을 추가함


class Thread1(QThread):
    threadEvent = QtCore.pyqtSignal(int)

    def __init__(self, parent, face_recog):
        super().__init__()
        self.face_recog = face_recog
        self.main = parent
        self.frame_list = []
        if face_recog is None:
            print("쓰레드 init: face_recog is None")

    def run(self):
        # 동영상에서 프레임을 추출하는 과정
        self.frame_list = self.face_recog.get_specific_frame()

        # 프레임 추출이 완료되면 핸들러로 결과 전달(성공 : 1, 실패 : 0)
        if len(self.frame_list) > 0:
            self.threadEvent.emit(1)
        else:
            self.threadEvent.emit(0)


class ExecuteVideo(Ui_videoForm):
    def __init__(self, videoForm):
        Ui_videoForm.__init__(self)
        self.setupUi(videoForm)
        self.videoForm = videoForm

        self.stopFlag = False
        self.pauseFlag = False
        self.isCameraDisplayed = True

        # 얼굴인식 실행/중지 핸들러 연결
        self.btn_start.clicked.connect(self.start_recog)
        self.btn_end.clicked.connect(self.end_recog)

        # 비디오 화면 버튼 핸들러
        self.btn_camera.clicked.connect(self.cam_handler)
        # self.btn_cam_stop.clicked.connect(self.cam_stop)

    def threadEventHandler(self, result):  # 쓰레드핸들러(result값 전달 받는 부분)
        # result값이 1이면 정상적으로 프레임 추출이 완료된다는 뜻

        video = self.face_recog.get_video()
        fcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
        out = cv2.VideoWriter(
            "outVideo/output2.mp4", fcc, 3.0, (int(video.get(3)), int(video.get(4)))
        )

        start = time.time()
        print(start)
        print("result 변수 : " + str(result))
        if result == 1:
            self.print_total_working.setText("근무시간 측정중...")
            while True:
                frame = self.face_recog.do_recognition()
                # frame이 아니라 jpg byte를 받아와서 이미지 출력
                # bytes -> QPixmap으로 변환하는 것이 핵심
                # frame이 null이 아닐 경우에만 윈도우 상 출력
                if frame is None:
                    print("<<<<동영상이 종료됨>>>>")
                    break
                if frame is not None and self.isCameraDisplayed is True:
                    # print('frame is not None')
                    # 1) 기존 방법
                    # 매개 변수 jpg_bytes -> 비디오 파일 꺼지자 마자 프로그램 강제 종료
                    # 매개 변수 face_recog.get_jpg_bytes() -> 이상 없음
                    #
                    # self.my_bytes = QByteArray(self.face_recog.get_jpg_bytes())
                    # self.bytes_pixmap = QPixmap()
                    # ok = self.bytes_pixmap.loadFromData(self.my_bytes)
                    # assert ok
                    # self.videoLabel.setPixmap(self.bytes_pixmap)
                    # # 동영상 버전이기 때문에 웹캠과 다르게 크기지정
                    # self.videoLabel.setFixedSize(1280, 720)

                    # 2) 변경 방법
                    # print(frame.shape)
                    # self.scaled_size = QSize(640, 480)
                    # 윈도우 사이즈 조절에 따라 프레임이 늘어나게 하려면..??
                    self.scaled_size = QSize(1280, 720)
                    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                               QImage.Format_RGB888)
                    p = convertToQtFormat.scaled(self.scaled_size, Qt.KeepAspectRatio)
                    self.videoLabel.setPixmap(QPixmap.fromImage(p))
                    self.videoLabel.adjustSize()
                    self.videoForm.adjustSize()



                # 비디오쓰기
                out.write(frame)

                # 근무 신호등 교체
                self.isWorking = self.face_recog.working
                if self.isWorking is True:
                    self.change_traffic_light("./templates/Traffic_Lights_green.png")
                else:
                    self.change_traffic_light("./templates/Traffic_Lights_red.png")

                if self.stopFlag or self.face_recog.video_end:
                    break
                cv2.waitKey(5) & 0xFF
                self.face_recog.notifyIsPaused(self.pauseFlag)
        end = time.time()
        print(str(end) + ", " + str(end - start))
        cv2.destroyAllWindows()

        self.print_total_working.setText(self.face_recog.calculate_total())
        print("finish")
        # 종료버튼을 누르고 나서 신호등과 카메라 화면을 초기화
        self.isCameraDisplayed = False
        self.videoLabel.setText("근무 종료")
        self.videoLabel.setFixedSize(100, 30)
        self.change_traffic_light("./templates/Traffic_Lights_init.png")
        # 윈도우 창을 적절하게 자동으로 조정
        self.videoForm.adjustSize()

        out.release()

    # 시작버튼 눌렸을 때 실행되는 함수
    def start_recog(self):
        self.print_total_working.setText("프레임추출중.. 잠시만 기다려주세요")

        self.face_recog = main.FaceRecog()
        self.th = Thread1(self, self.face_recog)
        self.th.threadEvent.connect(self.threadEventHandler)
        self.face_recog.get_name("Hyeonji")  # 추후에 수정할 것
        print(self.face_recog.known_face_names)

        # 프레임 추출하는 과정에 대해서만 쓰레드 시작 그 이후 코드는 쓰레드 핸들러에서 실행
        self.th.start()

    def change_traffic_light(self, file_path):
        self.pixmap = QPixmap(self.scriptDir + os.path.sep + file_path)
        self.pixmap = self.pixmap.scaled(self.traffic_width, self.traffic_height)
        self.imgLabel.setPixmap(self.pixmap)

    def pause_recog(self):
        # 처음 일시중지버튼 눌렸을 때
        if not self.pauseFlag:
            self.pauseFlag = True
            self.btn_pause.setText("재시작")
        else:
            self.pauseFlag = False
            self.btn_pause.setText("일시중지")

    # 종료버튼 눌렸을 때 실행되는 함수
    def end_recog(self):
        self.stopFlag = True

    def cam_handler(self):
        if self.isCameraDisplayed is True:
            print('cam_stop')
            self.isCameraDisplayed = False
            self.videoLabel.setText('화면 중지')
            # self.videoLabel.resize(100, 30)
            self.videoLabel.setFixedSize(100, 30)
            # self.adjustSize()
            self.videoForm.adjustSize()
        else:
            print('cam_start')
            self.isCameraDisplayed = True
            # 실시간이기 때문에 비디오 크기가 아님 웹캠 사이즈로 고정
            # self.videoLabel.setFixedSize(1280, 720)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    videoForm = QtWidgets.QWidget()
    menuUi = ExecuteVideo(videoForm)
    videoForm.show()
    sys.exit(app.exec_())
