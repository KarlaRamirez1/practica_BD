from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QDialog, 
							QMessageBox,  QLabel,
							QTableWidgetItem, QLineEdit)
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui


################################################################################
class Login(QDialog):#faltan validaciones
	def __init__(self):
		super().__init__()
		loadUi('UI/login.ui', self)

		
		self.User.setPlaceholderText("Administrador")
		self.Password.setPlaceholderText("Contraseña")
		self.Password.setEchoMode(QLineEdit.Password)
		self.cancel = False
		self.btnActive = False
		self.UserType = -1
		self.Access.clicked.connect(self.connect)
	
	def connect(self):
		if self.User.text() != "Admin":
			QMessageBox.about(self,"Error", "Usuario Incorrecto.")
			return
		if self.Password.text() != "1234":
			QMessageBox.about(self,"Error", "Contraseña Incorrecta.")
			return
		#Recoger datos usuario.
		#self.UserType = 0
		self.btnActive = True
		self.close()
	
	def closeEvent(self, event):
		if self.btnActive == False:
			self.cancel = True
################################################################################

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	GUI = Login()
	GUI.show()
	app.exec_()
