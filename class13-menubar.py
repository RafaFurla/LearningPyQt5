from PyQt5 import QtWidgets, uic
def menubar_green():
    uifile.label_2.setText("Green")
    uifile.label_2.setStyleSheet("color: green")

def menubar_red():
    uifile.label_2.setText("Red")
    uifile.label_2.setStyleSheet("color: red")

def menubar_blue():
    uifile.label_2.setText("Blue")
    uifile.label_2.setStyleSheet("color: blue")

app = QtWidgets.QApplication([])
uifile = uic.loadUi("class13-menubar.ui")
uifile.actionGreen.triggered.connect(menubar_green)  # When we are using menubar we use this method triggered instead clicked.
uifile.actionRed.triggered.connect(menubar_red)
uifile.actionBlue.triggered.connect(menubar_blue)
uifile.show()
app.exec()