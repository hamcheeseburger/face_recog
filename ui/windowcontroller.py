from PyQt5 import QtWidgets

from pygui_v2 import Ui_MainWindow


class WindowController(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)

        # Setting button click listener
        self.logoutBtn.clicked.connect(self.logout)
        self.realRecogStartBtn.clicked.connect(self.realRecogStart)
        self.realRecogEndBtn.clicked.connect(self.realRecogEnd)
        self.realRecogSoundBtn.clicked.connect(self.realRecogSound)
        self.videoCheckOpenBtn.clicked.connect(self.videoCheckOpen)
        self.videoCheckBtn.clicked.connect(self.videoCheck)
        self.videoRecogOpenBtn.clicked.connect(self.videoRecogOpen)
        self.videoRecogEndBtn.clicked.connect(self.videoRecogEnd)

        self.workListView.append("날짜시각\t근무타입\t근무시간")

        self.show()

    def logout(self):
        print("logoutBtn clicked")

    def realRecogStart(self):
        print("realRecogStartBtn clicked")

    def realRecogEnd(self):
        print("realRecogEndBtn clicked")

    def realRecogSound(self):
        print("realRecogSoundBtn clicked")

    def videoCheckOpen(self):
        print("videoCheckOpenBtn clicked")

    def videoCheck(self):
        print("videoCheckBtn clicked")

    def videoRecogOpen(self):
        print("videoRecogOpenBtn clicked")

    def videoRecogEnd(self):
        print("videoRecogEndBtn clicked")


    def addWorkToworkListView(self, workString):
        self.workListView.append(workString)

    def closeEvent(self, event):
        print("closed")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pygui = WindowController()
    pygui.addWorkToworkListView("추가한 글")
    sys.exit(app.exec_())