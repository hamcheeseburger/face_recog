import datetime
import subprocess
import threading
from threading import Timer
import cv2
import requests
import os
import sys
import face_recognition_models
from face_recognition_models import models

from PyQt5.QtCore import QByteArray, QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtWidgets

from info.loginfo import LogInfo
from info.settingInfo import SettingInfo
from info.urlInfo import UrlInfo
from info.userinfo import UserInfo
from info.workinfo import ArrayWorkInfo
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import simpleaudio as sa
from ui.pygui_v5 import Ui_MainWindow
from realTimeCheck import realtimemain
from videoCheck import videomain2
from python import server


class WindowController(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        self.face_recog = None
        self.video_face_recog = None
        print(face_recognition_models.__email__)
        threading.Thread(target=self.setValiable).start()

        self.workStart = False

        # Setting button click listener
        self.logoutBtn.clicked.connect(self.logout)
        self.realRecogStartBtn.clicked.connect(self.realRecogStart)
        self.realRecogEndBtn.clicked.connect(self.realRecogEnd)
        self.realRecogSoundBtn.clicked.connect(self.realRecogSound)
        self.videoCheckBtn.clicked.connect(self.videoCheck)
        self.videoRecogOpenBtn.clicked.connect(self.videoRecogOpen)
        self.videoRecogStartBtn.clicked.connect(self.videoRecogStart)
        self.realRecogDisplayBtn.clicked.connect(self.realRecogDisplay)

        # Define Variables
        self.userInfo = UserInfo.instance()
        self.settingInfo = SettingInfo.instance()
        self.arrayWorkInfo = ArrayWorkInfo.instance()
        self.logInfo = LogInfo.instance()
        self.isVideoCheckCilcked = False

        # 심플오디오
        self.scriptDir = os.path.dirname(os.path.abspath(__file__))
        self.workingWav = sa.WaveObject.from_wave_file(self.scriptDir + os.path.sep + './sound/voice_working.wav')
        self.notWorkingWav = sa.WaveObject.from_wave_file(self.scriptDir + os.path.sep + './sound/voice_notWorking.wav')

        # 사용자 정보 적용
        self.userNameLabel.setText(self.userNameLabel.text() + "\t" + self.userInfo.name)
        self.userIdLabel.setText(self.userIdLabel.text() + "\t" + self.userInfo.id)
        self.userIPLabel.setText(self.userIPLabel.text() + "\t" + self.userInfo.ip)
        self.imagePixmap = QPixmap()
        self.imagePixmap.loadFromData(self.userInfo.image)
        self.imagePixmap = self.imagePixmap.scaledToWidth(120)
        self.userImgLabel.setPixmap(self.imagePixmap)
        self.workTimeLabel.setText(str(datetime.timedelta(seconds=self.userInfo.work_time)).split(".")[0])

        # 세팅 정보 적용
        self.stgDecLabel.setText(self.stgDecLabel.text() + "\t" + str(self.settingInfo.DETEC_SEC) + "초")
        self.stgLvlLabel.setText(self.stgLvlLabel.text() + "\t" + str(self.settingInfo.RECOV_LV) + "단계")
        self.stgNodLabel.setText(self.stgNodLabel.text() + "\t" + str(self.settingInfo.NOD_SEC) + "초")

        self.workListView.append("날짜시각\t\t근무타입\t\t근무시간")

        # 화면 초기화 작업
        self.refreshView()
        self.showDateTime() # 현재시간 출력
        self.btn_init() # 버튼 비활성화

        self.show()

    def setValiable(self):
        self.face_recog = realtimemain.FaceRecog.instance()
        self.video_face_recog = videomain2.FaceRecog.instance()

    def showDateTime(self):
        now = datetime.datetime.now()
        time_format = now.strftime("%Y년 %m월 %d일 %H시 %M분".encode('unicode-escape').decode())
        time_format = time_format.encode().decode('unicode-escape')
        self.dateLabel.setText(time_format)

        self.date_timer = Timer(30, self.showDateTime)
        self.date_timer.start()

    def btn_init(self):
        self.realRecogEndBtn.setDisabled(True)
        self.realRecogSoundBtn.setDisabled(True)
        self.realRecogDisplayBtn.setDisabled(True)
        self.videoRecogStartBtn.setDisabled(True)
        self.videoCheckBtn.setDisabled(True)

    def init_variable(self):
        self.workStart = True
        self.stopFlag = False
        self.isCameraDisplayed = True
        self.workingAlarmFlag = False
        self.slackOffAlarmFlag = False
        self.alarmMute = False

    def logout(self):
        print("logoutBtn clicked")
        self.close()

    def realRecogStart(self):
        print("realRecogStartBtn clicked")
        if self.face_recog is None:
            print("face_recog is None")
            return

        self.init_variable()

        # 동영상 인식 불가능 하게 버튼 변경
        self.videoRecogOpenBtn.setDisabled(True)

        # 얼굴 인식 시작할 때 마다 변수 초기화 필요...
        self.face_recog.reset()

        self.realRecogAnnounceLabel.setText("..근무시간 측정중..")
        self.realRecogStartBtn.setDisabled(True)
        self.change_traffic_light("../templates/Traffic_Lights_red.png")

        # 카메라onoff, 소리onoff, 종료 버튼 활성화
        self.realRecogEndBtn.setDisabled(False)
        self.realRecogSoundBtn.setDisabled(False)
        self.realRecogDisplayBtn.setDisabled(False)

        while True:
            frame = self.face_recog.get_frame()

            if frame is None:
                print("frame is None")
                break
            elif self.isCameraDisplayed:
                byte = self.face_recog.get_jpg_bytes()
                if byte is not None:
                    my_bytes = QByteArray(byte)
                    bytes_pixmap = QPixmap()
                    ok = bytes_pixmap.loadFromData(my_bytes)
                    assert ok
                    bytes_pixmap = bytes_pixmap.scaledToWidth(330)
                    self.realRecogCamLabel.setPixmap(bytes_pixmap)

            if self.face_recog.working:
                self.change_traffic_light("../templates/Traffic_Lights_green.png")
                if self.workingAlarmFlag is False and self.alarmMute is False:
                    self.workingWav.play()
                    self.workingAlarmFlag = True
                    self.slackOffAlarmFlag = False

            elif self.face_recog.isRealSlackOff is True:
                self.change_traffic_light("../templates/Traffic_Lights_red.png")
                if self.slackOffAlarmFlag is False and self.alarmMute is False:
                    self.notWorkingWav.play()
                    self.slackOffAlarmFlag = True
                    self.workingAlarmFlag = False

            if self.stopFlag or self.face_recog.video_end:
                break
            #     아래 코드는 지우면 안됨
            cv2.waitKey(5) & 0xFF

        self.realRecogAnnounceLabel.setText(self.face_recog.calculate_total())
        # 종료버튼을 누르고 나서 신호등과 카메라 화면을 초기화
        self.isCameraDisplayed = False
        self.change_traffic_light("../templates/Traffic_Lights_init.png")
        self.realRecogCamLabel.setPixmap(self.camPixmap)

        # 작업 종료
        self.workStart = False
        # 버튼 초기화
        self.realRecogSoundBtn.setDisabled(True)
        self.realRecogEndBtn.setDisabled(True)
        self.realRecogDisplayBtn.setDisabled(True)
        self.realRecogStartBtn.setDisabled(False)
        self.videoRecogOpenBtn.setDisabled(False)

        # 화면 refresh
        self.refreshView()

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
        if self.isCameraDisplayed:
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
        fileName = './vca/vca4.jar'
        # start ./Duplicate/VideoCombineAnalysis.jar [videoPath] 의 명령어가 실행 되는 것
        subprocess.run(["start", fileName, self.videoRecogFileRoute], shell=True)
        # 중복 클릭 방지
        if self.isVideoCheckCilcked is False:
            self.isVideoCheckCilcked = True
            recevie_th = ReceiveThread(self)
            recevie_th.threadEvent.connect(self.receiveThreadHandler)
            recevie_th.start()

    def receiveThreadHandler(self, result):
        print(result)
        self.videoRecogStartBtn.setDisabled(True)
        if result == 1:
            print("result is True!")
            # 시작버튼 활성화
            self.videoRecogStartBtn.setDisabled(False)
            self.videoRecogRunLabel.setText("모든 검사를 통과하였습니다.")
            self.videoRecogRunLabel.setStyleSheet("color: rgb(51, 0, 255);")
        elif result == 0:
            print("result is False,,")
            self.videoRecogRunLabel.setText("검사를 통과하지 못했습니다.")
            self.videoRecogRunLabel.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.videoRecogRunLabel.setText("")
        self.isVideoCheckCilcked = False

    def videoRecogOpen(self):
        print("videoRecogOpenBtn clicked")
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter(
            self.tr("Data Files (*.mp4 *.avi *.mov *mkv);; Images (*.png *.xpm *.jpg *.gif);; All Files(*.*)"))
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            filesRoute = dialog.selectedFiles()
            self.videoRecogFileRoute = filesRoute[0]
            if self.videoRecogFileRoute != '':
                print(self.videoRecogFileRoute)
                # 무결성 검사 버튼 활성화
                self.videoCheckBtn.setDisabled(False)

    def videoRecogStart(self):
        if self.video_face_recog is None:
            print("video_face_recog is None")
            return

        print("videoRecogStartBtn clicked")
        if self.videoRecogStartBtn.text() == "시작":
            self.videoRecogRunLabel.setStyleSheet("color: rgb(0, 0, 0);")
            # 실시간 인식 비활성화
            self.realRecogStartBtn.setDisabled(True)
            self.init_variable()
            # self.videoRecogRunLabel.setText("프레임추출중..")
            self.videoRecogAnnounceLabel.setText("")
            self.videoRecogStartBtn.setDisabled(True)

            self.video_face_recog.reset()
            self.video_face_recog.set_file_route(self.videoRecogFileRoute)

            self.th = VideoThread(self, self.video_face_recog)
            self.th.threadEvent.connect(self.videoThreadEventHandler)

            # 프레임 추출하는 과정에 대해서만 쓰레드 시작 그 이후 코드는 쓰레드 핸들러에서 실행
            self.th.start()
        else:
            self.stopFlag = True

    def videoThreadEventHandler(self, result):  # 쓰레드핸들러(result값 전달 받는 부분)
        # result값이 1이면 정상적으로 프레임 추출이 완료된다는 뜻
        if result == 200:
            self.videoRecogStartWork()
        elif result is not None:
            self.videoRecogRunLabel.setText("프레임추출중.." + str(result) + "% 진행중")
        else:
            return

    def videoRecogStartWork(self):
        self.videoRecogRunLabel.setText("근무시간 측정중...")
        # 종료 버튼 활성화
        self.videoRecogStartBtn.setDisabled(False)
        self.videoRecogStartBtn.setText("종료")

        while True:
            frame = self.video_face_recog.do_recognition()

            if frame is None:
                print("<<<<동영상이 종료됨>>>>")
                break

            # 근무 신호등 교체
            self.isWorking = self.video_face_recog.working
            if self.stopFlag or self.video_face_recog.video_end:
                print("video stopFlag is True")
                break

        self.videoRecogRunLabel.setText("근무시간 측정완료")
        self.videoRecogAnnounceLabel.setText(self.video_face_recog.calculate_total())
        print("finish")
        # 작업 종료
        self.workStart = False

        self.videoRecogStartBtn.setText("시작")
        self.videoRecogStartBtn.setDisabled(True)
        self.videoCheckBtn.setDisabled(True)
        self.realRecogStartBtn.setDisabled(False)

        # 화면 refresh
        self.refreshView()

    def refreshView(self):
        size = len(self.arrayWorkInfo.work_info_array)
        if size != 0:
            # 근무기록 화면
            workInfo = self.arrayWorkInfo.work_info_array[size-1]
            worktime = str(datetime.timedelta(seconds=workInfo['work_time'])).split(".")[0]
            workString = str(workInfo['date_time']) + "\t" + str(workInfo['work_type']) + "\t\t" + worktime
            self.workListView.append(workString)
            # 근무한시간 재설정
            self.userInfo.work_time += workInfo['work_time']
            self.workTimeLabel.setText(str(datetime.timedelta(seconds=self.userInfo.work_time)).split(".")[0])

        # 로그파일 화면
        with open(self.logInfo.file_path, 'rt', encoding='utf-8') as file:
            log = file.read()

        self.logView.setText(log)

    def closeEvent(self, event):
        print(self.workStart)

        # 실시간 인식 logger close
        if self.face_recog is not None and self.face_recog.logger is not None:
            handlers = self.face_recog.logger.handlers[:]
            for handler in handlers:
                handler.close()
                self.face_recog.logger.removeHandler(handler)

        # 동영상 인식 logger close
        if self.video_face_recog is not None and self.video_face_recog.logger is not None:
            handlers = self.video_face_recog.logger.handlers[:]
            for handler in handlers:
                handler.close()
                self.video_face_recog.logger.removeHandler(handler)

        if self.workStart is False:
            # 자바 프로그램에서 응답이 안왔을 경우를 대비
            if self.isVideoCheckCilcked:
                subprocess.run(["python", "./python/client.py", "not_passed"], shell=True)
            self.sendWorkingInfo()
            self.date_timer.cancel()
        else:
            QtWidgets.QMessageBox.information(self, "QMessageBox", "작업이 실행중이므로 종료할 수 없습니다.")
            event.ignore()

    def sendWorkingInfo(self):
        # 캡쳐 이미지 list 가져오기
        path_dir = './CaptureImage/'
        image_list = os.listdir(path_dir)

        # 근무를 했을 경우
        if len(self.arrayWorkInfo.work_info_array) != 0:
            # 로그 파일에 로그아웃시간 추가
            now = datetime.datetime.now()
            logout_date_format = now.strftime("%Y-%m-%d %H:%M:%S")
            with open(self.logInfo.file_path, 'a', encoding='utf-8') as file:
                file.write("logout 시각 : " + logout_date_format + "\n")

            # url = "http://localhost:8090/awsDBproject/sending/info"
            # url = "http://3.35.38.165:8080/awsDBproject/sending/info"
            url = UrlInfo.instance().url + "/awsDBproject/sending/info"

            # 로그파일 files 배열에 추가
            log_file = open(self.logInfo.file_path, 'r', encoding="utf-8")
            files = [
                ("file", log_file)
            ]

            # 캡쳐 이미지 파일 files 배열에 추가
            image_files = []
            i = 1
            for image_name in image_list:
                image_file = open(path_dir + image_name, "rb")
                image_files.append(image_file)
                obj = ("image" + str(i), image_file)
                files.append(obj)
                i += 1

            # 근무정보 dictionary 타입으로 정의
            info = {
                "working_info": self.arrayWorkInfo.work_info_array,
                "log_created": self.logInfo.created_date,
                "ip": self.userInfo.ip,
                "logout_date": logout_date_format
            }

            print(files)
            print(info)
            try:
                response = requests.post(url, files=files, data=info, verify=False)
            except Exception as e:
                print(e)

            print(response)

            for image_f in image_files:
                image_f.close()

            log_file.close()
            if log_file.closed:
                print("log file closed")
            else:
                print("log file not closed")

        # 캡쳐 이미지 삭제
        for image_name in image_list:
            os.remove(path_dir + image_name)
        # 로그 파일 삭제
        os.remove(self.logInfo.file_path)


class VideoThread(QThread):
    threadEvent = QtCore.pyqtSignal(int)

    def __init__(self, parent, video_face_recog):
        super().__init__()
        self.video_face_recog = video_face_recog
        self.main = parent
        if video_face_recog is None:
            print("쓰레드 init: face_recog is None")

    def run(self):
        # 동영상에서 프레임을 추출하는 과정
        frame_list = []
        while True:
            frame, percent = self.video_face_recog.get_specific_frame()
            if frame is None:
                break
            else:
                frame_list.append(frame)
                self.threadEvent.emit(percent)

        # 프레임 추출이 완료되면 핸들러로 결과 전달(성공 : 1, 실패 : 0)
        if len(frame_list) > 0:
            self.video_face_recog.set_frame_list(frame_list)
            self.threadEvent.emit(200)
        else:
            self.threadEvent.emit(None)


class ReceiveThread(QThread):
    threadEvent = QtCore.pyqtSignal(int)

    def run(self):
        result = server.result_receiver(('', 5000))
        self.threadEvent.emit(result)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    pygui = WindowController()
    pygui.refreshView("추가한 글")
    sys.exit(app.exec_())
