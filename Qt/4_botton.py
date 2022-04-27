from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import sys


class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(600, 500)
        button = QPushButton("Click ME")
        layout.addWidget(button)
        button.setIcon(QtGui.QIcon(r"F:\Academic\Faradars\PyQt5\FVPHT9709-S02\Files and Codes\3.2.png"))
        button.clicked.connect(self.buttonclicked)

    def buttonclicked(self):
        print("the pushbutton clicked")


app = QApplication(sys.argv)
screen = window()
screen.show()
sys.exit(app.exec_())
