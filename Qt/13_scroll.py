from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500, 600)
        scrollbar = QScrollBar(Qt.Vertical)
        layout.addWidget(scrollbar)
        scrollarea = QScrollArea()
        layout.addWidget(scrollarea)
        scrollarea.setAlignment(Qt.AlignTop)
        label = QLabel("aaaaaaa444444444444aaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccccdddddddddddddddddddddddd")
        scrollarea.setWidget(label)


app = QApplication(sys.argv)
screen = window()
screen.show()
sys.exit(app.exec_())
