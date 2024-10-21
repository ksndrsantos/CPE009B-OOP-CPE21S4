import sys
import csv
from PyQt5.QtWidgets import QApplication
from registration import RegistrationApp
from PyQt5.QtCore import pyqtSlot

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationApp()
    sys.exit(app.exec_())