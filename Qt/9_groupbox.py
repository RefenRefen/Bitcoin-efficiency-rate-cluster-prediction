from PyQt5.QtWidgets import *
import sys


class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(400, 400)
        box = QGroupBox("group box")
        layout.addWidget(box)
        box.setCheckable(True)
        sublayout = QGridLayout()
        box.setLayout(sublayout)
        button1 = QPushButton("button1")
        sublayout.addWidget(button1)
        button2 = QPushButton("button2")
        sublayout.addWidget(button2)


app = QApplication(sys.argv)
screen = window()
screen.show()
sys.exit(app.exec_())
