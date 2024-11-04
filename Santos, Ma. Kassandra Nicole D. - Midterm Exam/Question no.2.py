import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow, QPushButton
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Special Midterm Exam in OOP"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.button = QPushButton('Click to change color!', self)
        self.button.setToolTip("It Turned into Yellow!")
        self.button.clicked.connect(self.changeColor)
        self.button.move(100, 70)

        self.show()

    def changeColor(self):
        self.button.setStyleSheet("background-color: yellow;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = App()
    sys.exit(app.exec_())
