from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QRadioButton, QApplication, QLabel, QPushButton
import sys


class window(QMainWindow):
    def __init__(self):
        super().__init__()
#Main window:
        self.setObjectName('MainWindow')
        self.setGeometry(850, 40, 432, 428)
        self.setStyleSheet("background-color: rgb(233, 255, 245);")
        self.setWindowTitle("Radio Buttons")
#Central Widget:
        self.workspace = QWidget()
        self.workspace.setObjectName("centralwidget")
        self.setGeometry(850, 40, 432, 428)
#RadioButton1:
        self.radiobutton1 = QRadioButton(self.workspace)
        self.radiobutton1.setText('Blue')
        self.radiobutton1.setGeometry(130, 120, 131, 17)
        self.radiobutton1.setStyleSheet('QRadioButton {color:"black";font:bold;font-size:15px}')
        self.radiobutton1.setObjectName('RadioButton1')
# RadioButton2:
        self.radiobutton2 = QRadioButton(self.workspace)
        self.radiobutton2.setText('Green')
        self.radiobutton2.setGeometry(130, 160, 131, 17)
        self.radiobutton2.setStyleSheet('QRadioButton {color:"black";font:bold;font-size:15px}')
        self.radiobutton2.setObjectName('RadioButton2')
# RadioButton3:
        self.radiobutton3 = QRadioButton(self.workspace)
        self.radiobutton3.setText('Yellow')
        self.radiobutton3.setGeometry(130, 200, 131, 17)
        self.radiobutton3.setStyleSheet('QRadioButton {color:"black";font:bold;font-size:15px}')
        self.radiobutton3.setObjectName('RadioButton3')
# RadioButton4:
        self.radiobutton4 = QRadioButton(self.workspace)
        self.radiobutton4.setText('Red')
        self.radiobutton4.setGeometry(130, 240, 131, 17)
        self.radiobutton4.setStyleSheet('QRadioButton {color:"black";font:bold;font-size:15px}')
        self.radiobutton4.setObjectName('RadioButton4')
# Label 1:
        self.label1 = QLabel(self.workspace)
        self.label1.setText("Select one color: ")
        self.label1.setGeometry(120, 50, 171, 21)
        self.label1.setStyleSheet('QLabel {color: rgb(85, 170, 127);font:bold;font-size:20px}')
        self.label1.setObjectName("Label: main title")
# Label 2:
        self.label2 = QLabel(self.workspace)
        self.label2.setText("Selected color: ")
        self.label2.setGeometry(50, 340, 350, 30)
        self.label2.setStyleSheet('QLabel {color: "black";font:bold;font-size:20px}')
        self.label2.setObjectName("Label: color select")
# PushButton
        self.pushButton = QPushButton(self.workspace)
        self.pushButton.setGeometry(120, 270, 141, 51)
        self.pushButton.setStyleSheet('QPushButton {background-color: rgb(85, 170, 255);font:bold;font-size:20px}')
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Send")
        self.pushButton.clicked.connect(self.pushbuttonclick)
#Calling graphics:
        self.setCentralWidget(self.workspace)
        self.show()

    def pushbuttonclick(self):
        if self.radiobutton1.isChecked():
            option = "option 1 selected!"
        elif self.radiobutton2.isChecked():
            option = "option 2 selected!"
        elif self.radiobutton3.isChecked():
            option = "option 3 selected!"
        elif self.radiobutton4.isChecked():
            option = "option 4 selected!"
        else:
            option = ""
        self.label2.setText(f'Selected color: {option}')


app = QApplication(sys.argv)
win = window()
sys.exit(app.exec_())