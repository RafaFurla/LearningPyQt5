from PyQt5 import uic, QtWidgets

def funcao_principal():
    if formulario.radioButton.isChecked():
        opcao = "opção 1 selecionada!"
    elif formulario.radioButton_2.isChecked():
        opcao = "opção 2 selecionada!"
    elif formulario.radioButton_3.isChecked():
        opcao = "opção 3 selecionada!"
    elif formulario.radioButton_5.isChecked():
        opcao = "opção 4 selecionada!"
    else:
        opcao = ""
    formulario.label_2.setText(f'Selected color: {opcao}')
app = QtWidgets.QApplication([])
formulario=uic.loadUi("class7-radiobuttons.ui")  # this creates a reference between the ui file and the object formulario
formulario.pushButton.clicked.connect(funcao_principal)  # formulario will call the ui file. pushButton will call the object pushButton inside the ui file. clicked will create an event when the button is clicked. connect will call the function "funcao_principal" after the button was clicked.

formulario.show()
app.exec()