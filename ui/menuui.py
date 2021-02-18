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
        self.resize(1000, 1000)

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.resize(1000, 1000)
        # self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 60, 221, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.logBtn = QtWidgets.QPushButton()
        self.logBtn.setObjectName("logBtn")
        self.gridLayout.addWidget(self.logBtn, 8, 0, 1, 1)

        self.copyCheckBtn = QtWidgets.QPushButton()
        self.copyCheckBtn.setObjectName("copyCheckBtn")
        self.gridLayout.addWidget(self.copyCheckBtn, 7, 0, 1, 1)

        self.processBtn = QtWidgets.QPushButton()
        self.processBtn.setObjectName("processBtn")
        self.gridLayout.addWidget(self.processBtn, 6, 0, 1, 1)

        self.jarBtn = QtWidgets.QPushButton()
        self.jarBtn.setObjectName("jarBtn")
        self.gridLayout.addWidget(self.jarBtn, 5, 0, 1, 1)

        self.videoBtn = QtWidgets.QPushButton()
        self.videoBtn.setObjectName("videoBtn")
        self.gridLayout.addWidget(self.videoBtn, 4, 0, 1, 1)

        self.realTimeBtn = QtWidgets.QPushButton()
        self.realTimeBtn.setObjectName("realTimeBtn")
        self.gridLayout.addWidget(self.realTimeBtn, 3, 0, 1, 1)

        self.settingInfo = QLabel()
        self.userImage = QLabel()
        # self.userImage.resize(400, 400)
        hbox1 = QHBoxLayout(self.gridLayoutWidget)
        hbox1.addWidget(self.userImage)
        hbox1.addWidget(self.settingInfo)
        self.gridLayout.addLayout(hbox1, 2, 0, 1, 1)

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
        self.copyCheckBtn.setText(_translate("menuFrom", "동영상 중복 체크"))
        self.logBtn.setText(_translate("menuForm", "근무 로그 보기"))
