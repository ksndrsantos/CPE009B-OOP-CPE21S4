import sys
from PyQt5.QtWidgets import QMainWindow,QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QApplication
from PyQt5.QtGui import QIcon
class GridExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid=QGridLayout()
        self.setLayout(grid)

        names = [
          '7', '8', '9', '/', 'sin', '',
          '4', '5', '6', '*', 'cos', '',
          '1', '2', '3', '-', 'tan','',
          '0', '.', '=','+', ' clear' '',
          '',  '', '',  '', '', '','',
        ]

        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0,1,1,5)

        positions = [(i,j) for i in range (1,7) for j in range (1,6)]
        for position, name in zip(positions,names):
            if name == '':
                continue
            button=QPushButton(name)
            grid.addWidget(button, *position)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Scientific Calculator')
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=GridExample()
    sys.exit(app.exec_())