from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

def displaymsg():
    readed_data = ui_file.lineEdit.text()  # this saves the data input by the user.
    ui_file.lineEdit.setText("")  # This cleans the box that user use to input the data after press the verify button.
    if readed_data =="":
        QMessageBox.about(ui_file, "alert", "No name typed!")  # this creates a message box style about (there's a lot of styles of message boxes. About is just one of them). You have to input the (ui_file, message title, message) in the about method.
    else:
        QMessageBox.about(ui_file, "alert", readed_data)

# main code:
app = QtWidgets.QApplication([])
ui_file = uic.loadUi("class9-messagebox.ui")
ui_file.pushButton.clicked.connect(displaymsg)
ui_file.show()
app.exec_()