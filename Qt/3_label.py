from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        label=QLabel("Faradars")
        layout.addWidget(label)
        label.setIndent(10)
        label.setMargin(50)
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
