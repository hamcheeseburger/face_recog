from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from login_gui import UiDialog


class ExecuteLogin(UiDialog):
    def __init__(self, formDialog):
        UiDialog.__init__(self)
        self.setupUi(formDialog)

        self.btn_login.clicked.connect(self.checkPassword)

    def checkPassword(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'Username' and self.lineEdit_password.text() == '000':
            msg.setText('Success')
            msg.exec_()
            app.quit()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    loginForm = QtWidgets.QDialog()
    execUi = ExecuteLogin(loginForm)
    loginForm.show()
    sys.exit(app.exec_())