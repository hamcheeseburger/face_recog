"""gui2 (useless)
기능설명:
    동영상으로 근무시간을 측정할 때 사용되는 UI (menu.py가 생기기 이전에 간이로 사용했던 ui)
    useless/videoCheck/main2.py와 연결되는 UI
개발자:
    송재임, 유현지
개발일시:
    2021.01.02.20.44.00
버전:
    0.0.0
"""
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
from useless.videoCheck import main2
# import main
import os


class Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.btn_pause = QPushButton('일시중지', self)
        self.stopFlag = False
        self.pauseFlag = False
        self.isCameraDisplayed = False
        self.initUI()

    def initUI(self):
        # 근무 확인 아이콘 생성
        self.scriptDir = os.path.dirname(os.path.abspath(__file__))
        self.imgLabel = QLabel()
        self.traffic_width = 120
        self.traffic_height = 33
        self.imgLabel.resize(self.traffic_width, self.traffic_height)
        self.pixmap = QPixmap(self.scriptDir + os.path.sep + './templates/Traffic_Lights_init.png')
        self.pixmap = self.pixmap.scaled(self.traffic_width, self.traffic_height)
        self.imgLabel.setPixmap(self.pixmap)

        # 비디오 출력용 라벨 생성
        self.videoLabel = QLabel(self)
        self.videoLabel.move(280, 120)
        # self.videoLabel.resize(640, 480)


        # 카메라 버튼 및 출력창 생성
        btn_cam_start = QPushButton("Camera On")
        btn_cam_stop = QPushButton("Camera Off")

        #버튼 생성
        btn_start = QPushButton('시작', self)
        btn_end = QPushButton('종료', self)

        label = QLabel('사용자 이름 입력(Knowns 파일에 있는 사용자명과 일치해야함)')
        # 사용자명 입력받을 editText
        self.et_name = QLineEdit(self)
        # 근무관련시간 출력할 text
        self.print_total_working = QLabel('total 시간 출력')

        # horizonal box, LinearLayout(Horizon)과 비슷한 역할을 함
        hbox = QHBoxLayout()
        hbox.addWidget(btn_start)
        hbox.addWidget(self.btn_pause)
        hbox.addWidget(btn_end)

        # vertical box, LinearLayout(Vertical)과 비슷한 역할을 함
        vbox = QVBoxLayout()
        # 카메라 화면 레이아웃 부착
        vbox.addWidget(self.videoLabel)
        vbox.addWidget(btn_cam_start)
        vbox.addWidget(btn_cam_stop)

        vbox.addWidget(label)
        vbox.addWidget(self.et_name)
        vbox.addLayout(hbox)
        vbox.addWidget(self.imgLabel)
        vbox.addWidget(self.print_total_working)

        self.setLayout(vbox)

        # 버튼 클릭 핸들러
        btn_start.clicked.connect(self.start_recog)
        self.btn_pause.clicked.connect(self.pause_recog)
        btn_end.clicked.connect(self.end_recog)

        # 비디오 화면 버튼 핸들러
        btn_cam_start.clicked.connect(self.cam_start)
        btn_cam_stop.clicked.connect(self.cam_stop)

        self.setWindowTitle('Face Recognition')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

    # 시작버튼 눌렸을 때 실행되는 함수
    def start_recog(self):
        self.print_total_working.setText('프레임추출중.. 잠시만 기다려주세요')
        face_recog = main2.FaceRecog()
        face_recog.get_name(self.et_name.text())
        print(face_recog.known_face_names)
        # frame_list = face_recog.get_specific_frame()

        start = time.time()
        print(start)
        # if len(frame_list) > 0:
        self.print_total_working.setText('근무시간 측정중...')
        while True:
            frame = face_recog.do_recognition()
            # frame이 아니라 jpg byte를 받아와서 이미지 출력
            # bytes -> QPixmap으로 변환하는 것이 핵심
            # frame이 null이 아닐 경우에만 윈도우 상 출력
            if frame is None:
                print("<<<<동영상이 종료됨>>>>")
                break
            elif self.isCameraDisplayed is True:
                # print('frame is not None')
                # 매개 변수 jpg_bytes -> 비디오 파일 꺼지자 마자 프로그램 강제 종료
                # 매개 변수 face_recog.get_jpg_bytes() -> 이상 없음
                self.my_bytes = QByteArray(face_recog.get_jpg_bytes())
                self.bytes_pixmap = QPixmap()
                ok = self.bytes_pixmap.loadFromData(self.my_bytes)
                assert ok
                self.videoLabel.setPixmap(self.bytes_pixmap)
                self.videoLabel.setFixedSize(1280, 720)

            # 근무 신호등 교체
            self.isWorking = face_recog.working
            if self.isWorking is True:
                self.change_traffic_light('../../templates/Traffic_Lights_green.png')
            else:
                self.change_traffic_light('../../templates/Traffic_Lights_red.png')

            if self.stopFlag or face_recog.video_end:
                break
            # cv2.imshow("Frame", frame)
            cv2.waitKey(5) & 0xFF
            face_recog.notifyIsPaused(self.pauseFlag)
        end = time.time()
        print(str(end) + ", " + str(end-start))
        cv2.destroyAllWindows()
        self.print_total_working.setText(face_recog.calculate_total())
        print('finish')
        # 종료버튼을 누르고 나서 신호등과 카메라 화면을 초기화
        self.cam_stop()
        self.videoLabel.setText('근무 종료')
        # self.videoLabel.resize(self.videoLabel.width(), self.videoLabel.height())
        self.change_traffic_light('../../templates/Traffic_Lights_init.png')
        # 윈도우 창을 적절하게 자동으로 조정
        self.adjustSize()

    def change_traffic_light(self, file_path):
        self.pixmap = QPixmap(self.scriptDir + os.path.sep + file_path)
        self.pixmap = self.pixmap.scaled(self.traffic_width, self.traffic_height)
        self.imgLabel.setPixmap(self.pixmap)

    def pause_recog(self):
        # 처음 일시중지버튼 눌렸을 때
        if not self.pauseFlag:
            self.pauseFlag = True
            self.btn_pause.setText('재시작')
        else:
            self.pauseFlag = False
            self.btn_pause.setText('일시중지')

    # 종료버튼 눌렸을 때 실행되는 함수
    def end_recog(self):
        self.stopFlag = True

    def cam_stop(self):
        print('cam_stop')
        self.isCameraDisplayed = False
        self.videoLabel.setText('화면 중지')
        # self.videoLabel.resize(100, 30)
        self.videoLabel.setFixedSize(100, 30)
        self.adjustSize()

    def cam_start(self):
        print('cam_start')
        self.isCameraDisplayed = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
