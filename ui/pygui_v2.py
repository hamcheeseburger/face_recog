# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/demo_210218_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QMainWindow


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # self.setupUi()

        # window창
        self.setObjectName("MainWindow")
        self.resize(1190, 647)

        # window창 바로 아래 엘리먼트들을 감싸는 중심 widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(21, 11, 1141, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        # 맨 위의 layout (로그아웃 버튼, 근무기록 버튼 포함)
        self.topLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.setObjectName("topLayout")
        # 로그아웃 버튼
        self.logoutBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoutBtn.sizePolicy().hasHeightForWidth())
        self.logoutBtn.setSizePolicy(sizePolicy)
        self.logoutBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.logoutBtn.setObjectName("logoutBtn")
        self.topLayout.addWidget(self.logoutBtn)
        # 근무기록 버튼
        self.workListBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workListBtn.sizePolicy().hasHeightForWidth())
        self.workListBtn.setSizePolicy(sizePolicy)
        self.workListBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.workListBtn.setObjectName("workListBtn")
        self.topLayout.addWidget(self.workListBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topLayout.addItem(spacerItem)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 372, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        # 왼쪽 레이아웃 (근무기록, 근무자정보, 로그확인 포함)
        self.leftLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout.setSpacing(15)
        self.leftLayout.setObjectName("leftLayout")
        self.workListBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workListBox.sizePolicy().hasHeightForWidth())
        self.workListBox.setSizePolicy(sizePolicy)
        self.workListBox.setMinimumSize(QtCore.QSize(370, 150))
        self.workListBox.setObjectName("workListBox")
        # workListView :근무기록리스트 view
        self.workListView = QtWidgets.QTextBrowser(self.workListBox)
        self.workListView.setGeometry(QtCore.QRect(20, 20, 330, 125))
        self.workListView.setObjectName("workListView")
        self.leftLayout.addWidget(self.workListBox)
        self.userInfoBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userInfoBox.sizePolicy().hasHeightForWidth())
        self.userInfoBox.setSizePolicy(sizePolicy)
        self.userInfoBox.setMinimumSize(QtCore.QSize(370, 170))
        self.userInfoBox.setObjectName("userInfoBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.userInfoBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 331, 131))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # 사용자 이름 라벨
        self.userNameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.userNameLabel.setObjectName("userNameLabel")
        self.verticalLayout_2.addWidget(self.userNameLabel)
        # 사용자 id 라벨
        self.userIdLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.userIdLabel.setObjectName("userIdLabel")
        self.verticalLayout_2.addWidget(self.userIdLabel)
        # 사용자 ip 라벨
        self.userIPLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.userIPLabel.setObjectName("userIPLabel")
        self.verticalLayout_2.addWidget(self.userIPLabel)
        # 세팅 인식단계 라벨
        self.stgLvlLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.stgLvlLabel.setObjectName("stgLvlLabel")
        self.verticalLayout_2.addWidget(self.stgLvlLabel)
        # 세팅 태만기준시간 라벨
        self.stgNodLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.stgNodLabel.setObjectName("stgNodLabel")
        self.verticalLayout_2.addWidget(self.stgNodLabel)
        # 세팅 화면탐지시간 라벨
        self.stgDecLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.stgDecLabel.setObjectName("stgDecLabel")
        self.verticalLayout_2.addWidget(self.stgDecLabel)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        # 사용자 사진 라벨
        self.userImgLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userImgLabel.sizePolicy().hasHeightForWidth())
        self.userImgLabel.setSizePolicy(sizePolicy)
        self.userImgLabel.setMinimumSize(QtCore.QSize(110, 0))
        self.userImgLabel.setObjectName("userImgLabel")
        self.horizontalLayout_4.addWidget(self.userImgLabel)
        self.leftLayout.addWidget(self.userInfoBox)
        self.logBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logBox.sizePolicy().hasHeightForWidth())
        self.logBox.setSizePolicy(sizePolicy)
        self.logBox.setMinimumSize(QtCore.QSize(370, 150))
        self.logBox.setObjectName("logBox")
        # 로그확인 view
        self.logView = QtWidgets.QTextBrowser(self.logBox)
        self.logView.setGeometry(QtCore.QRect(20, 30, 330, 120))
        self.logView.setObjectName("logView")
        self.leftLayout.addWidget(self.logBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(410, 50, 372, 531))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        # 가운데 layout (실시간인식 및 현재날짜 포함)
        self.centerLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.centerLayout.setContentsMargins(0, 0, 0, 0)
        self.centerLayout.setObjectName("centerLayout")
        self.dateBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateBox.sizePolicy().hasHeightForWidth())
        self.dateBox.setSizePolicy(sizePolicy)
        self.dateBox.setMinimumSize(QtCore.QSize(370, 50))
        self.dateBox.setObjectName("dateBox")
        # 현재날짜 라벨
        self.dateLabel = QtWidgets.QLabel(self.dateBox)
        self.dateLabel.setGeometry(QtCore.QRect(10, 20, 211, 16))
        self.dateLabel.setObjectName("dateLabel")
        self.centerLayout.addWidget(self.dateBox)
        self.realRecogBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realRecogBox.sizePolicy().hasHeightForWidth())
        self.realRecogBox.setSizePolicy(sizePolicy)
        self.realRecogBox.setMinimumSize(QtCore.QSize(370, 0))
        self.realRecogBox.setObjectName("realRecogBox")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.realRecogBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 30, 332, 442))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        # 실시간인식 시작 버튼
        self.realRecogStartBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realRecogStartBtn.sizePolicy().hasHeightForWidth())
        self.realRecogStartBtn.setSizePolicy(sizePolicy)
        self.realRecogStartBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.realRecogStartBtn.setObjectName("realRecogStartBtn")
        self.horizontalLayout_2.addWidget(self.realRecogStartBtn)
        self.realRecogEndBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realRecogEndBtn.sizePolicy().hasHeightForWidth())
        # 실시간인식 종료 버튼
        self.realRecogEndBtn.setSizePolicy(sizePolicy)
        self.realRecogEndBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.realRecogEndBtn.setObjectName("realRecogEndBtn")
        self.horizontalLayout_2.addWidget(self.realRecogEndBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        # 실시간인식 카메라 라벨
        self.realRecogCamLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realRecogCamLabel.sizePolicy().hasHeightForWidth())
        self.realRecogCamLabel.setSizePolicy(sizePolicy)
        self.realRecogCamLabel.setMinimumSize(QtCore.QSize(330, 260))
        self.realRecogCamLabel.setObjectName("realRecogCamLabel")
        self.verticalLayout_3.addWidget(self.realRecogCamLabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        # 실시간인식 음성안내 버튼
        self.realRecogSoundBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realRecogSoundBtn.sizePolicy().hasHeightForWidth())
        self.realRecogSoundBtn.setSizePolicy(sizePolicy)
        self.realRecogSoundBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.realRecogSoundBtn.setObjectName("realRecogSoundBtn")
        self.horizontalLayout_6.addWidget(self.realRecogSoundBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        # 실시간인식 신호등 라벨
        self.traffic_width = 120
        self.traffic_height = 33

        self.pixmap = QPixmap(
            # self.scriptDir + os.path.sep + "./templates/Traffic_Lights_init.png"
            "./templates/Traffic_Lights_init.png"
        )
        self.pixmap = self.pixmap.scaled(self.traffic_width, self.traffic_height)
        self.realRecogSignalLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realRecogSignalLabel.sizePolicy().hasHeightForWidth())
        self.realRecogSignalLabel.setSizePolicy(sizePolicy)
        self.realRecogSignalLabel.setMinimumSize(QtCore.QSize(140, 40))
        self.realRecogSignalLabel.setObjectName("realRecogSignalLabel")
        self.realRecogSignalLabel.resize(self.traffic_width, self.traffic_height)
        self.realRecogSignalLabel.setPixmap(self.pixmap)

        self.horizontalLayout_6.addWidget(self.realRecogSignalLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.realRecogAnnounceBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realRecogAnnounceBox.sizePolicy().hasHeightForWidth())
        self.realRecogAnnounceBox.setSizePolicy(sizePolicy)
        self.realRecogAnnounceBox.setTitle("")
        self.realRecogAnnounceBox.setObjectName("realRecogAnnounceBox")
        self.formLayout = QtWidgets.QFormLayout(self.realRecogAnnounceBox)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        # 실시간인식 순수근무시간 라벨
        self.realRecogWorkLabel = QtWidgets.QLabel(self.realRecogAnnounceBox)
        self.realRecogWorkLabel.setObjectName("realRecogWorkLabel")
        self.verticalLayout_4.addWidget(self.realRecogWorkLabel)
        # 실시간인식 총근무시간 라벨
        self.realRecogTotalLabel = QtWidgets.QLabel(self.realRecogAnnounceBox)
        self.realRecogTotalLabel.setObjectName("realRecogTotalLabel")
        self.verticalLayout_4.addWidget(self.realRecogTotalLabel)
        # 실시간인식 근무태만시간 라벨
        self.realRecogNotWorkLabel = QtWidgets.QLabel(self.realRecogAnnounceBox)
        self.realRecogNotWorkLabel.setObjectName("realRecogNotWorkLabel")
        self.verticalLayout_4.addWidget(self.realRecogNotWorkLabel)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_4)
        self.verticalLayout_3.addWidget(self.realRecogAnnounceBox)
        self.centerLayout.addWidget(self.realRecogBox)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(800, 110, 371, 471))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")

        # 오른쪽 레이아웃 (동영상 검증, 동영상 인식 포함)
        self.rightLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.rightLayout.setObjectName("rightLayout")
        self.videoCheckBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoCheckBox.sizePolicy().hasHeightForWidth())
        self.videoCheckBox.setSizePolicy(sizePolicy)
        self.videoCheckBox.setMinimumSize(QtCore.QSize(0, 200))
        self.videoCheckBox.setObjectName("videoCheckBox")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.videoCheckBox)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 30, 393, 141))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        # 동영상검증 열기 버튼
        self.videoCheckOpenBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.videoCheckOpenBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.videoCheckOpenBtn.setObjectName("videoCheckOpenBtn")
        self.horizontalLayout_7.addWidget(self.videoCheckOpenBtn)
        # 동영상 검증 버튼
        self.videoCheckBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.videoCheckBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.videoCheckBtn.setObjectName("videoCheckBtn")
        self.horizontalLayout_7.addWidget(self.videoCheckBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        # 동영상 정보 box
        self.videoInfoBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_5)
        self.videoInfoBox.setObjectName("videoInfoBox")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.videoInfoBox)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 20, 201, 61))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        # 동영상 이름 라벨
        self.videoNameLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.videoNameLabel.setObjectName("videoNameLabel")
        self.verticalLayout_7.addWidget(self.videoNameLabel)
        # 동영상 경로 라벨
        self.videoPathLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.videoPathLabel.setObjectName("videoPathLabel")
        self.verticalLayout_7.addWidget(self.videoPathLabel)
        # 동영상 크기 라벨
        self.videoSizeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.videoSizeLabel.setObjectName("videoSizeLabel")
        self.verticalLayout_7.addWidget(self.videoSizeLabel)
        self.verticalLayout_6.addWidget(self.videoInfoBox)
        self.rightLayout.addWidget(self.videoCheckBox)
        # 동영상 인식 box
        self.videoRecogBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_9)
        self.videoRecogBox.setObjectName("videoRecogBox")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.videoRecogBox)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 20, 331, 231))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        # 동영상 인식 열기 버튼
        self.videoRecogOpenBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.videoRecogOpenBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.videoRecogOpenBtn.setObjectName("videoRecogOpenBtn")
        self.horizontalLayout_8.addWidget(self.videoRecogOpenBtn)
        # 동영상 인식 종료 버튼
        self.videoRecogEndBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.videoRecogEndBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.videoRecogEndBtn.setObjectName("videoRecogEndBtn")
        self.horizontalLayout_8.addWidget(self.videoRecogEndBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.videoRecogRunBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoRecogRunBox.sizePolicy().hasHeightForWidth())
        self.videoRecogRunBox.setSizePolicy(sizePolicy)
        self.videoRecogRunBox.setMinimumSize(QtCore.QSize(0, 60))
        self.videoRecogRunBox.setTitle("")
        self.videoRecogRunBox.setObjectName("videoRecogRunBox")
        # 동영상 인식 실행 시 안내 라벨
        self.videoRecogRunLabel = QtWidgets.QLabel(self.videoRecogRunBox)
        self.videoRecogRunLabel.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.videoRecogRunLabel.setObjectName("videoRecogRunLabel")
        self.verticalLayout_8.addWidget(self.videoRecogRunBox)

        self.videoRecogAnnounceBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoRecogAnnounceBox.sizePolicy().hasHeightForWidth())
        self.videoRecogAnnounceBox.setSizePolicy(sizePolicy)
        self.videoRecogAnnounceBox.setMinimumSize(QtCore.QSize(0, 90))
        self.videoRecogAnnounceBox.setTitle("")
        self.videoRecogAnnounceBox.setObjectName("videoRecogAnnounceBox")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.videoRecogAnnounceBox)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 10, 165, 61))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        # 동영상 인식 순수근무시간 라벨
        self.videoRecogWorkLabel = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.videoRecogWorkLabel.setObjectName("videoRecogWorkLabel")
        self.verticalLayout_9.addWidget(self.videoRecogWorkLabel)
        # 동영상 인식 총근무시간 라벨
        self.videoRecogTotalLabel = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.videoRecogTotalLabel.setObjectName("videoRecogTotalLabel")
        self.verticalLayout_9.addWidget(self.videoRecogTotalLabel)
        # 동영상 인식 근무태만시간 라벨
        self.videoRecogNotWorkLabel = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.videoRecogNotWorkLabel.setObjectName("videoRecogNotWorkLabel")
        self.verticalLayout_9.addWidget(self.videoRecogNotWorkLabel)
        self.verticalLayout_8.addWidget(self.videoRecogAnnounceBox)
        self.rightLayout.addWidget(self.videoRecogBox)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1190, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    # def setupUi(self):

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logoutBtn.setText(_translate("MainWindow", "로그아웃"))
        self.workListBtn.setText(_translate("MainWindow", "근무기록"))
        self.workListBox.setTitle(_translate("MainWindow", "근무 기록"))
        self.userInfoBox.setTitle(_translate("MainWindow", "근무자 정보"))
        self.userNameLabel.setText(_translate("MainWindow", "근무자 이름"))
        self.userIdLabel.setText(_translate("MainWindow", "아이디"))
        self.userIPLabel.setText(_translate("MainWindow", "IP주소"))
        self.stgLvlLabel.setText(_translate("MainWindow", "사용자 인식 단계"))
        self.stgNodLabel.setText(_translate("MainWindow", "태만 기준 시간"))
        self.stgDecLabel.setText(_translate("MainWindow", "화면 탐지 시간 간격"))
        self.userImgLabel.setText(_translate("MainWindow", "사진"))
        self.logBox.setTitle(_translate("MainWindow", "로그확인"))
        self.dateBox.setTitle(_translate("MainWindow", "현재시각"))
        self.dateLabel.setText(_translate("MainWindow", "2020년 2월 4일 오후 11:32"))
        self.realRecogBox.setTitle(_translate("MainWindow", "실시간 인식"))
        self.realRecogStartBtn.setText(_translate("MainWindow", "시작"))
        self.realRecogEndBtn.setText(_translate("MainWindow", "종료"))
        self.realRecogCamLabel.setText(_translate("MainWindow", "카메라 화면"))
        self.realRecogSoundBtn.setText(_translate("MainWindow", "음성안내 끄기"))
        # self.realRecogSignalLabel.setText(_translate("MainWindow", "신호등"))
        self.realRecogWorkLabel.setText(_translate("MainWindow", ""))
        self.realRecogTotalLabel.setText(_translate("MainWindow", ""))
        self.realRecogNotWorkLabel.setText(_translate("MainWindow", ""))
        self.videoCheckBox.setTitle(_translate("MainWindow", "동영상 검증"))
        self.videoCheckOpenBtn.setText(_translate("MainWindow", "동영상 열기"))
        self.videoCheckBtn.setText(_translate("MainWindow", "동영상 검증"))
        self.videoInfoBox.setTitle(_translate("MainWindow", "동영상 정보"))
        self.videoNameLabel.setText(_translate("MainWindow", "동영상 파일 이름"))
        self.videoPathLabel.setText(_translate("MainWindow", "동영상 저장 경로"))
        self.videoSizeLabel.setText(_translate("MainWindow", "동영상 길이"))
        self.videoRecogBox.setTitle(_translate("MainWindow", "동영상 인식"))
        self.videoRecogOpenBtn.setText(_translate("MainWindow", "동영상 열기"))
        self.videoRecogEndBtn.setText(_translate("MainWindow", "종료"))
        self.videoRecogRunLabel.setText(_translate("MainWindow", "동영상 분석 중..78%"))
        self.videoRecogWorkLabel.setText(_translate("MainWindow", "순수근무시간 : 00:50:09"))
        self.videoRecogTotalLabel.setText(_translate("MainWindow", "총근무시간 : 1:00:09"))
        self.videoRecogNotWorkLabel.setText(_translate("MainWindow", "태만시간 : 00:10:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pygui = Ui_MainWindow()
    pygui.show()
    sys.exit(app.exec_())
