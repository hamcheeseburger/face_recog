"""video
기능설명:
     동영상으로 근무시간을 측정할 때 사용되는 UI의 기능부분
개발자:
    송재임, 유현지
개발일시:
    2021.01.05.20.53.00
버전:
    0.0.2
"""
import datetime
from ui.videoui import VideoUi
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtGui
import cv2
from videoCheck.videomain2 import FaceRecog
import os
import simpleaudio as sa
from login.userinfo import UserInfo
# ui기능

# 진행과정 : 시작버튼 클릭 -> 동영상 프레임추출 -> 프레임별로 얼굴인식 후 근무시간 측정
# 시작버튼 클릭시,ExecuteVideo.start_recog() 함수 실행
# 프레임추출부분, Thread1.run() 함수에 구현
# 그 외 부분, ExecuteVideo.threadEventHandler()에 구현


class Thread1(QThread):
    threadEvent = QtCore.pyqtSignal(int)

    def __init__(self, parent, face_recog):
        super().__init__()
        self.face_recog = face_recog
        self.main = parent
        if face_recog is None:
            print("쓰레드 init: face_recog is None")

    def run(self):
        # 동영상에서 프레임을 추출하는 과정
        frame_list = []
        while True:
            frame, percent = self.face_recog.get_specific_frame()
            if frame is None:
                break
            else:
                frame_list.append(frame)
                self.threadEvent.emit(percent)

        # 프레임 추출이 완료되면 핸들러로 결과 전달(성공 : 1, 실패 : 0)
        if len(frame_list) > 0:
            self.face_recog.set_frame_list(frame_list)
            self.threadEvent.emit(200)
        else:
            self.threadEvent.emit(None)


class ExecuteVideo(VideoUi):
    def __init__(self, id):
        VideoUi.__init__(self)

        self.userInfo = UserInfo.instance()
        self.user_name.setText("사용자 : " + self.userInfo.name)
        self.user_id = id
        self.fileRoute = ''
        self.init_variable()

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
        self.btn_select_route.clicked.connect(self.select_route)

        # 동영상 선택 안했을 시에 버튼 클릭 못하게
        self.btn_cam_start.setDisabled(True)
        self.btn_sound_start.setDisabled(True)
        self.btn_start.setDisabled(True)
        self.btn_end.setDisabled(True)

        self.show()

    def init_variable(self):
        self.stopFlag = False
        self.pauseFlag = False
        self.isCameraDisplayed = True
        self.workingAlarmFlag = False
        self.slackOffAlarmFlag = False
        self.alarmMute = True

    def threadEventHandler(self, result):  # 쓰레드핸들러(result값 전달 받는 부분)
        # result값이 1이면 정상적으로 프레임 추출이 완료된다는 뜻
        if result == 200:
            self.do_work()
        elif result is not None:
            self.print_total_working.setText("프레임추출중.. 잠시만 기다려주세요. " + str(result) + "% 진행중")
        else:
            return

    def do_work(self):
        video = self.face_recog.get_video()
        fcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
        now = datetime.datetime.now()
        nowDate = str(now.strftime('%Y%m%d_%H-%M-%S'))
        print(nowDate)
        out = cv2.VideoWriter(
            "outVideo/" + self.user_id + "_" + nowDate + ".mp4", fcc, 3.0, (int(video.get(3)), int(video.get(4)))
        )

        self.print_total_working.setText("근무시간 측정중...")
        # 캠onoff, 소리onoff, 종료 버튼 활성화
        self.btn_cam_start.setDisabled(False)
        self.btn_sound_start.setDisabled(False)
        self.btn_end.setDisabled(False)
        while True:
            frame = self.face_recog.do_recognition()
            # frame이 아니라 jpg byte를 받아와서 이미지 출력
            # bytes -> QPixmap으로 변환하는 것이 핵심
            # frame이 null이 아닐 경우에만 윈도우 상 출력
            if frame is None:
                print("<<<<동영상이 종료됨>>>>")
                break
            elif frame is not None and self.isCameraDisplayed is True:
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
                    self.videoLabel.setFixedSize(1280, 720)
                    self.adjustSize()

            # 비디오쓰기
            out.write(frame)

            # 근무 신호등 교체
            self.isWorking = self.face_recog.working
            if self.isWorking is True:
                self.change_traffic_light("../templates/Traffic_Lights_green.png")
                if self.workingAlarmFlag is False and self.alarmMute is False:
                    # print('working alarm!!')
                    play_obj = self.workingWav.play()
                    # play_obj.wait_done()
                    self.workingAlarmFlag = True
                    self.slackOffAlarmFlag = False
            else:
                self.change_traffic_light("../templates/Traffic_Lights_red.png")
                if self.slackOffAlarmFlag is False and self.alarmMute is False:
                    # print('slackOff alarm!!')
                    play_obj = self.notWorkingWav.play()
                    self.slackOffAlarmFlag = True
                    self.workingAlarmFlag = False

            if self.stopFlag or self.face_recog.video_end:
                break
            cv2.waitKey(5) & 0xFF
            self.face_recog.notifyIsPaused(self.pauseFlag)

        cv2.destroyAllWindows()

        self.print_total_working.setText(self.face_recog.calculate_total())
        print("finish")
        # 종료버튼을 누르고 나서 신호등과 카메라 화면을 초기화
        self.isCameraDisplayed = False
        self.videoLabel.setText(" ")
        self.videoLabel.setFixedSize(100, 30)
        # self.videoLabel.resize(self.videoLabel.width(), self.videoLabel.height())
        self.change_traffic_light("../templates/Traffic_Lights_init.png")
        # 윈도우 창을 적절하게 자동으로 조정
        # self.setFixedSize(400, 300)
        self.btn_sound_start.setDisabled(True)
        self.btn_cam_start.setDisabled(True)
        self.btn_end.setDisabled(True)
        self.btn_start.setDisabled(False)
        self.adjustSize()
        out.release()

    # 시작버튼 눌렸을 때 실행되는 함수
    def start_recog(self):
        self.init_variable()
        self.print_total_working.setText("프레임추출중.. 잠시만 기다려주세요")
        self.btn_start.setDisabled(True)

        self.face_recog = FaceRecog.instance()
        self.face_recog.set_file_route(self.fileRoute)

        self.th = Thread1(self, self.face_recog)
        self.th.threadEvent.connect(self.threadEventHandler)

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
            self.btn_cam_start.setText('Camera On')
            self.isCameraDisplayed = False
            self.videoLabel.setText('화면 중지')
            self.videoLabel.setFixedSize(100, 30)
            # self.setFixedSize(400, 300)
            self.adjustSize()
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

    def select_route(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter(
            self.tr("Data Files (*.mp4 *.avi *.mov *mkv);; Images (*.png *.xpm *.jpg *.gif);; All Files(*.*)"))
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            filesRoute = dialog.selectedFiles()
            self.fileRoute = filesRoute[0]
            if self.fileRoute != '':
                self.routeLabel.setText(self.fileRoute)
                # 시작버튼 활성화
                self.btn_start.setDisabled(False)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.end_recog()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # videoForm = QtWidgets.QWidget()
    # menuUi = ExecuteVideo(videoForm)
    # videoForm.show()
    obj = ExecuteVideo('yhj')

    sys.exit(app.exec_())
