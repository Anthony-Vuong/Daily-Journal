import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QCalendarWidget, \
    QHBoxLayout, QLabel
from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.conn = None
        self.selected_date = None

        # Variable that contain selected date in day, month, and year
        self.year = 0
        self.day = 0
        self.month = 0

        self.init_UI()
        self.init_database()

    # Initializie the user interface
    def init_UI(self):
        self.setWindowTitle("Daily Journal")
        self.setFixedSize(QSize(1250, 750))
        self.datebox = QLabel()
        self.datebox.setAlignment(QtCore.Qt.AlignCenter)
        today_date = self.get_today_date()
        self.datebox.setText(today_date)

        self.editWindow = QTextEdit()
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_edit)
        self.left_button = QPushButton("<")
        self.left_button.clicked.connect(self.last_day)
        self.right_button = QPushButton(">")
        self.right_button.clicked.connect(self.next_day)
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.get_selected_date)

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


    def init_database(self):
        self.add_connect_database()

        self.create_database_table()


    def add_connect_database(self):
        # Databse prototyping
        # CREATE TABLE new_employee ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL, resume BLOB NOT NULL);
        self.conn = QSqlDatabase.addDatabase("QSQLITE")
        self.conn.setDatabaseName("entry_records.sqlite")

        if not self.conn.open():
            print("Database Error: %s" % self.conn.lastError().databaseText())
            sys.exit(1)
        else:
            print("Database successfully connected.")

    def create_database_table(self):

        createTableQuery = QSqlQuery()
        createTableQuery.exec(

            """
            CREATE TABLE journal_entries ( 
                id INTEGER PRIMARY KEY, 
                date TEXT NOT NULL, 
                text_entry TEXT NOT NULL, 
                files BLOB NOT NULL
            )
            """
        )

        print(self.conn.tables())

    def add_to_table(self, id, curr_date, t, file):

        a=id
        b=curr_date
        c=t
        d=file

        query = QSqlQuery()
        # ID cannot be 0
        l = query.exec(
            f"""INSERT INTO journal_entries (id, date, text_entry, files) 
                    VALUES ('{a}', '{b}', '{c}', '{d}')"""
        )

        print(str(l))

    # Save button signal function
    def save_edit(self):

        # 1. Search for date
        # 2. Compare text plain to database text
        #       * if different, popup ask user if want to overwrite
        #       * if same, do nothing
        # 3.

        t = str(self.editWindow.toPlainText())

        d = self.get_selected_date


        self.add_to_table(123, self.selected_date, t, None)



    ################################################################################
    #           Both last_day() and next_day() need logic for moving into next month
    #           or previous month
    ################################################################################

    # Left button signal function
    # Gets the previous date and displays in QLabel "datebox"
    def last_day(self):
        self.day = self.day - 1
        date = QDate(self.year, self.month, self.day)
        self.calendar.setSelectedDate(date)
        self.get_selected_date(date)

    # Right button signal function
    # Gets the next date and displays in QLabel "datebox"
    def next_day(self):
        self.day = self.day + 1
        date = QDate(self.year, self.month, self.day)
        self.calendar.setSelectedDate(date)
        self.get_selected_date(date)

    ################################################################################
    ################################################################################

    # Initialize function for the current date
    def get_today_date(self):
        date = QDate.currentDate()
        self.update_selected_date(date)
        return date.toString(Qt.DefaultLocaleLongDate)

    # Function to display the date in a specific format - Weekday, Month Day, Year
    def get_selected_date(self, qDate):
        day_of_week_int = qDate.dayOfWeek()
        dayWeek = qDate.longDayName(day_of_week_int)
        month_of_year_int = qDate.month()
        monthYear = qDate.longMonthName(month_of_year_int)
        self.selected_date = ('{0}, {2} {3}, {1}'.format(dayWeek, qDate.year(), monthYear, qDate.day()))
        self.datebox.setText(self.selected_date)
        self.update_selected_date(qDate)


    #def set_selected_date(self):



    def update_selected_date(self, selected_date):
        self.day = int(selected_date.toString(Qt.ISODate).split("-")[2])
        self.month = int(selected_date.toString(Qt.ISODate).split("-")[1])
        self.year = int(selected_date.toString(Qt.ISODate).split("-")[0])




# Should throw this in main function
app = QApplication([])

window = MainWindow()

window.show()

app.exec()





