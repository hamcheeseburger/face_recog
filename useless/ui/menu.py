import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
from useless.ui.menuUi import Ui_menuForm
from ui.video import ExecuteVideo
from useless.ui.useless_realTime import ExecuteRealTime
import subprocess


class jar_thread(QThread):
    def run(self):
        cmd = "java -jar ./Original_Tool/VideoAnalyzer.jar ./test.txt"
        os.system(cmd)


class ExecuteMenu(Ui_menuForm):
    def __init__(self, menuForm, id):
        Ui_menuForm.__init__(self)
        self.setupUi(menuForm)
        self.menuForm = menuForm
        self.processBtn.clicked.connect(self.callExe)
        self.jarBtn.clicked.connect(self.callJar)
        self.videoBtn.clicked.connect(self.call_video_recog)
        self.realTimeBtn.clicked.connect(self.call_realTime_recog)
        self.th1 = jar_thread()
        self.userIdLabel.setText(id + "님 환영합니다.")
        self.logoutBtn.clicked.connect(self.logout)

        self.menuForm.show()

    def callExe(self):
        # 윈도우 명령어는 쉘안에 들어있으므로 shell=Ture여야 윈도우 쉘 명령어 사용ok
        fileName = '../../Original_Tool/VideoAnalyzer.exe'
        subprocess.run(["start", fileName], shell=True)

    def callJar(self):
        self.th1.start()

    def call_realTime_recog(self):
        realTimeWidget = QtWidgets.QWidget()
        realTimeUi = ExecuteRealTime(self.realTimeWidget)

        realTimeWidget.show()

    def call_video_recog(self):
        self.videoWidget = QtWidgets.QWidget()
        self.videoUi = ExecuteVideo(self.videoWidget)

        self.videoWidget.show()

    def logout(self):
        dirname = 'user_image'
        files = os.listdir(dirname)
        for filename in files:
            path = dirname + '/' + filename
            os.remove(path)

        self.menuForm.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    menuForm = QtWidgets.QWidget()
    menuUi = ExecuteMenu(menuForm)
    menuForm.show()
    sys.exit(app.exec_())
