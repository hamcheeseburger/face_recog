# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_210218_레이아웃_설정o.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(21, 11, 1141, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 372, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(370, 150))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 330, 125))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(370, 170))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 331, 131))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(110, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QtCore.QSize(370, 150))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 30, 330, 120))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.groupBox_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(410, 50, 372, 531))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(370, 50))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 211, 16))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(370, 0))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 30, 332, 431))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QtCore.QSize(330, 260))
        self.label_28.setObjectName("label_28")
        self.verticalLayout_5.addWidget(self.label_28)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(140, 40))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.groupBox_8 = QtWidgets.QGroupBox(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_8)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 160, 61))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.verticalLayout_5.addWidget(self.groupBox_8)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(800, 110, 371, 471))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBox_6 = QtWidgets.QGroupBox(self.verticalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_6)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 30, 331, 141))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_7.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_7.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_8.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_7.addWidget(self.pushButton_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.groupBox_7 = QtWidgets.QGroupBox(self.verticalLayoutWidget_5)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_7)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 20, 201, 61))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_7.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_7.addWidget(self.label_19)
        self.verticalLayout_6.addWidget(self.groupBox_7)
        self.verticalLayout_10.addWidget(self.groupBox_6)
        self.groupBox_11 = QtWidgets.QGroupBox(self.verticalLayoutWidget_9)
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_11)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 20, 331, 231))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_9.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_8.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_10.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_8.addWidget(self.pushButton_10)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.groupBox_10 = QtWidgets.QGroupBox(self.verticalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_20 = QtWidgets.QLabel(self.groupBox_10)
        self.label_20.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label_20.setObjectName("label_20")
        self.verticalLayout_8.addWidget(self.groupBox_10)
        self.groupBox_9 = QtWidgets.QGroupBox(self.verticalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 90))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.groupBox_9)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 10, 160, 61))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_9.addWidget(self.label_16)
        self.verticalLayout_8.addWidget(self.groupBox_9)
        self.verticalLayout_10.addWidget(self.groupBox_11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1218, 26))
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
        self.pushButton_5.setText(_translate("MainWindow", "로그아웃"))
        self.pushButton_6.setText(_translate("MainWindow", "근무기록"))
        self.groupBox.setTitle(_translate("MainWindow", "근무 기록"))
        self.groupBox_2.setTitle(_translate("MainWindow", "근무자 정보"))
        self.label_3.setText(_translate("MainWindow", "근무자 이름"))
        self.label_4.setText(_translate("MainWindow", "아이디 : sji"))
        self.label_5.setText(_translate("MainWindow", "IP주소"))
        self.label_6.setText(_translate("MainWindow", "사용자 인식 단계"))
        self.label_7.setText(_translate("MainWindow", "태만 기준 시간"))
        self.label_8.setText(_translate("MainWindow", "화면 탐지 시간 간격"))
        self.label.setText(_translate("MainWindow", "사진"))
        self.groupBox_5.setTitle(_translate("MainWindow", "로그확인"))
        self.groupBox_3.setTitle(_translate("MainWindow", "현재시각"))
        self.label_2.setText(_translate("MainWindow", "2020년 2월 4일 오후 11:32"))
        self.groupBox_4.setTitle(_translate("MainWindow", "실시간 인식"))
        self.pushButton.setText(_translate("MainWindow", "시작"))
        self.pushButton_2.setText(_translate("MainWindow", "종료"))
        self.label_28.setText(_translate("MainWindow", "카메라 화면"))
        self.pushButton_4.setText(_translate("MainWindow", "음성안내"))
        self.label_13.setText(_translate("MainWindow", "신호등"))
        self.label_11.setText(_translate("MainWindow", "순수근무시간 : 00:50:09"))
        self.label_10.setText(_translate("MainWindow", "총근무시간 : 1:00:09"))
        self.label_12.setText(_translate("MainWindow", "태만시간 : 00:10:00"))
        self.groupBox_6.setTitle(_translate("MainWindow", "동영상 검증"))
        self.pushButton_7.setText(_translate("MainWindow", "동영상 열기"))
        self.pushButton_8.setText(_translate("MainWindow", "동영상 검증"))
        self.groupBox_7.setTitle(_translate("MainWindow", "동영상 정보"))
        self.label_17.setText(_translate("MainWindow", "동영상 파일 이름"))
        self.label_18.setText(_translate("MainWindow", "동영상 저장 경로"))
        self.label_19.setText(_translate("MainWindow", "동영상 길이"))
        self.groupBox_11.setTitle(_translate("MainWindow", "동영상 인식"))
        self.pushButton_9.setText(_translate("MainWindow", "동영상 열기"))
        self.pushButton_10.setText(_translate("MainWindow", "종료"))
        self.label_20.setText(_translate("MainWindow", "동영상 분석 중..78%"))
        self.label_14.setText(_translate("MainWindow", "순수근무시간 : 00:50:09"))
        self.label_15.setText(_translate("MainWindow", "총근무시간 : 1:00:09"))
        self.label_16.setText(_translate("MainWindow", "태만시간 : 00:10:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())