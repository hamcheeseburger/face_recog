from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import cv2
from ui.realtimeui import RealTimeUi
import os
import simpleaudio as sa
from useless.realTime import uselessrealTimemain

# 푸쉬용 커밋
global face_recog


class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    scaled_size = QSize(640, 480)

    # parent = ExecuteRealTime 상속받음// QWidget
    def __init__(self, parent):
        super().__init__(parent)
        global face_recog
        face_recog = uselessrealTimemain.FaceRecog()

    def run(self):
        while True:
            frame = face_recog.get_frame()
            if frame is not None:
                # print(frame.shape)
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                           QImage.Format_RGB888)
                p = convertToQtFormat.scaled(self.scaled_size, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

    def scaled(self, scaled_size):
        self.scaled_size = scaled_size


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

        self.show()

    @pyqtSlot(QImage)
    def changePixmapHandler(self, image):
        # self.videoLabel.setPixmap(QPixmap.fromImage(image))
        if self.isCameraDisplayed is True:
            # 실시간이기 때문에 비디오 크기가 아님 웹캠 사이즈로 고정
            self.videoLabel.setFixedSize(640, 480)
            self.videoLabel.setPixmap(QPixmap.fromImage(image))
            self.adjustSize()

    # 시작버튼 눌렸을 때 실행되는 함수
    def start_recog(self):
        self.print_total_working.setText("근무시간 측정 중..")

        self.th1 = Thread(self)
        self.th1.changePixmap.connect(self.changePixmapHandler)
        # print(self.face_recog.known_face_names)
        # 프레임 추출하는 과정에 대해서만 쓰레드 시작 그 이후 코드는 쓰레드 핸들러에서 실행
        self.th1.start()

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
            self.isCameraDisplayed = False
            self.videoLabel.setText('화면 중지')
            self.videoLabel.setFixedSize(100, 30)
            # self.setFixedSize(400, 300)
            self.adjustSize()
        else:
            print('cam_start')
            self.isCameraDisplayed = True
            # 실시간이기 때문에 비디오 크기가 아님 웹캠 사이즈로 고정
            # self.videoLabel.setFixedSize(1280, 720)

    def sound_handler(self):
        # print("사운드 핸들러 동작")
        if self.alarmMute is False:
            self.alarmMute = True
        else:
            self.alarmMute = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # videoForm = QtWidgets.QWidget()
    # menuUi = ExecuteVideo(videoForm)
    # videoForm.show()
    obj = ExecuteRealTime('yhj')

    sys.exit(app.exec_())