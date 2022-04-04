import sys

import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

class window(QMainWindow):
    def __init__(self):
        super().__init__()
# Main window:
        self.top = 100
        self.left = 200
        self.width = 800
        self.height = 500
        self.title = "New Window"
# First button:
        button1 = QPushButton('Button1', self)
        button1.move(150, 200)
        button1.resize(150, 80)
        button1.setStyleSheet('QPushButton {background-color:#F5C507;font:bold;font-size:20px}')
        button1.clicked.connect(self.button1_click)
# Second button:
        button2 = QPushButton('Button2', self)
        button2.move(350, 200)
        button2.resize(150, 80)
        button2.setStyleSheet('QPushButton {background-color:#F50900;font:bold;font-size:20px}')
        button2.clicked.connect(self.button2_click)
# Third button:
        button_box = QPushButton('Send Text', self)
        button_box.move(550, 200)
        button_box.resize(150, 80)
        button_box.setStyleSheet('QPushButton {background-color:"lightblue";font:bold;font-size:20px}')
        button_box.clicked.connect(self.buttonbox_click)
# Label (car):
        self.label1 = QLabel(self)
        self.label1.setText("Press any button!")
        self.label1.move(50, 120)
        self.label1.resize(300, 25)
        self.label1.setStyleSheet('QLabel {color:"Black";font:bold;font-size:25px}')
# Label (text):
        self.label_box = QLabel(self)
        self.label_box.setText("Typed:")
        self.label_box.move(450, 120)
        self.label_box.resize(260, 25)
        self.label_box.setStyleSheet('QLabel {color:"Black";font:bold;font-size:25px}')
# Images. Obs.: images could be an Label object in PyQt5:
        self.car = QLabel(self)
        self.car.move (50, 300)
        self.car.resize(450, 180)
# Line Edit:
        self.text_box = QLineEdit(self)  # defining the Line Edit.
        self.text_box.move(25, 20)  # positioning the Line Edit box (left, height).
        self.text_box.resize(220, 40)  # Size of the line edit box (width, height).
# Calling the window:
        self.loadwindow()

    def loadwindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def button1_click(self):
        self.label1.setText("Car 1 was Selected!")
        self.label1.setStyleSheet('QLabel {color:#F5C507;font:bold;font-size:25px}')
        self.car.setPixmap(QtGui.QPixmap('car1.png'))

    def button2_click(self):
        self.label1.setText("Car 2 was Selected!")
        self.label1.setStyleSheet('QLabel {color:#F50900;font:bold;font-size:25px}')
        self.car.setPixmap(QtGui.QPixmap('car2.png'))

    def buttonbox_click(self):
        contents = self.text_box.text()  # this function already pick the user input in the string class way.
        self.label_box.setText(f'Typed: {contents}')  # this method setText is like the print method.

# Main code:
application = QApplication(sys.argv)
w = window()
sys.exit(application.exec())