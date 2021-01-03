import os
from gui import Gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox, QApplication
from menuUi import Ui_menuForm
from video import ExecuteVideo

class jar_thread(QThread):
    def run(self):
        cmd = "java -jar ./Original_Tool/VideoAnalyzer.jar ./test.txt"
        os.system(cmd)

class ExecuteMenu(Ui_menuForm):
    def __init__(self, menuForm):
        Ui_menuForm.__init__(self)
        self.setupUi(menuForm)

        self.jarBtn.clicked.connect(self.callJar)
        self.videoBtn.clicked.connect(self.call_video_recog)
        self.th1 = jar_thread()

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
