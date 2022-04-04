import sys

import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui  # this class (QtGui) makes possible to work with images

class window(QMainWindow):
    def __init__(self):
        super().__init__()
# defining main window:
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "New Window"
# defining the first button:
        button1 = QPushButton('Button1', self)
        button1.move(150, 200)
        button1.resize(150, 80)
        button1.setStyleSheet('QPushButton {background-color:#F5C507;font:bold;font-size:20px}')
        button1.clicked.connect(self.button1_click)
# defining the second button:
        button2 = QPushButton('Button2', self)
        button2.move(350, 200)
        button2.resize(150, 80)
        button2.setStyleSheet('QPushButton {background-color:#F50900;font:bold;font-size:20px}')
        button2.clicked.connect(self.button2_click)
# Defining the label:
        self.label1 = QLabel(self)
        self.label1.setText("Press any button!")
        self.label1.move(50, 50)
        self.label1.resize(300, 25)
        self.label1.setStyleSheet('QLabel {color:"Black";font:bold;font-size:25px}')
# Defining Images. Obs.: images could be an Label object in PyQt5:
        self.car = QLabel(self)  # defining the image as a label object.
        self.car.move (50, 400)  # Positioning image.
        self.car.resize(450, 180)  # size of the label box.

# Calling the window:
        self.loadwindow()

    def loadwindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def button1_click(self):
        self.label1.setText("Car 1 was Selected!")
        self.label1.setStyleSheet('QLabel {color:#F5C507;font:bold;font-size:25px}')
        self.car.setPixmap(QtGui.QPixmap('car1.png'))  # Here we will select image1.

    def button2_click(self):
        self.label1.setText("Car 2 was Selected!")
        self.label1.setStyleSheet('QLabel {color:#F50900;font:bold;font-size:25px}')
        self.car.setPixmap(QtGui.QPixmap('car2.png'))  # Here we will select image2.

# Main code:
application = QApplication(sys.argv)
w = window()
sys.exit(application.exec())