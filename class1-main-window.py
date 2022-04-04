import sys

import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class window(QMainWindow):
    def __init__(self):
        super().__init__()
# defining main window:
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "New Window"
# Calling the window:
        self.loadwindow()

    def loadwindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)  # this set is for the size and position of the window
        self.setWindowTitle(self.title)  # This method is to put a text in the window.
        self.show()  # this is for display the window on the screen.


# Main code:
application = QApplication(sys.argv)  # 
w = window()  # defining the instance of the class.
sys.exit(application.exec())  # this is for close the script when you press the window close button.
