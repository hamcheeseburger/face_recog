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
import os

import requests
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QThread
# from ui.video import ExecuteVideo
from info.userinfo import UserInfo
from ui.video2 import ExecuteVideo
import subprocess
from ui.menuui import MenuUi
from ui.realtime import ExecuteRealTime
from ui.log import Log
from info.workinfo import ArrayWorkInfo


class jar_thread(QThread):
    def run(self):
        cmd = "java -jar ./Original_Tool/VideoAnalyzer.jar ./test.txt"
        os.system(cmd)


class ExecuteMenu(MenuUi):
    def __init__(self, id):
        MenuUi.__init__(self)

        self.userInfo = UserInfo.instance()
        self.arrayWorkInfo = ArrayWorkInfo.instance()

        self.user_id = id
        self.processBtn.clicked.connect(self.callExe)
        self.jarBtn.clicked.connect(self.callJar)
        self.videoBtn.clicked.connect(self.call_video_recog)
        self.realTimeBtn.clicked.connect(self.call_realTime_recog)
        self.logBtn.clicked.connect(self.call_log_file)
        self.copyCheckBtn.clicked.connect(self.call_copy_check)

        self.th1 = jar_thread()
        self.userIdLabel.setText(self.userInfo.name + "님 환영합니다.")
        self.logoutBtn.clicked.connect(self.logout)

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
        url = "http://localhost:8090/awsDBproject/working/info"
        info = {
            "working_info": self.arrayWorkInfo.work_info_array,
            "id": self.user_id
        }
        print(info)
        try:
            response = requests.post(url, json=info, verify=False)
        except:
            print("Connection Error")

        print(response.status_code)

        # if response.status_code == 200:


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    menuForm = QtWidgets.QWidget()
    menuUi = ExecuteMenu(menuForm)
    menuForm.show()
    sys.exit(app.exec_())
