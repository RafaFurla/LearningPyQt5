from PyQt5 import QtWidgets, uic
value = 0
def increase():
    global value
    value += 10
    uifile.progressBar.setValue(value)

def zering():
    global value
    uifile.progressBar.setValue(0)
    value = 0

app = QtWidgets.QApplication([])
uifile = uic.loadUi("class11-progressbar.ui")
uifile.pushButton.clicked.connect(increase)
uifile.pushButton_2.clicked.connect(zering)
uifile.show()
app.exec()