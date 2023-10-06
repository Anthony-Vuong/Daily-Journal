from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Daily Journal")
        button = QPushButton("PRESS")
        self.setFixedSize(QSize(1250, 750))
        self.setCentralWidget(button)
        "This is a commnet"


app = QApplication([])

window = MainWindow()

window.show()

app.exec()





