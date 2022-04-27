from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class window(QWidget):
    def __init__(self):
        global label, slider1
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(600, 600)
        slider1 = QSlider(Qt.Horizontal)
        slider1.setValue(4)
        layout.addWidget(slider1, 0, 0)
        slider2 = QSlider(Qt.Vertical)
        slider2.setValue(4)
        slider2.setTickPosition(QSlider.TicksBothSides)
        layout.addWidget(slider2, 0, 1)
        label = QLabel("label")
        layout.addWidget(label)
        button = QPushButton("slider1 value")
        layout.addWidget(button)
        button.clicked.connect(self.buttonclick)

    def buttonclick(self):
        label.setText(str(slider1.value()))


app = QApplication(sys.argv)
screen = window()
screen.show()
sys.exit(app.exec_())
