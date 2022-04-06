from PyQt5 import QtWidgets, uic
def option():
    city = uifile.comboBox.currentText()  # currentText is the method that permits us to see or save the choose of the user.
    uifile.label_2.setText(f'City: {city}')

app = QtWidgets.QApplication([])
uifile = uic.loadUi('class16-combo-box.ui')
uifile.pushButton.clicked.connect(option)
uifile.comboBox.addItems(["", "São Paulo", "Rio de Janeiro", "Curitiba", "Sorocaba"])  # addItems makes a list of contents to the combo Box.
uifile.show()
app.exec()