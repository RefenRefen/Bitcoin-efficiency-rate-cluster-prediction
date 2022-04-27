import time

from PyQt5.QtWidgets import *
import sys
from time import sleep


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(400, 300)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sleep(2)
screen.setMinimumWidth(800)
sys.exit(app.exec_())
