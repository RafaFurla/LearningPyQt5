import sys

import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel  # The class QLabel defines the labels objects.

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
        button1.setStyleSheet('QPushButton {background-color:#0FB328;font:bold;font-size:20px}')
        button1.clicked.connect(self.button1_click)
# defining the second button:
        button2 = QPushButton('Button2', self)
        button2.move(350, 200)
        button2.resize(150, 80)
        button2.setStyleSheet('QPushButton {background-color:#2FA6F5;font:bold;font-size:20px}')
        button2.clicked.connect(self.button2_click)
# Defining the label:
        self.label1 = QLabel(self)  # defining the self.label attribute as an object of the class QLabel.
        self.label1.setText("Press any button!")  # defining text content of the label.
        self.label1.move(50, 50)  # position of the label (left, height)
        self.label1.resize(300, 25)  # size of the label (width, height)
        self.label1.setStyleSheet('QLabel {color:"Black";font:bold;font-size:25px}')  # defining the style of the label
# Calling the window:
        self.loadwindow()

    def loadwindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def button1_click(self):
        self.label1.setText("Button 1 was clicked!")
        self.label1.setStyleSheet('QLabel {color:#0FB328;font:bold;font-size:25px}')

    def button2_click(self):
        self.label1.setText("Button 2 was clicked!")
        self.label1.setStyleSheet('QLabel {color:#2FA6F5;font:bold;font-size:25px}')

# Main code:
application = QApplication(sys.argv)
w = window()
sys.exit(application.exec())