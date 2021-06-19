import sys
import sqlite3
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QMessageBox,
							QPushButton, QLabel,QTableWidgetItem,
							QAbstractItemView)
from PyQt5.QtGui import QIcon, QColor
from PyQt5 import QtWidgets, QtCore #,QtGui
from PyQt5.uic import loadUi
from Modules.login import Login

conexion = sqlite3.connect("BD_BañosCharly_Master")


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI/main.ui', self)

        self.login = Login()
        self.login.exec_()
        if self.login.cancel:
            QMessageBox.about(self,"Error","No se puede cerrar sin acceder.")
            sys.exit(self)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	GUI = Main()
	GUI.show()
	sys.exit(app.exec_())
