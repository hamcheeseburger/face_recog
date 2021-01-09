"""realtime face recognition ui
기능설명:
    실시간 얼굴인식 ui를 정의하였다.
개발자:
    송재임 유현지
개발일시:
    2021.01.05.22.00.00
버전:

"""
import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, QFileDialog, QTextEdit
from PyQt5 import QtWidgets, QtCore


class RealTimeUi(QWidget):
    def __init__(self):
        # 근무 확인 아이콘 생성
        QWidget.__init__(self)
        self.scriptDir = os.path.dirname(os.path.abspath(__file__))
        self.imgLabel = QLabel()
        self.traffic_width = 120
        self.traffic_height = 33
        self.imgLabel.resize(self.traffic_width, self.traffic_height)
        self.pixmap = QPixmap(
            # self.scriptDir + os.path.sep + "./templates/Traffic_Lights_init.png"
            "./templates/Traffic_Lights_init.png"
        )
        self.pixmap = self.pixmap.scaled(self.traffic_width, self.traffic_height)
        self.imgLabel.setPixmap(self.pixmap)

        self.user_name = QLabel("사용자이름")

        self.videoLabel = QLabel()
        self.videoLabel.move(280, 120)

        self.btn_cam_start = QPushButton("Camera")
        self.btn_sound_start = QPushButton("sound")

        self.btn_start = QPushButton("시작")
        self.btn_end = QPushButton("종료")

        self.print_total_working = QLabel("total 시간 출력")

        # self.routeLabel = QLabel()
        # self.routeLabel.setStyleSheet("color: black;"
        #                               "background-color : white;"
        #                       "border-style: solid;"
        #                       "border-width: 1px;"
        #                       "border-color: black;")
        # self.btn_select_route = QPushButton('불러오기')

        hbox = QHBoxLayout()
        hbox.addWidget(self.user_name)
        hbox.addWidget(self.imgLabel)

        # hbox1 = QHBoxLayout()
        # hbox1.addWidget(self.routeLabel)
        # hbox1.addWidget(self.btn_select_route)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.btn_cam_start)
        hbox2.addWidget(self.btn_sound_start)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.btn_start)
        hbox3.addWidget(self.btn_end)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        # vbox.addLayout(hbox1)
        vbox.addWidget(self.videoLabel)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.print_total_working)

        self.setLayout(vbox)

        self.setWindowTitle("Face Recognition")
        self.move(300, 300)
        self.resize(400, 300)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = RealTimeUi()
    ui.show()
    sys.exit(app.exec_())