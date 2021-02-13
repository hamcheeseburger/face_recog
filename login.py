"""login
기능설명:
     로그인 Ui의 기능을 담당하는 모듈
개발자:
    송재임, 유현지
개발일시:
    2021.01.07.16.51.00
버전:
    0.0.1
"""
import datetime

import requests
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, QtCore

from info.loginfo import LogInfo
from login import logincheck
from realTimeCheck import realtimemain
from videoCheck import videomain2
from ui.logingui import UiDialog
from ui.menu import ExecuteMenu
from info.userinfo import UserInfo


class ExecuteLogin(UiDialog):
    def __init__(self, loginDialog):
        self.loginDialog = loginDialog
        UiDialog.__init__(self)
        self.setupUi(self.loginDialog)

        self.check_user = logincheck.CheckUser()
        self.btn_login.clicked.connect(self.checkPassword)
        self.network_thread = NetworkThread()
        self.network_thread.threadEvent.connect(self.threadHandler)
        self.realFaceRecog = realtimemain.FaceRecog.instance()
        self.videoFaceRecog = videomain2.FaceRecog.instance()
        self.userInfo = UserInfo.instance()

    def checkPassword(self):
        msg = QMessageBox()
        id = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        # 서버 로그인
        result, name, image = self.check_user.user_check_web_server(id, password)
        if result == 1:
            self.userInfo.setInfo(id, password, name, image)
            self.makeLogFile()
            self.getSetting()
            self.menuWindow()
            self.loginDialog.close()
        elif result == 0:
            msg.setText('Incorrect Password')
            msg.exec_()
        elif result == -1:
            msg.setText('Response Error')
            msg.exec_()
        elif result == -2:
            msg.setText('Network Error')
            msg.exec_()

    def menuWindow(self):
        self.loginDialog.close()
        # self.menuWidget = QtWidgets.QWidget()
        # self.menuUi = ExecuteMenu(self.menuWidget, self.lineEdit_username.text())

        self.menu = ExecuteMenu(self.lineEdit_username.text())

    def makeLogFile(self):
        now = datetime.datetime.now()
        time_format = now.strftime("%Y%m%d_%H-%M-%S")
        created_format = now.strftime("%Y-%m-%d %H:%M:%S")

        file_name = self.userInfo.id + "_" + time_format + ".txt"
        with open("./worklog/" + file_name, 'wt', encoding='utf-8') as file:
            file.write("login 시각 : " + created_format + "\n")
        self.logInfo = LogInfo.instance()
        self.logInfo.setFileName(file_name)
        self.logInfo.created_date = created_format

        print(self.logInfo.file_path)

    def getSetting(self):
        # print("Getting setting information from server!")
        self.network_thread.start()

    def threadHandler(self, result_dict):
        if result_dict is not None:
            if not result_dict.get("error"):
                print("\nGet SETTING from SERVER")
                print("DETEC_SEC : " + str(result_dict['DETEC_SEC']))
                print("NOD_SEC : " + str(result_dict['NOD_SEC']))
                print("VID_INTVL : " + str(result_dict['VID_INTVL']))
                print("RECOV_LV : " + str(result_dict['RECOG_LV']) + "\n")

                self.realFaceRecog.NOD_SEC = result_dict['NOD_SEC']
                self.realFaceRecog.DETEC_SEC = result_dict['DETEC_SEC']
                self.realFaceRecog.RECOG_LV = result_dict['RECOG_LV']

                self.videoFaceRecog.VID_INTVL = result_dict['VID_INTVL']
                self.videoFaceRecog.NOD_SEC = result_dict['NOD_SEC']
                self.videoFaceRecog.RECOG_LV = result_dict['RECOG_LV']
            else:
                print("result_dict has error")
        else:
            print("result_dict is None")


class NetworkThread(QThread):
    threadEvent = QtCore.pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def run(self):
        # 프로그램 기본 세팅 정보를 가져옴
        # req_url = "http://3.35.38.165:8080/awsDBproject/setting/client"
        req_url = "http://localhost:8090/awsDBproject/setting/client"
        try:
            response = requests.post(req_url, data=None, verify=False)
        except:
            print("Connection Error")
            self.threadEvent.emit(None)

        if response.status_code == 200:
            setting_data = response.json()
            self.threadEvent.emit(setting_data)
        else:
            print(response.status_code)
            self.threadEvent.emit(None)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    loginForm = QtWidgets.QDialog()
    execUi = ExecuteLogin(loginForm)
    loginForm.show()
    sys.exit(app.exec_())
