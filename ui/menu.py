"""menu action
기능설명:
    menu ui를 상속받아 메뉴 버튼 클릭시의 동작을 정의한다.
개발자:
    송재임 유현지
개발일시:
    2021.01.02.23.00.00
버전:
    0.0.2
"""
import datetime
import os

import requests
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QThread
# from ui.video import ExecuteVideo
from info.userinfo import UserInfo
from realTimeCheck import realtimemain
from ui.video2 import ExecuteVideo
import subprocess
from ui.menuui import MenuUi
from ui.realtime import ExecuteRealTime
from ui.log import Log
from info.workinfo import ArrayWorkInfo
from info.loginfo import LogInfo
from videoCheck import videomain2


class jar_thread(QThread):
    def run(self):
        cmd = "java -jar ./Original_Tool/VideoAnalyzer.jar ./test.txt"
        os.system(cmd)


class ExecuteMenu(MenuUi):
    def __init__(self, id):
        MenuUi.__init__(self)

        # 사용자정보객체 생성
        self.userInfo = UserInfo.instance()
        # 근무정보를 담을 array 클래스 생성
        self.arrayWorkInfo = ArrayWorkInfo.instance()
        self.logInfo = LogInfo.instance()

        self.user_id = id # 없어져도 되는 변수..
        # 버튼 클릭리스너 설정
        self.processBtn.clicked.connect(self.callExe)
        self.jarBtn.clicked.connect(self.callJar)
        self.videoBtn.clicked.connect(self.call_video_recog)
        self.realTimeBtn.clicked.connect(self.call_realTime_recog)
        self.logBtn.clicked.connect(self.call_log_file)
        self.copyCheckBtn.clicked.connect(self.call_copy_check)
        self.logoutBtn.clicked.connect(self.logout)

        self.th1 = jar_thread()
        # 사용자이름으로 환영문구 설정
        self.userIdLabel.setText(self.userInfo.name + "님 환영합니다.")
        self.show()

    def callExe(self):
        # 윈도우 명령어는 쉘안에 들어있으므로 shell=Ture여야 윈도우 쉘 명령어 사용ok
        fileName = './Original_Tool/VideoAnalyzer.exe'
        subprocess.run(["start", fileName], shell=True)

    def callJar(self):
        self.th1.start()

    def call_realTime_recog(self):
        self.realTimeExe = ExecuteRealTime(self.user_id)

    def call_video_recog(self):
        # self.videoWidget = QtWidgets.QWidget()
        # self.videoUi = ExecuteVideo(self.videoWidget, self.user_id)
        #
        # self.videoWidget.show()

        self.videoExe = ExecuteVideo(self.user_id)

    def call_log_file(self):
        print("로그 버튼 클릭")
        self.logExe = Log()

    def call_copy_check(self):
        print("중복체크버튼 클릭")
        fileName = './Duplicate/DuplicateVideoDetector.jar'
        subprocess.run(["start", fileName], shell=True)

    def logout(self):
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        print("closed")
        self.sendWorkingInfo()
        self.logout()

    def sendWorkingInfo(self):
        path_dir = './CaptureImage/'
        image_list = os.listdir(path_dir)
        if len(self.arrayWorkInfo.work_info_array) == 0:
            os.remove(self.logInfo.file_path)
        else:

            url = "http://localhost:8090/awsDBproject/sending/info"
            # url = "http://3.35.38.165:8080/awsDBproject/working/info"
            # url = "http://3.35.38.165:8080/awsDBproject/sending/info"
            log_file = open(self.logInfo.file_path, 'r', encoding="utf-8")
            # upload = {
            #     "log_file": log_file
            # }

            files = [
                ("file", log_file)
            ]

            i = 1
            for image_name in image_list:
                image_file = open(path_dir + image_name, "rb")
                obj = ("image" + str(i), image_file)
                files.append(obj)
                i += 1

            info = {
                "working_info": self.arrayWorkInfo.work_info_array,
                "log_created": self.logInfo.created_date
            }

            print(files)
            print(info)
            try:
                response = requests.post(url, files=files, data=info, verify=False)
            except Exception as e:
                print(e)

            print(response)

        for image_name in image_list:
            os.remove(path_dir + image_name)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    menuForm = QtWidgets.QWidget()
    menuUi = ExecuteMenu(menuForm)
    menuForm.show()
    sys.exit(app.exec_())
