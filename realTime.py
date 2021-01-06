import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets
import cv2
from realTime_ui import RealTimeUi
import os
import simpleaudio as sa
import realTime_main


class ExecuteRealTime(RealTimeUi):
    def __init__(self, id):
        RealTimeUi.__init__(self)

        self.user_name.setText("사용자 : " + id)
        self.user_id = id
        self.stopFlag = False
        self.pauseFlag = False
        self.isCameraDisplayed = True
        # self.fileRoute = ''
        self.workingAlarmFlag = False
        self.slackOffAlarmFlag = False
        self.alarmMute = False
        # simpleaudio
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        self.workingWav = sa.WaveObject.from_wave_file(scriptDir + os.path.sep + './sound/voice_working.wav')
        self.notWorkingWav = sa.WaveObject.from_wave_file(scriptDir + os.path.sep + './sound/voice_notWorking.wav')

        # 얼굴인식 실행/중지 핸들러 연결
        self.btn_start.clicked.connect(self.start_recog)
        self.btn_end.clicked.connect(self.end_recog)

        # 비디오 화면 버튼 핸들러
        self.btn_cam_start.clicked.connect(self.cam_handler)
        self.btn_sound_start.clicked.connect(self.sound_handler)
        # self.btn_select_route.clicked.connect(self.select_route)

        # 시작 버튼 미클릭시 버튼 클릭 못하게
        self.btn_cam_start.setDisabled(True)
        self.btn_sound_start.setDisabled(True)
        # self.btn_start.setDisabled(True)
        self.btn_end.setDisabled(True)

        self.show()



    # 시작버튼 눌렸을 때 실행되는 함수
    def start_recog(self):
        self.face_recog = realTime_main.FaceRecog()
        self.print_total_working.setText("근무시간 측정중..")
        self.btn_start.setDisabled(True)

        start = time.time()
        print(start)
        # 캠onoff, 소리onoff, 종료 버튼 활성화
        self.btn_cam_start.setDisabled(False)
        self.btn_sound_start.setDisabled(False)
        self.btn_end.setDisabled(False)
        while True:
            frame = self.face_recog.get_frame()
            # frame이 아니라 jpg byte를 받아와서 이미지 출력
            # bytes -> QPixmap으로 변환하는 것이 핵심
            # frame이 null이 아닐 경우에만 윈도우 상 출력
            if frame is None:
                print("frame is None")
                break
            if frame is not None and self.isCameraDisplayed is True:
                # print('frame is not None')
                # 매개 변수 jpg_bytes -> 비디오 파일 꺼지자 마자 프로그램 강제 종료
                # 매개 변수 face_recog.get_jpg_bytes() -> 이상 없음
                byte = self.face_recog.get_jpg_bytes()
                if byte is not None:
                    self.my_bytes = QByteArray(byte)
                    self.bytes_pixmap = QPixmap()
                    ok = self.bytes_pixmap.loadFromData(self.my_bytes)
                    assert ok
                    self.videoLabel.setPixmap(self.bytes_pixmap)
                    # self.videoLabel.setFixedSize(1280, 720)
                    self.videoLabel.setFixedSize(self.bytes_pixmap.size())
                    self.videoLabel.adjustSize()
                    self.adjustSize()

            # 근무 신호등 교체
            self.isWorking = self.face_recog.working
            if self.isWorking is True:
                self.change_traffic_light("./templates/Traffic_Lights_green.png")
                if self.workingAlarmFlag is False and self.alarmMute is False:
                    # print('working alarm!!')
                    play_obj = self.workingWav.play()
                    # play_obj.wait_done()
                    self.workingAlarmFlag = True
                    self.slackOffAlarmFlag = False
            else:
                self.change_traffic_light("./templates/Traffic_Lights_red.png")
                if self.slackOffAlarmFlag is False and self.alarmMute is False:
                    # print('slackOff alarm!!')
                    play_obj = self.notWorkingWav.play()
                    self.slackOffAlarmFlag = True
                    self.workingAlarmFlag = False

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
        self.videoLabel.setText("근무종료")
        self.videoLabel.setFixedSize(100, 30)
        # self.videoLabel.resize(self.videoLabel.width(), self.videoLabel.height())
        self.change_traffic_light("./templates/Traffic_Lights_init.png")
        # 윈도우 창을 적절하게 자동으로 조정
        self.setFixedSize(400, 200)
        self.btn_sound_start.setDisabled(True)
        self.btn_cam_start.setDisabled(True)
        self.btn_end.setDisabled(True)
        self.btn_start.setDisabled(False)
        self.adjustSize()
        # self.resize(400, 200)

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
            print('cam_off')
            self.btn_cam_start.setText('Camera On')
            self.isCameraDisplayed = False
            self.videoLabel.setText('화면 중지')
            self.videoLabel.setFixedSize(100, 30)
            self.setFixedSize(400, 200)
            self.adjustSize()
            # self.resize(400, 200)
        else:
            print('cam_start')
            self.btn_cam_start.setText('Camera Off')
            self.isCameraDisplayed = True
            # 실시간이기 때문에 비디오 크기가 아님 웹캠 사이즈로 고정
            # self.videoLabel.setFixedSize(1280, 720)

    def sound_handler(self):
        # print("사운드 핸들러 동작")
        if self.alarmMute is False:
            self.btn_sound_start.setText('Sound On')
            self.alarmMute = True
        else:
            self.btn_sound_start.setText('Sound Off')
            self.alarmMute = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # videoForm = QtWidgets.QWidget()
    # menuUi = ExecuteVideo(videoForm)
    # videoForm.show()
    obj = ExecuteRealTime('yhj')

    sys.exit(app.exec_())
