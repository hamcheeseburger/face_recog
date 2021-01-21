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

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
# import login.logincheck
from login import logincheck
from ui.logingui import UiDialog
from ui.menu import ExecuteMenu
from realTimeCheck import realtimemain
from videoCheck import videomain2


class ExecuteLogin(UiDialog):
    def __init__(self, loginDialog):
        self.loginDialog = loginDialog
        UiDialog.__init__(self)
        self.setupUi(self.loginDialog)

        self.check_user = logincheck.CheckUser()
        realtimemain.FaceRecog.instance()
        videomain2.FaceRecog.instance()
        self.btn_login.clicked.connect(self.checkPassword)

    def checkPassword(self):
        msg = QMessageBox()
        id = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        # db로 로그인
        # if self.check_user.user_check_db(id, password):
        #     self.menuWindow()
        #     self.loginDialog.close()
        # else:
        #     msg.setText('Incorrect Password')
        #     msg.exec_()

        # 바이너리로 로그인
        # if self.check_user.user_check_binary(id, password):
        #     self.menuWindow()
        #     self.loginDialog.close()
        # else:
        #     msg.setText('Incorrect Password')
        #     msg.exec_()

        # AWS DB로 로그인
        # if self.check_user.user_check_aws(id, password):
        #     self.menuWindow()
        #     self.loginDialog.close()
        # else:
        #     msg.setText('Incorrect Password')
        #     msg.exec_()

        # 서버 로그인
        if self.check_user.user_check_web_server(id, password):
            self.menuWindow()
            self.loginDialog.close()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()

    def menuWindow(self):
        self.loginDialog.close()
        # self.menuWidget = QtWidgets.QWidget()
        # self.menuUi = ExecuteMenu(self.menuWidget, self.lineEdit_username.text())

        self.menu = ExecuteMenu(self.lineEdit_username.text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    loginForm = QtWidgets.QDialog()
    execUi = ExecuteLogin(loginForm)
    loginForm.show()
    sys.exit(app.exec_())