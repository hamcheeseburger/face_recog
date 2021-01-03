import os
from gui import Gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox, QApplication
from menuUi import Ui_menuForm
from video import ExecuteVideo

import subprocess


class jar_thread(QThread):
    def run(self):
        cmd = "java -jar ./Original_Tool/VideoAnalyzer.jar ./test.txt"
        os.system(cmd)


class ExecuteMenu(Ui_menuForm):
    def __init__(self, menuForm):
        Ui_menuForm.__init__(self)
        self.setupUi(menuForm)

        self.processBtn.clicked.connect(self.callExe)
        self.jarBtn.clicked.connect(self.callJar)
        self.videoBtn.clicked.connect(self.call_video_recog)
        self.th1 = jar_thread()


    def callExe(self):
        # 윈도우 명령어는 쉘안에 들어있으므로 shell=Ture여야 윈도우 쉘 명령어 사용ok
        fileName = './Original_Tool/VideoAnalyzer.exe'
        subprocess.run(["start", fileName], shell=True)

    def callJar(self):
        self.th1.start()

    def call_video_recog(self):
        self.videoWidget = QtWidgets.QWidget()
        self.videoUi = ExecuteVideo(self.videoWidget)

        self.videoWidget.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    menuForm = QtWidgets.QWidget()
    menuUi = ExecuteMenu(menuForm)
    menuForm.show()
    sys.exit(app.exec_())
