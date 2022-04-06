from PyQt5 import QtWidgets, uic
def buttonframe1():
    uifile.frame_2.close()  # the method close() closes the frame.
def buttonframe2():
    uifile.frame_2.show()  # the method show() open the frame.

app = QtWidgets.QApplication([])
uifile = uic.loadUi('class15-frame.ui')
uifile.pushButton_2.clicked.connect(buttonframe1)
uifile.pushButton_3.clicked.connect(buttonframe2)
uifile.show()
app.exec()