from PyQt5.QtWidgets import *
import sys


class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500, 500)
        button1 = QPushButton("button1")
        button2 = QPushButton("button2")
        button3 = QPushButton("button3")
        button1.setToolTip("tooltip button1")
        button2.setToolTip("tooltip button2")
        button3.setWhatsThis("whatsthis button3")
        layout.addWidget(button1, 0, 0)
        layout.addWidget(button2, 1, 0)
        layout.addWidget(button3, 2, 0)


app = QApplication(sys.argv)
screen = window()
screen.show()
sys.exit(app.exec_())
