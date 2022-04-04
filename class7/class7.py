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
formulario=uic.loadUi("class7-radiobuttons.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()