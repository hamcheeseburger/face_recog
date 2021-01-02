import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from menuUi import Ui_menuForm


class ExecuteMenu(Ui_menuForm):
    def __init__(self, menuForm):
        Ui_menuForm.__init__(self)
        self.setupUi(menuForm)

        self.jarBtn.clicked.connect(self.callJar)

    def callJar(self):
        # msg = QMessageBox()
        # msg.setText('jar!')
        # msg.exec_()
        cmd = "java -jar ./Original_Tool/VideoAnalyzer.jar ./test.txt"
        os.system(cmd)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    menuForm = QtWidgets.QWidget()
    menuUi = ExecuteMenu(menuForm)
    menuForm.show()
    sys.exit(app.exec_())
