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
import socket

import requests
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, QtCore

from info.loginfo import LogInfo
from info.urlInfo import UrlInfo
from login import logincheck
# from ui.logingui import UiDialog
# from ui.logingui_v2 import UiDialog
from ui.logingui_v3 import UiDialog
import face_recognition_models
from face_recognition_models import models
# from ui.menu import ExecuteMenu

from ui.windowcontroller import WindowController
from info.userinfo import UserInfo
from info.settingInfo import SettingInfo


class ExecuteLogin(UiDialog):
    def __init__(self, loginDialog):
        print(face_recognition_models.__email__)
        models
        self.loginDialog = loginDialog
        UiDialog.__init__(self)
        self.setupUi(self.loginDialog)
        self.check_user = logincheck.CheckUser()
        self.btn_login.clicked.connect(self.LoginBtnClicked)
        self.network_thread = NetworkThread()
        self.network_thread.threadEvent.connect(self.threadHandler)
        self.userInfo = UserInfo.instance()

        self.combo_url.currentIndexChanged.connect(self.comboxHandler)

        self.urlInfo = UrlInfo.instance()

    def comboxHandler(self):
        if self.combo_url.currentIndex() == 2:
            self.label_url.setVisible(True)
            return

        self.label_url.setVisible(False)

    def LoginBtnClicked(self):
        # 접속 주소 설정
        comboIndex = self.combo_url.currentIndex()
        if comboIndex == 0:
            self.urlInfo.url = "http://localhost:8090"
        elif comboIndex == 1:
            self.urlInfo.url = "http://3.35.38.165:8080"
        else:
            self.urlInfo.url = self.label_url.text()

        print(self.urlInfo.url)

        msg = QMessageBox()
        id = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        if id == "" or password == "":
            msg.setText('아이디와 비밀번호를 입력하세요.')
            msg.exec_()
            return

        # 서버 로그인
        result = self.check_user.user_check_web_server(id, password)
        if result == 1:
            # self.userInfo.setInfo(id, password, name, image)
            # 사용자 IP 주소 얻기
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            print(s.getsockname()[0])
            self.userInfo.ip = s.getsockname()[0]
            # self.userInfo.ip = socket.gethostbyname(socket.getfqdn())
            self.makeLogFile()
            self.getSetting()

        elif result == 0:
            msg.setText('일치하는 사용자가 없습니다.')
            msg.exec_()
        elif result == -1:
            msg.setText('서버 응답 오류')
            msg.exec_()
        elif result == -2:
            msg.setText('서버와의 접속에 실패하였습니다.')
            msg.exec_()

    def menuWindow(self):
        self.loginDialog.close()
        self.menu = WindowController()

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
        if result_dict is not -1:
            if not result_dict.get("error"):
                settingInfo = SettingInfo.instance()
                settingInfo.RECOV_LV = result_dict['RECOG_LV']
                settingInfo.NOD_SEC = result_dict['NOD_SEC']
                settingInfo.DETEC_SEC = result_dict['DETEC_SEC']
                settingInfo.VID_INTVL = result_dict['VID_INTVL']
            else:
                print("result_dict has error")
        else:
            print("result_dict is None")

        self.menuWindow()


class NetworkThread(QThread):
    threadEvent = QtCore.pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def run(self):
        # 프로그램 기본 세팅 정보를 가져옴
        req_url = UrlInfo.instance().url + "/awsDBproject/setting/client"

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
            self.threadEvent.emit(-1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    loginForm = QtWidgets.QDialog()
    execUi = ExecuteLogin(loginForm)
    loginForm.show()
    sys.exit(app.exec_())
