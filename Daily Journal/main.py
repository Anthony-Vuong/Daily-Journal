from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QCalendarWidget, \
    QHBoxLayout, QLabel
from PyQt5.QtCore import QSize, Qt, QDate

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Daily Journal")
        self.setFixedSize(QSize(1250, 750))

        self.year = 0
        self.day = 0
        self.month = 0

        self.datebox = QLabel()
        self.datebox.setAlignment(QtCore.Qt.AlignCenter)
        date = self.get_Today_Date()
        self.datebox.setText(date)

        self.editWindow = QTextEdit()
        self.save_button = QPushButton("Save")
        self.left_button = QPushButton("<")
        self.left_button.clicked.connect(self.last_day)
        self.right_button = QPushButton(">")
        self.right_button.clicked.connect(self.next_day)
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.get_Date)

        hlayout_date_save = QHBoxLayout()
        hlayout_date_save.addWidget(self.save_button)
        hlayout_date_save.addWidget(self.left_button)
        hlayout_date_save.addWidget(self.datebox)
        hlayout_date_save.addWidget(self.right_button)
        vlayout1 = QVBoxLayout()
        vlayout1.addLayout(hlayout_date_save)
        vlayout1.addWidget(self.editWindow)

        vlayout2 = QVBoxLayout()
        vlayout2.addWidget(self.calendar)

        mainlayout = QHBoxLayout()
        mainlayout.addLayout(vlayout1)
        mainlayout.addLayout(vlayout2)
        widget = QWidget()
        widget.setLayout(mainlayout)
        self.setCentralWidget(widget)



    def last_day(self):
        self.day = self.day - 1
        date = QDate(self.year, self.month, self.day)
        self.calendar.setSelectedDate(date)
        self.get_Date(date)

    def next_day(self):
        self.day = self.day + 1
        date = QDate(self.year, self.month, self.day)
        self.calendar.setSelectedDate(date)
        self.get_Date(date)

    def get_Today_Date(self):
        date = QDate.currentDate()
        self.day = int(date.toString(Qt.ISODate).split("-")[2])
        print(str(self.day))
        self.month = int(date.toString(Qt.ISODate).split("-")[1])
        self.year = int(date.toString(Qt.ISODate).split("-")[0])

        return date.toString(Qt.DefaultLocaleLongDate)


    def get_Date(self, qDate):
        day_of_week_int = qDate.dayOfWeek()
        dayWeek = qDate.longDayName(day_of_week_int)
        month_of_year_int = qDate.month()
        monthYear = qDate.longMonthName(month_of_year_int)
        date = ('{0}, {2} {3}, {1}'.format(dayWeek, qDate.year(), monthYear, qDate.day()))
        self.datebox.setText(date)



app = QApplication([])

window = MainWindow()

window.show()

app.exec()





