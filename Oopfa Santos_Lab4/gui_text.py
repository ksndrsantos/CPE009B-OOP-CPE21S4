import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()  # Initialize the main window like the previous one
        # window = QMainwIndow()
        self.title = "PyQt Line Edit"
        self.x = 200  # or left
        self.y = 200  # or top
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        #create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20,20)
        self.textbox.resize(250,40)
        self.textbox.setText("Set this text Value")

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())