# from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('로그인')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="3"> 사용자이름 </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('사용자 이름을 입력하세요.')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="3"> 비밀번호 </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('비밀번호를 입력하세요.')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'Usernmae' and self.lineEdit_password.text() == '000':
            msg.setText('Success')
            msg.exec_()
            app.quit()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = LoginForm()
    form.show()

    sys.exit(app.exec_())
