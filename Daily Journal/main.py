from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Daily Journal")
        button = QPushButton("PRESS")
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()














