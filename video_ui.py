import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5 import QtWidgets, QtCore


class VideoUi(object):
    def __init__(self):
        # 근무 확인 아이콘 생성
        self.scriptDir = os.path.dirname(os.path.abspath(__file__))
        self.imgLabel = QLabel()
        self.traffic_width = 120
        self.traffic_height = 33
        self.imgLabel.resize(self.traffic_width, self.traffic_height)
        self.pixmap = QPixmap(
            self.scriptDir + os.path.sep + "./templates/Traffic_Lights_init.png"
        )
        self.pixmap = self.pixmap.scaled(self.traffic_width, self.traffic_height)
        self.imgLabel.setPixmap(self.pixmap)

        self.user_name = QLabel("사용자이름")

        self.videoLabel = QLabel()
        self.videoLabel.move(280, 120)

        self.btn_cam_start = QPushButton("Camera On")
        self.btn_cam_stop = QPushButton("Camera Off")

        self.btn_start = QPushButton("시작")
        self.btn_end = QPushButton("종료")

        self.print_total_working = QLabel("total 시간 출력")

    def setup_ui(self, videoForm):
        videoForm.setObjectName("videoForm")
        # videoForm.resize(378, 350)

        self.gridLayoutWidget = QtWidgets.QWidget(videoForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 60, 221, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        hbox = QHBoxLayout()
        hbox.addWidget(self.user_name)
        hbox.addWidget(self.imgLabel)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.btn_cam_start)
        hbox2.addWidget(self.btn_cam_stop)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.btn_start)
        hbox3.addWidget(self.btn_end)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.videoLabel)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.print_total_working)

        self.gridLayout.addLayout(vbox, 0, 0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    videoFrom = QtWidgets.QWidget()
    ui = VideoUi()
    ui.setup_ui(videoFrom)
    videoFrom.show()
    sys.exit(app.exec_())