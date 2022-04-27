from PyQt5.QtWidgets import *
import sys


class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500, 500)
        rb1 = QRadioButton("python")
        layout.addWidget(rb1)
        rb1.toggled.connect(self.rb1clicked)
        rb2 = QRadioButton("java")
        layout.addWidget(rb2)
        rb2.toggled.connect(self.rb2clicked)

    def rb1clicked(self):
        rb1 = self.sender()
        if rb1.isChecked():
            print("python selected")

    def rb2clicked(self):
        rb2 = self.sender()
        if rb2.isChecked():
            print("java selected")


app = QApplication(sys.argv)
screen = window()
screen.show()
sys.exit(app.exec_())
