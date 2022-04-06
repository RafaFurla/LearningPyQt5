from PyQt5 import QtWidgets, uic

def save():
    name = uifile.lineEdit.text()
    age = uifile.lineEdit_3.text()
    phone = uifile.lineEdit_2.text()
    data = f'Name: {name}\nAge: {age}\nPhone Number: {phone}'
    file = QtWidgets.QFileDialog.getSaveFileName()[0]  # QfileDialog.getSaveFileName is a method that generates a list and saves the name of the file that user created and the path to that file in the position zero of the list. It's similar to the sys.argv
    with open(f'{file}.txt','w') as a:
        a.write(data)

app = QtWidgets.QApplication([])
uifile = uic.loadUi("class17-savebox-in-menubar.ui")
uifile.actionSave.triggered.connect(save)  # the menu bar generates actions. We create an actionSave and triggered it with our method above.
uifile.show()
app.exec()