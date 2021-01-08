# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5.QtGui import QPixmap


class Ui_videoForm(object):
    def setupUi(self, videoForm):
        videoForm.setObjectName("videoForm")
        videoForm.resize(412, 359)

        self.user_name = QtWidgets.QLabel(videoForm)
        self.user_name.setGeometry(QtCore.QRect(60, 50, 91, 21))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_name.setFont(font)
        self.user_name.setObjectName("user_name")

        self.imgLabel = QtWidgets.QLabel(videoForm)
        self.imgLabel.setGeometry(QtCore.QRect(200, 50, 81, 21))
        self.imgLabel.setMaximumSize(QtCore.QSize(120, 33))

        font = QtGui.QFont()
        font.setPointSize(11)
        self.imgLabel.setFont(font)
        self.imgLabel.setObjectName("imgLabel")
        # 신호등 아이콘 사이즈 초기화
        self.scriptDir = os.path.dirname(os.path.abspath(__file__))
        self.traffic_width = 120
        self.traffic_height = 33
        self.imgLabel.resize(self.traffic_width, self.traffic_height)

        self.gridLayoutWidget = QtWidgets.QWidget(videoForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 90, 321, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.videoLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        # self.videoLabel.setMaximumSize(QtCore.QSize(100, 30))
        self.videoLabel.setText("")
        self.videoLabel.setObjectName("videoLabel")

        self.verticalLayout.addWidget(self.videoLabel)

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.btn_start = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_2.addWidget(self.btn_start)

        self.btn_end = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_end.setObjectName("btn_end")
        self.horizontalLayout_2.addWidget(self.btn_end)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_camera = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_camera.setObjectName("btn_camera")
        self.horizontalLayout.addWidget(self.btn_camera)

        self.btn_sound = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_sound.setObjectName("btn_sound")
        self.horizontalLayout.addWidget(self.btn_sound)

        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.print_total_working = QtWidgets.QLabel(self.gridLayoutWidget)
        self.print_total_working.setObjectName("print_total_working")
        self.gridLayout_2.addWidget(self.print_total_working, 4, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)

        self.retranslateUi(videoForm)
        QtCore.QMetaObject.connectSlotsByName(videoForm)

    def retranslateUi(self, videoForm):
        _translate = QtCore.QCoreApplication.translate
        videoForm.setWindowTitle(_translate("videoForm", "Form"))
        self.user_name.setText(_translate("videoForm", "사용자이름"))
        # 근무확인 아이콘
        self.pixmap = QPixmap(
            self.scriptDir + os.path.sep + "./templates/Traffic_Lights_init.png"
        )
        self.pixmap = self.pixmap.scaled(self.traffic_width, self.traffic_height)
        self.imgLabel.setPixmap(self.pixmap)
        self.imgLabel.setText(_translate("videoForm", ""))
        self.btn_start.setText(_translate("videoForm", "시작"))
        self.btn_end.setText(_translate("videoForm", "종료"))
        self.btn_camera.setText(_translate("videoForm", "camera"))
        self.btn_sound.setText(_translate("videoForm", "sound"))
        self.print_total_working.setText(_translate("videoForm", "total 시간 출력"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    videoForm = QtWidgets.QWidget()
    ui = Ui_videoForm()
    ui.setupUi(videoForm)
    videoForm.show()
    sys.exit(app.exec_())