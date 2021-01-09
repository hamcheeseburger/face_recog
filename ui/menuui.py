"""menu ui
기능설명:
    menu ui를 정의하고 있다.
개발자:
    송재임
개발일시:
    2021.01.02.22.00.00
버전:
    0.0.2
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class MenuUi(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(378, 350)

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 60, 221, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.processBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.processBtn.setObjectName("processBtn")
        self.gridLayout.addWidget(self.processBtn, 5, 0, 1, 1)

        self.jarBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.jarBtn.setObjectName("jarBtn")
        self.gridLayout.addWidget(self.jarBtn, 4, 0, 1, 1)

        self.videoBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.videoBtn.setObjectName("videoBtn")
        self.gridLayout.addWidget(self.videoBtn, 3, 0, 1, 1)

        self.realTimeBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.realTimeBtn.setObjectName("realTimeBtn")
        self.gridLayout.addWidget(self.realTimeBtn, 2, 0, 1, 1)

        self.userIdLabel = QtWidgets.QLabel()
        self.logoutBtn = QtWidgets.QPushButton("로그아웃")
        hbox = QHBoxLayout(self.gridLayoutWidget)
        hbox.addWidget(self.userIdLabel)
        hbox.addWidget(self.logoutBtn)
        self.gridLayout.addLayout(hbox, 1, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("menuForm", "Form"))
        self.processBtn.setText(_translate("menuForm", "동영상 무결성 체크(exe 호출)"))
        self.jarBtn.setText(_translate("menuForm", "동영상 무결성 체크(jar 호출)"))
        self.videoBtn.setText(_translate("menuForm", "동영상 인식"))
        self.realTimeBtn.setText(_translate("menuForm", "실시간 인식"))
