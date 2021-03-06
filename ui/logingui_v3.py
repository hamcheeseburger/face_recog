# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiDialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(388, 228)
        self.label_username = QtWidgets.QLabel(dialog)
        self.label_username.setGeometry(QtCore.QRect(69, 53, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_username.setFont(font)
        self.label_username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(dialog)
        self.label_password.setGeometry(QtCore.QRect(70, 84, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_password.setFont(font)
        self.label_password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_password.setObjectName("label_password")
        self.lineEdit_username = QtWidgets.QLineEdit(dialog)
        self.lineEdit_username.setGeometry(QtCore.QRect(170, 54, 141, 21))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(dialog)
        self.lineEdit_password.setGeometry(QtCore.QRect(170, 84, 141, 21))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.btn_login = QtWidgets.QPushButton(dialog)
        self.btn_login.setGeometry(QtCore.QRect(144, 178, 93, 28))
        self.btn_login.setObjectName("btn_login")
        self.label_title = QtWidgets.QLabel(dialog)
        self.label_title.setGeometry(QtCore.QRect(150, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(69, 121, 56, 12))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.combo_url = QtWidgets.QComboBox(dialog)
        self.combo_url.setGeometry(QtCore.QRect(170, 116, 141, 21))
        self.combo_url.setObjectName("combo_url")
        self.combo_url.addItem("Local Server")
        self.combo_url.addItem("AWS Server")
        self.combo_url.addItem("직접입력")

        self.label_url = QtWidgets.QLineEdit(dialog)
        self.label_url.setGeometry(QtCore.QRect(70, 145, 241, 21))
        self.label_url.setObjectName("label_url")
        self.label_url.setText("http://")
        self.label_url.setVisible(False)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Login"))
        self.label_username.setText(_translate("dialog", "아이디"))
        self.label_password.setText(_translate("dialog", "비밀번호"))
        self.btn_login.setText(_translate("dialog", "로그인"))
        self.label_title.setText(_translate("dialog", "Login"))
        self.label.setText(_translate("dialog", "접속 주소"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = UiDialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
