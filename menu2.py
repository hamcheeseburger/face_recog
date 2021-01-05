import os
from gui import Gui
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox, QApplication
from video import ExecuteVideo
# from video2 import ExecuteVideo
from gui import Gui
import subprocess
from menuUi2 import MenuUi

class jar_thread(QThread):
    def run(self):
        cmd = "java -jar ./Original_Tool/VideoAnalyzer.jar ./test.txt"
        os.system(cmd)


class ExecuteMenu(MenuUi):
    def __init__(self, id):
        MenuUi.__init__(self)

        self.user_id = id
        self.processBtn.clicked.connect(self.callExe)
        self.jarBtn.clicked.connect(self.callJar)
        self.videoBtn.clicked.connect(self.call_video_recog)
        self.th1 = jar_thread()
        self.userIdLabel.setText(id + "님 환영합니다.")
        self.logoutBtn.clicked.connect(self.logout)

        self.show()

    def callExe(self):
        # 윈도우 명령어는 쉘안에 들어있으므로 shell=Ture여야 윈도우 쉘 명령어 사용ok
        fileName = './Original_Tool/VideoAnalyzer.exe'
        subprocess.run(["start", fileName], shell=True)

    def callJar(self):
        self.th1.start()

    def call_video_recog(self):
        # self.videoWidget = QtWidgets.QWidget()
        # self.videoUi = ExecuteVideo(self.videoWidget, self.user_id)
        #
        # self.videoWidget.show()

        self.videoExe = ExecuteVideo(self.user_id)
    def logout(self):
        dirname = 'user_image'
        files = os.listdir(dirname)
        for filename in files:
            path = dirname + '/' + filename
            os.remove(path)

        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        print("closed")
        self.logout()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    menuForm = QtWidgets.QWidget()
    menuUi = ExecuteMenu(menuForm)
    menuForm.show()
    sys.exit(app.exec_())
