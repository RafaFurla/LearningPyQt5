from PyQt5 import QtWidgets, uic

def openotherpage():
    ui_file2.show()

app = QtWidgets.QApplication([])
ui_file1 = uic.loadUi("class10-adding-other-page1.ui")
ui_file2 = uic.loadUi("class10-adding-other-page2.ui")
ui_file1.pushButton.clicked.connect(openotherpage)
ui_file1.show()
app.exec()