from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(600, 600)
        label1 = QLabel("label1 spanning 2 columns")
        layout.addWidget(label1, 0, 0, 0, 2)
        label2 = QLabel("label2 spanning 2 rows")
        layout.addWidget(label2, 2, 0, 2, 2)


app = QApplication(sys.argv)
screen = window()
screen.show()
sys.exit(app.exec_())
