from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(600, 600)
        button1 = QPushButton("button1")
        button2 = QPushButton("button2")
        button3 = QPushButton("button3")
        splitter = QSplitter()
        layout.addWidget(splitter)
        splitter.addWidget(button1)
        splitter.addWidget(button2)
        splitter.addWidget(button3)
        splitter.setOrientation(Qt.Vertical)
        splitter.setHandleWidth(20)
        s = splitter.count()
        print(s)


app = QApplication(sys.argv)
screen = window()
screen.show()
sys.exit(app.exec_())
