import sys
from PyQt5.QtWidgets import *


class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500, 500)
        self.cb1 = QCheckBox("number 1")
        self.cb1.setChecked(True)
        layout.addWidget(self.cb1)
        self.cb1.toggled.connect(self.checkbox)
        self.cb2 = QCheckBox("number 2")
        layout.addWidget(self.cb2)
        self.cb2.toggled.connect(self.checkbox)
        self.cb2.setTristate(True)

    def checkbox(self):
        if self.cb1.isChecked():
            print("checkbox1 clicked")
        if self.cb2.isChecked():
            print("checkbox2 clicked")


app = QApplication(sys.argv)
screen = window()
screen.show()
sys.exit(app.exec_())
