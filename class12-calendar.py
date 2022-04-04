from PyQt5 import QtWidgets, uic
def date():
    date = str(uifile.calendarWidget.selectedDate())  # output date that user selected with the cursor.
    year = date[19:23]
    month = date[24:26]
    day = date[27:30].replace(")","")
    uifile.label.setText(f'Selected Date: {year}/{month}/{day}')

app = QtWidgets.QApplication([])
uifile = uic.loadUi("class12-calendar.ui")
uifile.calendarWidget.selectionChanged.connect(date)
uifile.show()
app.exec()
