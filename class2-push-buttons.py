import sys

import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip #QToolTip is for customizing the buttons. QPushButton is to make the objects.

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
        button1.move(150, 200)  # Position of the button left and height
        button1.resize(150, 80)  # size of the button width and height
        button1.setStyleSheet('QPushButton {background-color:#0FB328;font:bold;font-size:20px}')  # this method is for put style in the button. It's very similar to CSS style. #0FB328 is the background color in hexadecimal
        button1.clicked.connect(self.button1_click)  # this method is used to call another method that will be the specification of what will gonna happen if the button was clicked.
# defining the second button:
        button2 = QPushButton('Button2', self)
        button2.move(350, 200)
        button2.resize(150, 80)
        button2.setStyleSheet('QPushButton {background-color:#2FA6F5;font:bold;font-size:20px}')
        button2.clicked.connect(self.button2_click)
# Calling the window:
        self.loadwindow()

    def loadwindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)  # this set is for the size and position of the window
        self.setWindowTitle(self.title)  # This method is to put a text in the window.
        self.show()  # this is for display the window on the screen.

    def button1_click(self):
        print('Button 1 was clicked!')

    def button2_click(self):
        print('Button 2 was clicked!')

# Main code:
application = QApplication(sys.argv)  #
w = window()  # defining the instance of the class.
sys.exit(application.exec())  # this is for close the script when you press the window close button.