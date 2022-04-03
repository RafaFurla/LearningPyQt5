from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Rotulari Learning PyQt5")
        self.initUI()

    def initUI(self):
        # Defining a label:
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50, 50)

        # Defining a button:
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    # Defining what happening when you click the b1 button
    def clicked(self):
        self.label.setText("You pressed the button")

    def update(self):
        self.label.adjustSize()
        self.update()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

# main code:
window()
