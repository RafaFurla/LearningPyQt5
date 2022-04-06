from PyQt5 import QtWidgets, uic

def save():
    name = uifile.lineEdit.text()
    age = uifile.lineEdit_3.text()
    phone = uifile.lineEdit_2.text()
    data = f'Name: {name}\nAge: {age}\nPhone Number: {phone}'
    file = QtWidgets.QFileDialog.getSaveFileName()[0]
    with open(f'{file}.txt','w') as a:
        a.write(data)

def readfile():
    file = QtWidgets.QFileDialog.getOpenFileName()[0]  # QfileDialog.getOpenFileName is a method to search for open a file.
    with open(file,'r') as a:
        uifile.label_5.setText(a.read())


app = QtWidgets.QApplication([])
uifile = uic.loadUi("class18-openbox-in-menubar.ui")
uifile.actionSave.triggered.connect(save)
uifile.actionOpen.triggered.connect(readfile)
uifile.show()
app.exec()