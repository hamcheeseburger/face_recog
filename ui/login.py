from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from ui.login_gui import UiDialog
from login.loginCheck import CheckUser
from ui.menu2 import ExecuteMenu


class ExecuteLogin(UiDialog):
    def __init__(self, loginDialog):
        self.loginDialog = loginDialog
        UiDialog.__init__(self)
        self.setupUi(self.loginDialog)

        self.check_user = CheckUser()
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
        if self.check_user.user_check_binary(id, password):
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