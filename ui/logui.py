import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, QFileDialog, QTextEdit, \
    QScrollArea
from PyQt5 import QtWidgets, QtCore, QtGui


class LogUi(QWidget):
    def __init__(self):
        # 근무 확인 아이콘 생성
        QWidget.__init__(self)

        self.resize(800, 370)
        scrollArea = QScrollArea()
        self.layout = QVBoxLayout()

        file = './server.log'
        with open(file) as rFile:
            content = rFile.read()

        self.message = QLabel(content)
        self.message.setFont(QtGui.QFont("", 10))
        scrollArea.setWidget(self.message)

        self.layout.addWidget(scrollArea)
        self.setLayout(self.layout)
        self.setWindowTitle("근무로그확인")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = LogUi()
    ui.show()
    sys.exit(app.exec_())