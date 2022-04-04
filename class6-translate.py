import sys
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
class mainwindow (QMainWindow):
    def __init__(self):
        super().__init__()
# Main window:
        self.setGeometry(100, 200, 800, 500)
        self.setWindowTitle("New Window")
# Centralwidget:
        self.workspace = QMainWindow()
        self.workspace.setObjectName("workspace")
        self.workspace.setGeometry(0, 0, 800, 500)
# Button1:
        self.button1 = QPushButton(self.workspace)
        self.button1.setText("Button1")
        self.button1.setGeometry(150, 200, 150, 80)
        self.button1.setObjectName("Button1")
        self.button1.setStyleSheet("QPushButton {background-color:#F5C507;color:'black';font:bold;font-size:20px}")
# Button2:
        self.button2 = QPushButton(self.workspace)
        self.button2.setText("Button2")
        self.button2.setGeometry(350, 200, 150, 80)
        self.button2.setObjectName("Button2")
        self.button2.setStyleSheet("QPushButton {background-color:#F50900;color:'black';font:bold;font-size:20px}")
# Label:
        self.label = QLabel(self.workspace)
        self.label.setText("Press any button!")
        self.label.setGeometry(50, 120, 300, 40)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel {color:'black'; font:bold; setfamily: Embassy BT; font-size: 25px}")
# Calling the project:
        self.setCentralWidget(self.workspace)
        self.show()

application = QApplication(sys.argv)
window = mainwindow()
sys.exit(application.exec())
