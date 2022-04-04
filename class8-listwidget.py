from PyQt5 import QtWidgets, uic

def list_data():
    readed_data = ui_file.lineEdit.text()  # This will save the user input in "readed_data"
    ui_file.listWidget.addItem(readed_data)  # This will add the input of the user in the table.
    ui_file.lineEdit.setText("")  # This cleans the table after we press the send button.

def delete():
    ui_file.listWidget.clear()  # This clears all the table.

app = QtWidgets.QApplication([])
ui_file = uic.loadUi("class8-listwidget.ui")  # This makes a reference between the ui file and the object ui_file
ui_file.pushButton.clicked.connect(list_data)  # connects the 'clicked' method of button 1 with the function that describes what button 1 does.
ui_file.pushButton_2.clicked.connect(delete)  # connects the 'clicked' method of button 2 with the function that describes what button 2 does.

ui_file.show()
app.exec()
