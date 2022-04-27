from PyQt5.QtWidgets import *
import sys


class window(QWidget):
    def __init__(self):
        global buttongroup
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500, 500)
        button1 = QPushButton("button1")
        layout.addWidget(button1)
        button2 = QPushButton("button2")
        layout.addWidget(button2)
        button3 = QPushButton("button3")
        layout.addWidget(button3)
        buttongroup = QButtonGroup()
        buttongroup.addButton(button1, 1)
        buttongroup.addButton(button2, 2)
        buttongroup.addButton(button3, 3)
        buttongroup.buttonClicked[int].connect(self.on_button)

    def on_button(self, id):
        print("number %s clicked" % id)


app = QApplication(sys.argv)
screen = window()
screen.show()
sys.exit(app.exec_())
