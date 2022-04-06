from PyQt5 import QtWidgets, uic
def calculate():
    sum_ = 0
    if (uifile.checkBox_2.isChecked()):  # isChecked is a method that returns True or False. This method is used to know if the box was selected by the user.
        sum_ += 15.00
        uifile.checkBox_2.setChecked(False)  # In this case we are using the setChecked method to deselect the box after the sum.
    if (uifile.checkBox_4.isChecked()):
        sum_ += 20.00
        uifile.checkBox_4.setChecked(False)
    if (uifile.checkBox_5.isChecked()):
        sum_ += 10.00
        uifile.checkBox_5.setChecked(False)
    if (uifile.checkBox_3.isChecked()):
        sum_ += 32.00
        uifile.checkBox_3.setChecked(False)
    if (uifile.checkBox.isChecked()):
        sum_ += 5.50
        uifile.checkBox.setChecked(False)
    uifile.label.setText(f"Total Value: {sum_:.2f}")
app = QtWidgets.QApplication([])
uifile = uic.loadUi("class14-checkbox.ui")
uifile.pushButton.clicked.connect(calculate)
uifile.show()
app.exec()