import sqlite3

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from login_gui import UiDialog
from menuUi import Ui_menuForm
from menu import ExecuteMenu


class ExecuteLogin(UiDialog):
    def __init__(self, loginDialog):
        self.loginDialog = loginDialog
        UiDialog.__init__(self)
        self.setupUi(self.loginDialog)

        self.btn_login.clicked.connect(self.checkPassword)


    def checkPassword(self):
        msg = QMessageBox()
        # if self.lineEdit_username.text() == 'Username' and self.lineEdit_password.text() == '000':
        #     msg.setText('Success')
        #     msg.exec_()
        #     app.quit()
        # else:
        #     msg.setText('Incorrect Password')
        #     msg.exec_()

        id = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        conn = sqlite3.connect("recog_user.db", isolation_level=None)
        cursor = conn.cursor()

        sql = "select name, hex(image) from user_table where id=? and password=?"
        cursor.execute(sql, (id, password))
        row = cursor.fetchone()
        if row is None:
            msg.setText('Incorrect Password')
            msg.exec_()
            return False

        print(row[0])  # 사용자 이름
        strr = row[1]  # 사용자 사진

        with open('test_file.bin', 'a') as file_bin:
            file_bin.write(strr)

        path = "db_image/" + row[0] + ".jpg"
        print(path)
        with open(path, 'wb') as file:
            file.write(bytes.fromhex(strr))

        cursor.close()
        conn.close()

        # msg.setText('Success')
        # msg.exec_()
        # app.quit()
        # return True

        self.menuWindow()
        self.loginDialog.close()

    def menuWindow(self):
        self.loginDialog.close()
        self.menuWidget = QtWidgets.QWidget()
        self.menuUi = ExecuteMenu(self.menuWidget)
        # self.menuWidget.exec_()
        self.menuWidget.show()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    loginForm = QtWidgets.QDialog()
    execUi = ExecuteLogin(loginForm)
    loginForm.show()
    sys.exit(app.exec_())