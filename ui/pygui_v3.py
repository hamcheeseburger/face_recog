# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_210218_v3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 1151, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.topLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.setObjectName("topLayout")
        self.logoutBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoutBtn.sizePolicy().hasHeightForWidth())
        self.logoutBtn.setSizePolicy(sizePolicy)
        self.logoutBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.logoutBtn.setObjectName("logoutBtn")
        self.topLayout.addWidget(self.logoutBtn)
        self.dateBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateBox.sizePolicy().hasHeightForWidth())
        self.dateBox.setSizePolicy(sizePolicy)
        self.dateBox.setMinimumSize(QtCore.QSize(370, 50))
        self.dateBox.setObjectName("dateBox")
        self.dateLabel = QtWidgets.QLabel(self.dateBox)
        self.dateLabel.setGeometry(QtCore.QRect(10, 20, 211, 16))
        self.dateLabel.setObjectName("dateLabel")
        self.topLayout.addWidget(self.dateBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topLayout.addItem(spacerItem)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(420, 80, 374, 431))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.middleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.middleLayout.setContentsMargins(0, 0, 0, 0)
        self.middleLayout.setObjectName("middleLayout")
        self.videoRecogBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_9)
        self.videoRecogBox.setObjectName("videoRecogBox")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.videoRecogBox)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 30, 331, 371))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.videoCheckBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoCheckBox.sizePolicy().hasHeightForWidth())
        self.videoCheckBox.setSizePolicy(sizePolicy)
        self.videoCheckBox.setMinimumSize(QtCore.QSize(0, 70))
        self.videoCheckBox.setTitle("")
        self.videoCheckBox.setObjectName("videoCheckBox")
        self.widget = QtWidgets.QWidget(self.videoCheckBox)
        self.widget.setGeometry(QtCore.QRect(10, 10, 312, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.videoCheckTextlabel = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoCheckTextlabel.sizePolicy().hasHeightForWidth())
        self.videoCheckTextlabel.setSizePolicy(sizePolicy)
        self.videoCheckTextlabel.setMinimumSize(QtCore.QSize(80, 30))
        self.videoCheckTextlabel.setObjectName("videoCheckTextlabel")
        self.horizontalLayout_7.addWidget(self.videoCheckTextlabel)
        self.videoCheckBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoCheckBtn.sizePolicy().hasHeightForWidth())
        self.videoCheckBtn.setSizePolicy(sizePolicy)
        self.videoCheckBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.videoCheckBtn.setObjectName("videoCheckBtn")
        self.horizontalLayout_7.addWidget(self.videoCheckBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_8.addWidget(self.videoCheckBox)
        self.videoRecogBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoRecogBox_2.sizePolicy().hasHeightForWidth())
        self.videoRecogBox_2.setSizePolicy(sizePolicy)
        self.videoRecogBox_2.setMinimumSize(QtCore.QSize(0, 70))
        self.videoRecogBox_2.setTitle("")
        self.videoRecogBox_2.setObjectName("videoRecogBox_2")
        self.widget1 = QtWidgets.QWidget(self.videoRecogBox_2)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 311, 51))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.videoRecogOpenBtn = QtWidgets.QPushButton(self.widget1)
        self.videoRecogOpenBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.videoRecogOpenBtn.setObjectName("videoRecogOpenBtn")
        self.horizontalLayout_8.addWidget(self.videoRecogOpenBtn)
        self.videoRecogEndBtn = QtWidgets.QPushButton(self.widget1)
        self.videoRecogEndBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.videoRecogEndBtn.setObjectName("videoRecogEndBtn")
        self.horizontalLayout_8.addWidget(self.videoRecogEndBtn)
        self.verticalLayout_8.addWidget(self.videoRecogBox_2)
        self.videoRecogRunBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoRecogRunBox.sizePolicy().hasHeightForWidth())
        self.videoRecogRunBox.setSizePolicy(sizePolicy)
        self.videoRecogRunBox.setMinimumSize(QtCore.QSize(0, 60))
        self.videoRecogRunBox.setTitle("")
        self.videoRecogRunBox.setObjectName("videoRecogRunBox")
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
        self.videoRecogWorkLabel = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.videoRecogWorkLabel.setObjectName("videoRecogWorkLabel")
        self.verticalLayout_9.addWidget(self.videoRecogWorkLabel)
        self.videoRecogTotalLabel = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.videoRecogTotalLabel.setObjectName("videoRecogTotalLabel")
        self.verticalLayout_9.addWidget(self.videoRecogTotalLabel)
        self.videoRecogNotWorkLabel = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.videoRecogNotWorkLabel.setObjectName("videoRecogNotWorkLabel")
        self.verticalLayout_9.addWidget(self.videoRecogNotWorkLabel)
        self.verticalLayout_8.addWidget(self.videoRecogAnnounceBox)
        self.middleLayout.addWidget(self.videoRecogBox)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(30, 80, 371, 431))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.leftLayput = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.leftLayput.setContentsMargins(0, 0, 0, 0)
        self.leftLayput.setObjectName("leftLayput")
        self.realRecogBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realRecogBox.sizePolicy().hasHeightForWidth())
        self.realRecogBox.setSizePolicy(sizePolicy)
        self.realRecogBox.setMinimumSize(QtCore.QSize(370, 0))
        self.realRecogBox.setObjectName("realRecogBox")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.realRecogBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 345, 391))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
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
        self.realRecogEndBtn.setSizePolicy(sizePolicy)
        self.realRecogEndBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.realRecogEndBtn.setObjectName("realRecogEndBtn")
        self.horizontalLayout_2.addWidget(self.realRecogEndBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.realRecogCamLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realRecogCamLabel.sizePolicy().hasHeightForWidth())
        self.realRecogCamLabel.setSizePolicy(sizePolicy)
        self.realRecogCamLabel.setMinimumSize(QtCore.QSize(330, 200))
        self.realRecogCamLabel.setObjectName("realRecogCamLabel")
        self.verticalLayout_3.addWidget(self.realRecogCamLabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.faceRecogDisplayBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faceRecogDisplayBtn.sizePolicy().hasHeightForWidth())
        self.faceRecogDisplayBtn.setSizePolicy(sizePolicy)
        self.faceRecogDisplayBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.faceRecogDisplayBtn.setObjectName("faceRecogDisplayBtn")
        self.horizontalLayout_6.addWidget(self.faceRecogDisplayBtn)
        self.faceRecogSoundBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faceRecogSoundBtn.sizePolicy().hasHeightForWidth())
        self.faceRecogSoundBtn.setSizePolicy(sizePolicy)
        self.faceRecogSoundBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.faceRecogSoundBtn.setObjectName("faceRecogSoundBtn")
        self.horizontalLayout_6.addWidget(self.faceRecogSoundBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.signalLampLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signalLampLabel.sizePolicy().hasHeightForWidth())
        self.signalLampLabel.setSizePolicy(sizePolicy)
        self.signalLampLabel.setMinimumSize(QtCore.QSize(140, 40))
        self.signalLampLabel.setObjectName("signalLampLabel")
        self.horizontalLayout_6.addWidget(self.signalLampLabel)
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
        self.realRecogWorkLabel = QtWidgets.QLabel(self.realRecogAnnounceBox)
        self.realRecogWorkLabel.setObjectName("realRecogWorkLabel")
        self.verticalLayout_4.addWidget(self.realRecogWorkLabel)
        self.realRecogTotalLabel = QtWidgets.QLabel(self.realRecogAnnounceBox)
        self.realRecogTotalLabel.setObjectName("realRecogTotalLabel")
        self.verticalLayout_4.addWidget(self.realRecogTotalLabel)
        self.realRecogNotWorkLabel = QtWidgets.QLabel(self.realRecogAnnounceBox)
        self.realRecogNotWorkLabel.setObjectName("realRecogNotWorkLabel")
        self.verticalLayout_4.addWidget(self.realRecogNotWorkLabel)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_4)
        self.verticalLayout_3.addWidget(self.realRecogAnnounceBox)
        self.leftLayput.addWidget(self.realRecogBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(810, 80, 372, 571))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.rightLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.rightLayout.setSpacing(30)
        self.rightLayout.setObjectName("rightLayout")
        self.userInfoBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userInfoBox.sizePolicy().hasHeightForWidth())
        self.userInfoBox.setSizePolicy(sizePolicy)
        self.userInfoBox.setMinimumSize(QtCore.QSize(370, 200))
        self.userInfoBox.setObjectName("userInfoBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.userInfoBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 331, 171))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.userNameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.userNameLabel.setObjectName("userNameLabel")
        self.verticalLayout_2.addWidget(self.userNameLabel)
        self.userIdLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.userIdLabel.setObjectName("userIdLabel")
        self.verticalLayout_2.addWidget(self.userIdLabel)
        self.userIPLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.userIPLabel.setObjectName("userIPLabel")
        self.verticalLayout_2.addWidget(self.userIPLabel)
        self.stgLvlLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.stgLvlLabel.setObjectName("stgLvlLabel")
        self.verticalLayout_2.addWidget(self.stgLvlLabel)
        self.stgNodLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.stgNodLabel.setObjectName("stgNodLabel")
        self.verticalLayout_2.addWidget(self.stgNodLabel)
        self.stgDecLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.stgDecLabel.setObjectName("stgDecLabel")
        self.verticalLayout_2.addWidget(self.stgDecLabel)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.userImgLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userImgLabel.sizePolicy().hasHeightForWidth())
        self.userImgLabel.setSizePolicy(sizePolicy)
        self.userImgLabel.setMinimumSize(QtCore.QSize(120, 0))
        self.userImgLabel.setObjectName("userImgLabel")
        self.horizontalLayout_4.addWidget(self.userImgLabel)
        self.rightLayout.addWidget(self.userInfoBox)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.rightLayout.addItem(spacerItem5)
        self.logBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logBox.sizePolicy().hasHeightForWidth())
        self.logBox.setSizePolicy(sizePolicy)
        self.logBox.setMinimumSize(QtCore.QSize(370, 300))
        self.logBox.setObjectName("logBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.logBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 331, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.logRefreshBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logRefreshBtn.sizePolicy().hasHeightForWidth())
        self.logRefreshBtn.setSizePolicy(sizePolicy)
        self.logRefreshBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.logRefreshBtn.setObjectName("logRefreshBtn")
        self.horizontalLayout.addWidget(self.logRefreshBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.logView = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.logView.setObjectName("logView")
        self.verticalLayout.addWidget(self.logView)
        self.rightLayout.addWidget(self.logBox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 520, 771, 131))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.bottomBox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.bottomBox.setContentsMargins(0, 0, 0, 0)
        self.bottomBox.setObjectName("bottomBox")
        self.workListBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workListBox.sizePolicy().hasHeightForWidth())
        self.workListBox.setSizePolicy(sizePolicy)
        self.workListBox.setMinimumSize(QtCore.QSize(765, 100))
        self.workListBox.setObjectName("workListBox")
        self.workListView = QtWidgets.QTextBrowser(self.workListBox)
        self.workListView.setGeometry(QtCore.QRect(20, 20, 731, 101))
        self.workListView.setObjectName("workListView")
        self.bottomBox.addWidget(self.workListBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1209, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logoutBtn.setText(_translate("MainWindow", "로그아웃"))
        self.dateBox.setTitle(_translate("MainWindow", "현재시각"))
        self.dateLabel.setText(_translate("MainWindow", "2020년 2월 4일 오후 11:32"))
        self.videoRecogBox.setTitle(_translate("MainWindow", "동영상 인식"))
        self.videoCheckTextlabel.setText(_translate("MainWindow", "무결성 및 중복 검증"))
        self.videoCheckBtn.setText(_translate("MainWindow", "동영상 검증"))
        self.label.setText(_translate("MainWindow", "동영상 근무 인식"))
        self.videoRecogOpenBtn.setText(_translate("MainWindow", "동영상 열기"))
        self.videoRecogEndBtn.setText(_translate("MainWindow", "종료"))
        self.videoRecogRunLabel.setText(_translate("MainWindow", "동영상 분석 중..78%"))
        self.videoRecogWorkLabel.setText(_translate("MainWindow", "순수근무시간 : 00:50:09"))
        self.videoRecogTotalLabel.setText(_translate("MainWindow", "총근무시간 : 1:00:09"))
        self.videoRecogNotWorkLabel.setText(_translate("MainWindow", "태만시간 : 00:10:00"))
        self.realRecogBox.setTitle(_translate("MainWindow", "실시간 인식"))
        self.realRecogStartBtn.setText(_translate("MainWindow", "시작"))
        self.realRecogEndBtn.setText(_translate("MainWindow", "종료"))
        self.realRecogCamLabel.setText(_translate("MainWindow", "카메라 화면"))
        self.faceRecogDisplayBtn.setText(_translate("MainWindow", "카메라끄기"))
        self.faceRecogSoundBtn.setText(_translate("MainWindow", "음성안내"))
        self.signalLampLabel.setText(_translate("MainWindow", "신호등"))
        self.realRecogWorkLabel.setText(_translate("MainWindow", "순수근무시간 : 00:50:09"))
        self.realRecogTotalLabel.setText(_translate("MainWindow", "총근무시간 : 1:00:09"))
        self.realRecogNotWorkLabel.setText(_translate("MainWindow", "태만시간 : 00:10:00"))
        self.userInfoBox.setTitle(_translate("MainWindow", "근무자 정보"))
        self.userNameLabel.setText(_translate("MainWindow", "근무자 이름"))
        self.userIdLabel.setText(_translate("MainWindow", "아이디 : sji"))
        self.userIPLabel.setText(_translate("MainWindow", "IP주소"))
        self.stgLvlLabel.setText(_translate("MainWindow", "사용자 인식 단계"))
        self.stgNodLabel.setText(_translate("MainWindow", "태만 기준 시간"))
        self.stgDecLabel.setText(_translate("MainWindow", "화면 탐지 시간 간격"))
        self.userImgLabel.setText(_translate("MainWindow", "사진"))
        self.logBox.setTitle(_translate("MainWindow", "로그확인"))
        self.logRefreshBtn.setText(_translate("MainWindow", "새로고침"))
        self.workListBox.setTitle(_translate("MainWindow", "근무 기록"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
