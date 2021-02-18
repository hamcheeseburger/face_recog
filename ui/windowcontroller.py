from datetime import time

import cv2
from PyQt5 import QtWidgets
import os
import sys

from simpleaudio.shiny import *
from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QPixmap

from info.settingInfo import SettingInfo
from info.userinfo import UserInfo

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import simpleaudio as sa
# from ui.pygui_v2 import Ui_MainWindow
from ui.pygui_v3 import Ui_MainWindow
from realTimeCheck.realtimemain import FaceRecog


class WindowController(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)

        # Setting button click listener
        self.logoutBtn.clicked.connect(self.logout)
        self.realRecogStartBtn.clicked.connect(self.realRecogStart)
        self.realRecogEndBtn.clicked.connect(self.realRecogEnd)
        self.realRecogSoundBtn.clicked.connect(self.realRecogSound)
        self.videoCheckBtn.clicked.connect(self.videoCheck)
        self.videoRecogOpenBtn.clicked.connect(self.videoRecogOpen)
        self.videoRecogEndBtn.clicked.connect(self.videoRecogEnd)
        self.realRecogDisplayBtn.clicked.connect(self.realRecogDisplay)

        # Define Variables
        self.userInfo = UserInfo.instance()
        self.settingInfo = SettingInfo.instance()
        # self.cameraOffPixmap = QPixmap("./templates/CAM_OFF.png")
        # self.cameraOffPixmap = self.cameraOffPixmap.scaledToWidth(330)

        # 심플오디오
        self.scriptDir = os.path.dirname(os.path.abspath(__file__))
        self.workingWav = sa.WaveObject.from_wave_file(self.scriptDir + os.path.sep + './sound/voice_working.wav')
        self.notWorkingWav = sa.WaveObject.from_wave_file(self.scriptDir + os.path.sep + './sound/voice_notWorking.wav')

        # 사용자 정보 적용
        self.userNameLabel.setText(self.userNameLabel.text() + "\t" + self.userInfo.name)
        self.userIdLabel.setText(self.userIdLabel.text() + "\t" + self.userInfo.id)
        self.imagePixmap = QPixmap()
        self.imagePixmap.loadFromData(self.userInfo.image)
        self.imagePixmap = self.imagePixmap.scaledToWidth(120)
        self.userImgLabel.setPixmap(self.imagePixmap)

        # 세팅 정보 적용
        self.stgDecLabel.setText(self.stgDecLabel.text() + "\t" + str(self.settingInfo.DETEC_SEC) + "초")
        self.stgLvlLabel.setText(self.stgLvlLabel.text() + "\t" + str(self.settingInfo.RECOV_LV) + "단계")
        self.stgNodLabel.setText(self.stgNodLabel.text() + "\t" + str(self.settingInfo.NOD_SEC) + "초")

        self.workListView.append("날짜시각\t\t근무타입\t\t근무시간")

        # 비활성화 버튼 초기화
        self.btn_init()
        self.show()

    def btn_init(self):
        self.realRecogEndBtn.setDisabled(True)
        self.realRecogSoundBtn.setDisabled(True)
        self.realRecogDisplayBtn.setDisabled(True)
        self.videoRecogEndBtn.setDisabled(True)

    def realRecog_init_variable(self):
        self.stopFlag = False
        self.pauseFlag = False
        self.isCameraDisplayed = True
        self.workingAlarmFlag = False
        self.slackOffAlarmFlag = False
        self.alarmMute = False

    def logout(self):
        print("logoutBtn clicked")

    def realRecogStart(self):
        print("realRecogStartBtn clicked")
        self.realRecog_init_variable()
        self.face_recog = FaceRecog.instance()
        # 얼굴 인식 시작할 때 마다 변수 초기화 필요...
        self.realRecogAnnounceLabel.setText("..근무시간 측정중..")
        self.realRecogStartBtn.setDisabled(True)
        self.change_traffic_light("../templates/Traffic_Lights_red.png")

        # 카메라onoff, 소리onoff, 종료 버튼 활성화
        self.realRecogEndBtn.setDisabled(False)
        self.realRecogSoundBtn.setDisabled(False)
        self.realRecogDisplayBtn.setDisabled(False)

        while True:
            frame = self.face_recog.get_frame()
            #     # frame이 아니라 jpg byte를 받아와서 이미지 출력
            #     # bytes -> QPixmap으로 변환하는 것이 핵심
            #     # frame이 null이 아닐 경우에만 윈도우 상 출력
            if frame is None:
                print("frame is None")
                break
            if frame is not None and self.isCameraDisplayed is True:
                # print('frame is not None')
                byte = self.face_recog.get_jpg_bytes()
                if byte is not None:
                    my_bytes = QByteArray(byte)
                    bytes_pixmap = QPixmap()
                    ok = bytes_pixmap.loadFromData(my_bytes)
                    assert ok
                    bytes_pixmap = bytes_pixmap.scaledToWidth(330)
                    self.realRecogCamLabel.setPixmap(bytes_pixmap)
            # 근무 신호등 교체
            self.isWorking = self.face_recog.working
            self.isRealSlackOff = self.face_recog.isRealSlackOff
            if self.isWorking is True:
                self.change_traffic_light("../templates/Traffic_Lights_green.png")
                if self.workingAlarmFlag is False and self.alarmMute is False:
                    # print('working alarm!!')
                    play_obj = self.workingWav.play()
                    #             # play_obj.wait_done()
                    self.workingAlarmFlag = True
                    self.slackOffAlarmFlag = False
            elif self.isRealSlackOff is True:
                self.change_traffic_light("../templates/Traffic_Lights_red.png")
                if self.slackOffAlarmFlag is False and self.alarmMute is False:
                    # print('slackOff alarm!!')
                    play_obj = self.notWorkingWav.play()
                    self.slackOffAlarmFlag = True
                    self.workingAlarmFlag = False
            #
            if self.stopFlag or self.face_recog.video_end:
                break
            cv2.waitKey(5) & 0xFF
            self.face_recog.notifyIsPaused(self.pauseFlag)

        self.realRecogAnnounceLabel.setText(self.face_recog.calculate_total())
        # 종료버튼을 누르고 나서 신호등과 카메라 화면을 초기화
        self.isCameraDisplayed = False
        self.change_traffic_light("../templates/Traffic_Lights_init.png")

        self.realRecogCamLabel.setPixmap(self.camPixmap)
        # 버튼 초기화
        self.realRecogSoundBtn.setDisabled(True)
        self.realRecogEndBtn.setDisabled(True)
        self.realRecogDisplayBtn.setDisabled(True)
        self.realRecogStartBtn.setDisabled(False)

    def change_traffic_light(self, file_path):
        self.pixmap = QPixmap(self.scriptDir + os.path.sep + file_path)
        self.pixmap = self.pixmap.scaled(self.traffic_width, self.traffic_height)
        self.realRecogSignalLabel.setPixmap(self.pixmap)

    def realRecogEnd(self):
        print("realRecogEndBtn clicked")
        self.stopFlag = True
        if self.face_recog is not None:
            self.face_recog.close()

    def realRecogSound(self):
        print("realRecogSoundBtn clicked")
        if self.alarmMute is False:
            self.alarmMute = True
            self.realRecogSoundBtn.setText("음성안내 켜기")
        else:
            self.alarmMute = False
            self.realRecogSoundBtn.setText("음성안내 끄기")

    def realRecogDisplay(self):
        if self.isCameraDisplayed is True:
            print('cam_off')
            self.realRecogDisplayBtn.setText('카메라켜기')
            self.isCameraDisplayed = False
            self.realRecogCamLabel.setPixmap(self.camPixmap)
        else:
            print('cam_start')
            self.realRecogDisplayBtn.setText('카메라끄기')
            self.isCameraDisplayed = True

    def videoCheck(self):
        print("videoCheckBtn clicked")

    def videoRecogOpen(self):
        print("videoRecogOpenBtn clicked")

    def videoRecogEnd(self):
        print("videoRecogEndBtn clicked")

    def addWorkToworkListView(self, workString):
        self.workListView.append(workString)

    def closeEvent(self, event):
        print("closed")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    pygui = WindowController()
    pygui.addWorkToworkListView("추가한 글")
    sys.exit(app.exec_())
